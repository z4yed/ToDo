from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDo
from .forms import ToDoForm
from django.utils import timezone
from django.db.models import Q
# Create your views here.

def homeView(request):
    todos = ToDo.objects.filter(time_completed__isnull=True)
    context = {'todos': todos}
    return render(request, 'app1/home.html', context)

def detailView(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    context = {'todo': obj}
    return render(request, 'app1/details.html', context)

def createView(request):
    form = ToDoForm()
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-view')

    context = {
        'form': form
    }
    return render(request, 'app1/create.html', context)

def editView(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    form = ToDoForm(instance = obj)
    if request.method == "POST":
        form = ToDoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    context = {
        'obj': obj,
        'form':form
    }
    return render(request, 'app1/edit.html', context)


def deleteView(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('home-view')

    context = {
        'obj':obj,
    }
    return render(request, 'app1/delete.html', context)

def completedView(request):
    obj = ToDo.objects.filter(time_completed__isnull=False)
    context = {
    'obj': obj
    }
    return render(request, 'app1/completed.html', context)

def markComplete(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        obj.is_completed = True
        obj.time_completed = timezone.now()
        obj.save()
        return redirect('completed-view')
