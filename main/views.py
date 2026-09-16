from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Education
from main.forms import ProjectForm


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
    education_list = Education.objects.all()
    context = {
        'name': 'Nasywa Namira Suhendro',
        'education_list': education_list
    }
    return render(request, "education.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None) # digunakan untuk mentrigger class

    if request.method == "POST" and form.is_valid():
        form.save() # digunakan untuk menyimpan value yang telah dimasukkan pengguna lewat form ke database.
        messages.success(request, "Proyek baru berhasil ditambahkan!") # digunakan untuk mengirim pesan ke client untuk dapat ditampilkan.
        return redirect("main:show_projects") # akan berjalan setelah form berhasil disimpan, halaman website akan diarahkan ke halaman projects yang bisa dilihat.

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)