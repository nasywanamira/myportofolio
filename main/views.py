import datetime
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST

from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm


def is_editor(user): # True kalo user bagian dari Editor
    return user.groups.filter(name="Editor").exists()


def show_main(request): # untuk main page aka Profile
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Nasywa Namira Suhendro",
        "npm": "2506532196",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Driven by curiosity and learning by doing. I show up, embrace the challenge (even if it's scary), "
            "and figure it out as I go ;). especially in business analysis and partnerships!!"
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)
# request.COOKIES.get('last_login', ...) membaca nilai dari cookie bernama last_login. Kita menggunakan method .get() dengan nilai default agar aplikasi tidak melempar error (KeyError) jika pengunjung membuka halaman utama sebelum login atau jika cookie belum tersedia.
# Nilai string tanggal tersebut kita masukkan ke dalam dictionary context dengan kunci "last_login".


def show_experience(request): # untuk Experience page
    context = {
        "name": "Nasywa Namira Suhendro",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request): # untuk Education page
    # cuma ngerender kerangka halaman. Datanya sengaja nggak dikirim
    # lewat context, karena sekarang diambil browser sendiri lewat fetch() ke get_education_json
    school_query = request.GET.get("school", "").strip()

    context = {
        'name': 'Nasywa Namira Suhendro',
        'school_query': school_query, # biar kata kunci dari ?school= tetap terisi di kolom search
        'form': EducationForm(), # form kosong, cuma buat di-render di dalam modal

    }
    return render(request, "education.html", context)

def get_education_json(request):
    # Endpoint JSON yang dipanggil fetch() dari education.html (bisa diakses semua peran, termasuk pengunjung)
    # mengambil data dalam format JSON
    school_query = request.GET.get("school", "").strip()
    # prefetch_related('starred_by') supaya data star diambil sekaligus, bukan 1 query per education (N+1)
    educations = Education.objects.prefetch_related('starred_by').all()

    # search AJAX: filter berdasarkan nama institusi, icontains = nggak peduli huruf besar/kecil
    if school_query:
        educations = educations.filter(school__icontains=school_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logic Star
    data = []
    for education in educations:
        starred_users = education.starred_by.all()
        # pengunjung yang belum login otomatis dianggap belum nge-star
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(education.id), # dijadiin string biar aman dipakai di JS (buat bikin URL star & delete)
            "fields": {
                "school": education.school,
                "degree": education.degree,
                "start_year": education.start_year,
                "end_year": education.end_year,
                "description": education.description,
                "logo": education.logo or "",  # logo boleh kosong (null), diganti "" biar JS nggak nampilin "null"
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        # safe=False karena yang dikirim berupa list, bukan dict
    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def create_education(request): # untuk add education
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save() # simpan value yg dimasukkan pengguna
        messages.success(request, "Riwayat pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Nami",
        "form": form,
        "action_title":"Add New Education",
        "button_text": "Tambah Education",
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def edit_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    # update data menggunakan form
    education = get_object_or_404(Education, pk=id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan berhasil diperbarui!")
        return redirect("main:show_education")

    context = {
        "name": "Nasywa Namira Suhendro",
        "form": form,
        "action_title": "Edit Education",
        "button_text": "Simpan Perubahan",
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def delete_education(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    # delete data
    education = get_object_or_404(Education, pk=id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None) # digunakan untuk mentrigger class

    if request.method == "POST" and form.is_valid():
        form.save() # digunakan untuk menyimpan value yang telah dimasukkan pengguna lewat form ke database.
        messages.success(request, "Proyek baru berhasil ditambahkan!") # digunakan untuk mengirim pesan ke client untuk dapat ditampilkan.
        return redirect("main:show_projects") # akan berjalan setelah form berhasil disimpan, halaman website akan diarahkan ke halaman projects yang bisa dilihat.

    context = {
        "name": "Nami",
        "form": form,
    }
    return render(request, "projects_form.html", context)
# @login_required memeriksa request.user sebelum isi fungsi dijalankan. Kalau pengunjung belum login, Django langsung mengalihkannya ke alamat pada login_url tanpa pernah menyentuh kode di dalam fungsi.
# Nilai login_url harus sama persis dengan path yang kamu daftarkan di main/urls.py. Kalau kamu menulis /login tanpa garis miring penutup, halamannya tetap ketemu lewat APPEND_SLASH, tetapi browser harus melewati satu pengalihan tambahan lebih dulu.

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nami",
        "title_query": title_query,
        "is_editor": request.user.is_authenticated and is_editor(request.user),
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    # mengubah setiap objek Project menjadi sebuah dictionary
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False # memeriksa apakah request.user ada di dalam daftar akun yang memberi star pada proyek tersebut (is_starred) dan menghitung total star
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False) # mengirimkan data utuh ini ke browser.

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Nami",
        "form": form,
    }
    return render(request, "register.html", context)
# Pada permintaan GET, form kosong ditampilkan. Pada POST, form menerima data dari request.POST.
# UserCreationForm menyediakan username, password1, dan password2. is_valid() memeriksa username, kecocokan kedua password, dan aturan password dari konfigurasi proyek.
# form.save() membuat akun dengan password yang sudah di-hash. Registrasi tidak langsung membuat pengguna login; pengguna diarahkan ke halaman login.
# Jika validasi gagal, form yang sama dirender kembali agar pesan kesalahannya bisa dibaca.
# messages.success() menyiapkan pesan untuk ditampilkan setelah pengalihan. Nilai name tetap nama pemilik portofolio

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main") # fungsi redirect() menghasilkan objek HttpResponseRedirect.
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Nami",
        "form": form,
    }
    return render(request, "login.html", context)
# AuthenticationForm menerima request sebagai argumen pertama dan data input melalui argumen data. is_valid() memeriksa kredensial menggunakan sistem autentikasi Django.
# Setelah validasi berhasil, form.get_user() memberikan objek pengguna yang sudah terautentikasi. Kita tidak perlu memanggil authenticate() lagi.
# login(request, user) mencatat pengguna dalam session. Pada permintaan berikutnya, Django dapat mengenali pengguna lewat request.user.
# Fungsi view diberi nama login_user agar tidak menimpa fungsi login yang kita impor.
# Implementasi ini selalu mengarahkan pengguna ke halaman profil setelah login. Parameter next belum diproses.

def logout_user(request): 
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response
# menghapus data session saat ini, lalu pengguna diarahkan ke halaman profil. 
# Akunnya tetap ada di database dan dapat digunakan untuk login kembali.
# response.delete_cookie('last_login') menyisipkan header HTTP pada respons yang menginstruksikan browser klien untuk segera menghapus cookie last_login dari penyimpanannya.
# Ketika kamu diarahkan kembali ke halaman utama setelah logout, request.COOKIES.get('last_login') tidak lagi menemukan cookie tersebut, sehingga teks default akan ditampilkan.


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")
# Fungsi ini memakai @login_required tanpa pemeriksaan is_superuser. Pengguna terdaftar mana pun boleh memberi star; yang tidak boleh hanya pengunjung yang belum punya akun.
# project.starred_by.add(...) dan .remove(...) menambah dan menghapus baris di tabel penghubung. Memanggil .add() dua kali untuk pengguna yang sama tidak membuat data ganda.
# Pemeriksaan request.method == "POST" memastikan data hanya berubah lewat pengiriman form, bukan karena alamatnya kebetulan dibuka di browser.

@login_required(login_url="/login/")
def toggle_star_education(request, id):
    education = get_object_or_404(Education, pk=id)

    if request.method == "POST":
        # klo akun ini udh pernah ngasih star, batalkan star
        # kalo belom, tambahkan star
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)
    return redirect("main:show_education")

@login_required(login_url="/login/")
def update_project(request, project_id):
    # Editor boleh mengubah data project tp ga boleh add/delete
    if not (request.user.is_superuser or is_editor(request.user)):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Nami",
        "form": form,
        "project": project,
        "action_title": "Edit Project",
        "button_text": "Simpan Perubahan",
    }
    return render(request, "projects_form.html", context)


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
# @require_POST membuat view ini hanya menerima metode POST. Permintaan dengan metode lain langsung dibalas 405 Method Not Allowed.
# Pemeriksaan is_superuser tetap wajib, sama seperti pada create_project di Tutorial 04. Menyembunyikan tombol di template tidak mencegah siapa pun memanggil endpoint ini langsung dengan fetch.
# Di sini kita tidak memakai @login_required. Dekorator itu membalas pengunjung yang belum login dengan redirect ke halaman login, dan fetch akan mengikuti redirect tersebut lalu menerima halaman HTML login dengan status 200 sehingga JavaScript kita tidak bisa mengenali kegagalannya. Karena AnonymousUser juga memiliki is_superuser bernilai False, satu pemeriksaan di atas sudah menolak baik pengunjung yang belum login maupun pengguna biasa dengan respons JSON 403 yang mudah dibaca JavaScript.
# Kita memakai kembali ProjectForm alih-alih membuat objek Project langsung dari request.POST. Dengan begitu, semua validasi yang sudah ada (field wajib, panjang maksimum, format URL) tetap berlaku untuk permintaan AJAX.
# Status 201 Created menandakan data baru berhasil dibuat, sedangkan 400 Bad Request dikirim bersama pesan kesalahan tiap field dari form.errors.get_json_data(), misalnya {"title": [{"message": "This field is required.", "code": "required"}]}.


@require_POST # membuat view ini hanya menerima metode POST. Permintaan dengan metode lain langsung dibalas 405 Method Not Allowed.
def create_education_ajax(request):
    # pengecekan ini sudah nolak pengunjung & user biasa dengan JSON 403.
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pendidikan."},
            status=403,
        )
    
    # pakai EducationForm lagi biar validasi (field wajib, panjang maks) + strip_tags tetap berlaku
    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Pendidikan berhasil ditambahkan.", "pk": str(education.id)},
            status=201,# 201 Created = data baru berhasil dibuat
        )
        
    # 400 Bad Request + pesan error per field, nanti ditampilin JS lewat toast
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)