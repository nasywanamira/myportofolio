from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
]

# Fungsi include() meneruskan permintaan dengan awalan "" dari level proyek ke main/urls.py. 
# Di sana, Django memilih view berdasarkan sisa path. 
# Rute langsung ke landing_page dari Tutorial 1 digantikan oleh include("main.urls"), 
# sehingga halaman profil sekarang ditangani oleh show_main.