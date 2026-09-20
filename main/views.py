from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education, Project
from main.forms import ProjectForm, EducationForm


def show_main(request): # untuk main page aka Profile
    context = {
        "name": "Nasywa Namira Suhendro",
        "npm": "2506532196",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Driven by curiosity and learning by doing. I show up, embrace the challenge (even if it's scary), "
            "and figure it out as I go ;). especially in business analysis and partnerships!!"
        ),
    }
    return render(request, "index.html", context)


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

def edit_education(request):
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

def create_project(request):
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

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")