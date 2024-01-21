from django.http import HttpResponse
from django.shortcuts import render, redirect

from.forms import TodoForm
from.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView


# Create your views here.

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POSTget('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,id):
    if request.method=='POST':
        task=Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})

