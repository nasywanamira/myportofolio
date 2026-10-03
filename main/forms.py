from django.forms import ModelForm, TextInput, Textarea, URLInput, ValidationError

from main.models import Project, Education
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

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
                    "placeholder": "Nama institusi",
                    "maxlength": 255,
                }   
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "Jurusan yang ditempuh",
                }
            ),
            "start_year": TextInput(
                attrs={
                    "placeholder": "Tahun masuk"
                }
            ),
            "end_year": TextInput(
                attrs={
                    "placeholder": "Tahun lulus"
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
    def clean_school(self):
        school = strip_tags(self.cleaned_data["school"]).strip()
        if not school:
            raise ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return school

    def clean_degree(self):
        degree = strip_tags(self.cleaned_data["degree"]).strip()
        if not degree:
            raise ValidationError("Gelar/jurusan tidak boleh hanya berisi tag HTML.")
        return degree

    def clean_start_year(self):
        return strip_tags(self.cleaned_data["start_year"]).strip()

    def clean_end_year(self):
        # end_year opsional (blank=True, null=True), jadi bisa kosong / None
        end_year = self.cleaned_data.get("end_year")
        return strip_tags(end_year).strip() if end_year else end_year

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

    def clean_logo(self):
        # logo opsional; hanya izinkan URL http(s) atau path relatif
        logo = self.cleaned_data.get("logo")
        if not logo:
            return logo
        logo = strip_tags(logo).strip()
        if logo and not logo.lower().startswith(("http://", "https://", "/")):
            raise ValidationError("URL logo harus diawali http://, https://, atau /.")
        return logo