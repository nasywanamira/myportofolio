from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project, Education

class ProjectForm(ModelForm):
    class Meta:
        model = Project # model digunakan untuk menentukan model Django yang menjadi sumber data dan struktur dari ModelForm. Field pada form akan dibuat berdasarkan field yang terdapat pada model tersebut.
        fields = [ # digunakan untuk menentukan field model yang ingin ditampilkan pada form. 
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = { # digunakan untuk mengatur tampilan dan jenis elemen HTML yang digunakan oleh setiap field pada form
            "title": TextInput( # digunakan untuk field teks satu baris
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea( # digunakan untuk field deskripsi yang membutuhkan area teks lebih besar
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput( # digunakan untuk field yang berisi URL
                attrs={
                    "placeholder": "https://github.com/kakBurhan/burhanquestv4",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school",
            "degree",
            "start_year",
            "end_year",
            "description",
            "logo",
        ]
        labels = {
            "school": "Nama sekolah /  universitas",
            "degree": "Jurusan",
            "start_year": "Tahun masuk",
            "end_year": "Tahun selesai / lulus",
            "description": "Deskripsi",
            "logo": "URL Logo / Gambar",
        }
        widgets ={
            "school": TextInput( # digunakan untuk field teks satu baris
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }   
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "S1 Sistem Informasi",
                }
            ),
            "start_year": TextInput(
                attrs={
                    "placeholder": "2025"
                }
            ),
            "end_year": TextInput(
                attrs={
                    "placeholder": "2029"
                }
            ),
            "description": Textarea( # digunakan untuk field deskripsi yang membutuhkan area teks lebih besar
                attrs={
                    "placeholder": "Activities, Achievements, etc.",
                    "rows": 4
                }
            ),
            "logo": TextInput(
                attrs={
                    "placeholder": "https://... (opsional)"
                }
            ),
        }