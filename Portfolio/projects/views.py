# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from projects.models import Project, Post

def index(request):
    project_updates = Project.objects.filter(published = 'true').order_by('-updated')[:5]
    post_created = Post.objects.filter(published = 'true').order_by('-created')[:5]
    context = {'project_updates': project_updates, 'post_created': post_created}
    return render(request, 'home.html', context)

def projects(request):
    project_list = Project.objects.filter(published = 'true').order_by('-created')
    post_created = Post.objects.filter(published = 'true').order_by('-updated')[:5]
    project_updates = Project.objects.filter(published = 'true').order_by('-updated')[:5]
    context = {'project_list': project_list, 'project_updates': project_updates, 'post_created': post_created }
    # render is a shortcut for using context.  pass request, template URL, and context Var
    #returns an HttpResponse object
    return render(request, 'projects/index.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    posts_list = Post.objects.filter(project = project_id).order_by('created')
    return render(request, 'projects/detail.html', {'project': project, 'posts_list': posts_list})

def posts(request):
    posts_list = Post.objects.filter(published = 'true').order_by('-created')
    post_created = Post.objects.filter(published = 'true').order_by('-updated')[:5]
    project_updates = Project.objects.filter(published = 'true').order_by('-updated')[:5]
    context = {'posts_list': posts_list, 'project_updates': project_updates, 'post_created': post_created}
    # render is a shortcut for using context.  pass request, template URL, and context Var
    return render(request, 'posts/index.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    project_item = get_object_or_404(Project, pk = post.project_id)
    posts_list = Post.objects.filter(project = post.project).order_by('created')
    return render(request, 'posts/detail.html', {'post': post, 'posts_list': posts_list, 'project': project_item})

def resume(request):
    return HttpResponse("Resume page")
