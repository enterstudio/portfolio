# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from projects.models import Project, Post

def index(request):
    context = {}
    return render(request, 'home.html', context)

def projects(request):
    project_list = Project.objects.all().order_by('created')
    context = {'project_list': project_list}
    # render is a shortcut for using context.  pass request, template URL, and context Var
    #returns an HttpResponse object
    return render(request, 'projects/index.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    return render(request, 'projects/detail.html', {'project': project})

def posts(request):
    posts_list = Post.objects.all().order_by('created')
    context = {'posts_list': posts_list}
    # render is a shortcut for using context.  pass request, template URL, and context Var
    return render(request, 'posts/index.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'posts/detail.html', {'post': post})

def resume(request):
    return HttpResponse("Resume page")
