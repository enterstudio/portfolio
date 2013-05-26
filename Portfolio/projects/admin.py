from django.contrib import admin
from projects.models import Project
from projects.models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'published', 'slug', 'project', 'updated', 'content' ]

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'published', 'slug', 'image', 'updated', 'summary', 'description', 'github_link', 'live_link' ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)

