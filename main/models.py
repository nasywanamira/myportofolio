import uuid
from django.db import models

class Experience(models.Model):
    
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

class Education(models.Model):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_year = models.CharField(max_length=50)
    end_year = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    logo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.school
