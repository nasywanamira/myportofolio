import datetime
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm


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
    # mengambil data dari response JSON
    json_response = get_education_json(request)
    educations = serializers.deserialize("json", json_response.content.decode("utf-8"))
    education_list= [edu.object for edu in educations]

    context = {
        'name': 'Nasywa Namira Suhendro',
        'education_list': education_list
    }
    return render(request, "education.html", context)

def get_education_json(request):
    # mengambil data dalam format JSON
    educations = Education.objects.all()
    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def create_education(request): # untuk add education
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

def edit_education(request, id):
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

def delete_education(request, id):
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
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nami",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

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