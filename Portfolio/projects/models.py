from django.db import models
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
import datetime
from django.utils import timezone

#Category for use as FK for Posts or Projects
class Category(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True)

    # Return readable string of 'title'
    def __unicode__(self):
        return self.title

#tags to identify languages and frameworks in a project    
class Tag(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(blank=True) 

    # Return readable string of 'title'
    def __unicode__(self):
        return self.title

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    image = FileBrowseField("Image", max_length=200, directory="uploads/", extensions=[".jpg",".jpeg",".png"], blank=True, null=True)
    summary = HTMLField()
    description = HTMLField()
    created = models.DateTimeField(db_index=True)
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
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    content = HTMLField()
    created = models.DateTimeField(db_index=True)
    updated = models.DateTimeField(db_index=True)
    published = models.BooleanField()
    
    # Return readable string of 'title'
    def __unicode__(self):
        return self.title
    