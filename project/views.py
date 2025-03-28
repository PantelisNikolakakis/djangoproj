from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Project

# Create your views here.

@login_required
def projects(request):
    projects = Project.objects.filter(created_by =  request.user)
    paginator = Paginator(projects, 3)
    page = request.GET.get('page', 1)

    try:
        projects_to_show = paginator.page(page)
    except PageNotAnInteger:
        projects_to_show = paginator.page(1)
    except EmptyPage:
        projects_to_show = paginator.page(paginator.num_pages)

    page_list = projects_to_show.paginator.page_range
    print(page_list)

    return render(request, 'project/projects.html', {
        'projects': projects_to_show,   # Project.objects.filter(created_by =  request.user)[starting_number:ending_number]# projects
        'page_list': page_list
    })

@login_required
def project(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk = pk)

    return render(request, 'project/project.html',{
        'project': project
    })

@login_required
def add(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        
        if name and description: 
            project = Project.objects.create(name = name, description = description, created_by = request.user)

            return redirect('/projects/')
        else: 
            print('Not valid')

    return render(request, 'project/add.html')

@login_required
def edit(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk = pk)

    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name and description:
            project.name = name
            project.description = description
            project.save()
            return redirect('/projects/')

    return render(request, 'project/edit.html',{
        'project': project
    })

@login_required
def delete(request, pk):
    project = Project.objects.filter(created_by = request.user).get(pk = pk)
    project.delete()
    return redirect('/projects/')


def paginate(request):
    if request.method == "POST":
        page = request.POST.get("page", 1)  # Get page number from POST data
        print(f"Pageeeeeeeeeeee: {page}")
        projects = Project.objects.filter(created_by=request.user)
        paginator = Paginator(projects, 3)
        projects_to_show = paginator.get_page(page)

        try:
            projects_to_show = paginator.page(page)
        except PageNotAnInteger:
            projects_to_show = paginator.page(1)
        except EmptyPage:
            projects_to_show = paginator.page(paginator.num_pages)

        page_list = projects_to_show.paginator.page_range
        print(page_list)

        return render(request, "project/project_list.html", {
            "projects": projects_to_show,
            "page_list": page_list
        })

    return JsonResponse({"error": "Invalid request"}, status=400)