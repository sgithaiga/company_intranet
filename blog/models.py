from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # returns us to the post-detail view. can also set this to blog-home
        return reverse('post-detail', kwargs={'pk': self.pk})

class Vacancies (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # returns us to the post-detail view. can also set this to blog-home
        return reverse('blog-home', kwargs={'pk': self.pk})

class Applications(models.Model):
    name = models.CharField(max_length=200)
    Pf_no = models.CharField(max_length=200)
    job_applied_for = models.CharField(max_length=200)
    cover_letter = models.TextField()
    cv = models.FileField(upload_to='documents/', null=True)
    certs = models.FileField(upload_to='documents/', null=True)
    date_applied = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class HrDocs(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/', null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

