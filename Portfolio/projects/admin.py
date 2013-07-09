from django.contrib import admin
from projects.models import Project, Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'tags', 'published', 'slug', 'project', 'created', 'updated', 'content' ]

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'category', 'tags', 'published', 'slug', 'image', 'created', 'updated', 'summary', 'description', 'github_link', 'live_link' ]

class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'description']

class TagAdmin(admin.ModelAdmin):
    fields = ['title', 'description']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
