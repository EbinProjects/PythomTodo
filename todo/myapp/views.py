import django.urls
from django.shortcuts import render, redirect
from .models import TODO1
from .forms import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


# Create your views here.
class TodoListView(ListView):
    model = TODO1
    template_name = 'home1.html'
    context_object_name = 'products'


class Details(DetailView):
    model = TODO1
    template_name = 'details.html'
    context_object_name = 'i'


class Deleted(DeleteView):
    model = TODO1
    template_name = 'delete.html'
    success_url = django.urls.reverse_lazy('cbvHome')


class TaskUpdate(UpdateView):
    model = TODO1
    template_name = 'update.html'
    context_object_name = 'i'
    fields = ('name', 'priority', 'datefield')

    def get_success_url(self):
        # / return django.urls.reverse_lazy('cbvHome', kwargs={'pk': self.object.id})
        return django.urls.reverse_lazy('cbvHome')


def Todo(request):
    products = TODO1.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = TODO1(name=name, priority=priority, datefield=date)
        task.save()
    return render(request, "home.html", {'products': products})


def update(request, tackid):
    task = TODO1.objects.get(id=tackid)
    f = TodoForms(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, "edit.html", {'f': f, 'task': task})


def Delete(request, tackid):
    if request.method == 'POST':
        item = TODO1.objects.get(id=tackid)
        item.delete()
        return redirect('/')
    return render(request, "delete.html")
