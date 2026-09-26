import uuid
from django.contrib.auth.models import User
from django.db import models

class Experience(models.Model): # page Experience
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    main_image = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model): # page Education
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_year = models.CharField(max_length=50)
    end_year = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    logo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.school

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)

    starred_by = models.ManyToManyField(
        User, related_name="stared_projects", blank=True
    )

# ManyToManyField dipakai karena satu proyek bisa di-star banyak pengguna, dan satu pengguna bisa mem-star banyak proyek. Django membuat tabel penghubungnya sendiri di belakang layar.
# related_name="starred_projects" menentukan nama jalur sebaliknya. Dari objek User, daftar proyek yang ia star bisa diambil lewat user.starred_projects.all().
# blank=True membuat field ini boleh kosong saat sebuah proyek baru dibuat.

    def __str__(self):
        return self.title