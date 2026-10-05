from django.urls import path

from main.views import (create_education_ajax, create_project_ajax, show_main, 
                        show_experience, 
                        show_education, 
                        get_education_json,
                        create_education,
                        edit_education,
                        delete_education, 
                        create_project, 
                        show_projects, 
                        get_projects_json, 
                        delete_project,
                        register,
                        login_user,
                        logout_user, toggle_star, toggle_star_education, update_project)

app_name = "main" # memberikan namespace pada URL milik aplikasi main.

urlpatterns = [
    # Main & Experience
    path("", show_main, name="show_main"), # profile
    path("experience/", show_experience, name="show_experience"), # experience

    # Education
    path("education/", show_education, name="show_education"), # education
    path("education/create/", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"), # endpoint JSON buat fetch()
    path('education/edit/<int:id>/', edit_education, name='edit_education'),
    path('education/delete/<int:id>/', delete_education, name='delete_education'),

    # Projects
    path("projects/add/", create_project, name="create_project"), #project
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("projects/<uuid:project_id>/edit/", update_project, name="update_project"),

    # Register
    path("register/", register, name="register"),

    # Login
    path("login/", login_user, name="login"), # Nama URL main:login menunjuk ke view login_user

    # Logout
    path("logout/", logout_user, name="logout"), # main:logout menunjuk ke logout_user

    # Toggle star
    path(
        "projects/<uuid:project_id>/star/",
        toggle_star,
        name="toggle_star", # toggle star di Project field
    ),
    path("education/<int:id>/star/", toggle_star_education, name="toggle_star_education"), # toggle star di Education field
    # toggle star pakai <int:id>, bukan <uuid:id>, karena model Education pakai ID integer

    # project AJAX
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),

    # education AJAX: endpoint POST yang dipanggil dari modal
    path("education/add-ajax/", create_education_ajax, name="create_education_ajax"),
]

# Pola URL "" berarti halaman utama aplikasi tanpa tambahan path.
# Pola URL "experience/" mengarahkan permintaan /experience/ ke show_experience.
# name="show_main" dan name="show_experience" memberi nama pada rute agar dapat dirujuk 
# melalui navigasi dan test tanpa menulis URL secara langsung.
