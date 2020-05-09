from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import Project
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import main
from .forms import ProjectForm

def home(request):
    return render(request, 'main/home.html')

def random(request):
    return render(request, 'main/signup.html')
    
class ProjectList(ListView):
    model = Project
    template_name = 'main/results.html'
    queryset = Project.objects.all()

    def get(self, request):
        ''' Get a list of all codes currently in the database.'''
        projects = self.queryset.filter(is_visible=True)
        return render(request, self.template_name, {
            'projects': projects
        })


class ProjectDetail(DetailView):
    model = Project
    template_name = 'main/details.html'

    def get(self, request, slug):
        project = get_object_or_404(Project, slug__iexact=self.kwargs['slug'])
        code = self.get_queryset().get(slug__iexact=slug)
        context = {
            'project': project
        }
        return render(request, self.template_name, context)

class ProjectCreate(UserPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'main/create.html'
    queryset = Project.objects.all()

    def form_valid(self, form):
        '''Initializes the post_by field based on who submitted the form.'''
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def get(self, request):
        '''displaying'''
        context = {'form': ProjectForm()}

        return render(request, self.template_name, context)

    def test_func(self):
        # project = self.get_object()
        user = self.request.user
        return (user.is_authenticated is True)

class ProjectUpdate(UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'main/update.html'
    queryset = Project.objects.all()

    def test_func(self):
        '''Ensures the user adding the Code is an officer.'''
        code = self.get_object()
        user = self.request.user
        return (user.is_authenticated is True)

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'main/delete.html'
    success_url = reverse_lazy('projects:home')
    success_message = "project successfully archived"
    queryset = Project.objects.all()

    def test_func(self):
        code = self.get_object()
        user = self.request.user
        return (user.is_authenticated is True)

    def get(self, request, slug):
        '''displaying'''
        code = self.get_queryset().get(slug=slug)

        context = {
            'project': project
        }
        return render(request, self.template_name, context)

    def delete(self, request, *args, **kwargs):
        '''hiding project'''
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_visible = False
        self.object.save()
        return HttpResponseRedirect(success_url)