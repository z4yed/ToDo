from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDo
from .forms import ToDoForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    return render(request, 'app1/welcome.html')

@login_required
def homeView(request):
    todos = ToDo.objects.filter(time_completed__isnull=True, user=request.user)
    context = {'todos': todos}
    return render(request, 'app1/home.html', context)

@login_required
def detailView(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    context = {'todo': obj}
    return render(request, 'app1/details.html', context)
@login_required
def createView(request):
    form = ToDoForm()
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('home-view')

    context = {
        'form': form
    }
    return render(request, 'app1/create.html', context)

@login_required
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

@login_required
def deleteView(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('home-view')

    context = {
        'obj':obj,
    }
    return render(request, 'app1/delete.html', context)

@login_required
def completedView(request):
    obj = ToDo.objects.filter(time_completed__isnull=False)
    context = {
    'obj': obj
    }
    return render(request, 'app1/completed.html', context)

@login_required
def markComplete(request, pk):
    obj = get_object_or_404(ToDo, pk=pk)
    if request.method == "POST":
        obj.is_completed = True
        obj.time_completed = timezone.now()
        obj.save()
        return redirect('completed-view')
