from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {
        'tasks': tasks,
        'form':form,
    }

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request=request, template_name='index.html', context=context)

def update_task(request, pk):
    task = Task.objects.get(id = pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = { 
        'form':form,
    }
    
    return render(request=request, template_name='update.html', context=context)


def delete_task(request, pk):
    item = Task.objects.get(id = pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    context = {
        'item':item,
    }

    return render(request=request, template_name='delete.html', context=context)