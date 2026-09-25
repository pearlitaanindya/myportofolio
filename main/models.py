import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    organization = models.TextField(default="", blank=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_experience", blank=True
    )
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

# model education
class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # id
    degree = models.CharField(max_length=255) # gelar pada item education
    gpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True) # gpa/nilai
    school = models.TextField() #  institusi 
    thumbnail = models.URLField(blank=True, null=True) # logo
    started_at = models.DateField() # field tanggal mulai
    ended_at = models.DateField(blank=True, null=True) # field tanggal selesai
    starred_by = models.ManyToManyField(
        User, related_name="starred_education", blank=True
    )

    def __str__(self):
            return self.degree
        
    @property
    def is_ongoing(self):
        return self.ended_at is None