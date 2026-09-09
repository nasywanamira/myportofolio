from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")


# Semua method yang namanya diawali test_ akan dijalankan otomatis oleh Django. Method setUp() dijalankan sebelum setiap test sehingga tiap test memperoleh data awal yang bersih.

# Enam test tersebut memeriksa hal yang berbeda:

# Halaman profil dapat diakses, memakai index.html, tidak menampilkan kartu pengalaman, dan memiliki tautan ke halaman Experience.
# URL yang tidak terdaftar menghasilkan status 404 Not Found.
# Model menyimpan nilai dan menghitung is_ongoing dengan benar.
# Halaman Experience memakai experience.html, menampilkan data model beserta kategori dan statusnya, serta memiliki tautan kembali ke profil.
# Halaman Experience menampilkan pesan yang sesuai ketika belum ada data.
# Pengalaman dengan ended_at terisi menampilkan status Selesai.
# reverse() mencari URL berdasarkan app_name dan name yang telah dibuat di main/urls.py, sama seperti tag {% url %} pada template. Cara ini membuat tautan dan test tetap mengikuti rute jika path berubah. 
# assertNotContains memastikan teks tertentu tidak muncul dalam respons, sedangkan timezone.now() memberikan waktu saat ini untuk mengisi ended_at pada test pengalaman yang sudah selesai.