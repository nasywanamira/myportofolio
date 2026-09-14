from django.shortcuts import render

from main.models import Experience, Education


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