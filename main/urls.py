from django.urls import path

from main.views import show_main, show_experience, show_education, create_project, show_projects, get_projects_json, delete_project

app_name = "main" # memberikan namespace pada URL milik aplikasi main.

urlpatterns = [
    path("", show_main, name="show_main"), # profile
    path("experience/", show_experience, name="show_experience"), # experience
    path("education/", show_education, name="show_education"), # education
    path("projects/add/", create_project, name="create_project"), #project
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
]

# Pola URL "" berarti halaman utama aplikasi tanpa tambahan path.
# Pola URL "experience/" mengarahkan permintaan /experience/ ke show_experience.
# name="show_main" dan name="show_experience" memberi nama pada rute agar dapat dirujuk 
# melalui navigasi dan test tanpa menulis URL secara langsung.
