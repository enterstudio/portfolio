from django.contrib import admin
from adminfiles.admin import FilePickerAdmin
from projects.models import Project
from projects.models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'published', 'slug', 'project', 'updated', 'content' ]

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'published', 'slug', 'updated', 'summary', 'description', 'github_link', 'live_link' ]
    adminfiles_fields = ('description',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)

