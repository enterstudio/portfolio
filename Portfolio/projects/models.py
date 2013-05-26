from django.db import models
from tinymce.models import HTMLField
import datetime
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    summary = HTMLField()
    description = models.TextField()
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(db_index=True)
    github_link = models.URLField(max_length=100, blank=True)
    live_link = models.URLField(max_length=100, blank=True)
    published = models.BooleanField()
    
    # Return readable string of 'title'
    def __unicode__(self): 
        return self.title
    
class Post(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    content = HTMLField()
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(db_index=True)
    published = models.BooleanField()
    
    # Return readable string of 'title'
    def __unicode__(self):
        return self.title