from django.shortcuts import render

from main.models import Experience


def show_main(request):
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


def show_experience(request):
    context = {
        "name": "Nasywa Namira Suhendro",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)