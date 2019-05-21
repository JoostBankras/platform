from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vacature, Reaction
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  

def add_reaction(request, pk=None):
    user = request.user
    if pk:
        vacature = Vacature.objects.get(id=pk)
        vacature.add_reaction(user)
    return redirect("vacatures")

class VacaturesListView(ListView):
    model = Vacature
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class VacatureCreateView(LoginRequiredMixin, CreateView):
    model = Vacature
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class VacatureDetailView(DetailView):
    model = Vacature

class VacatureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vacature
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        vacature = self.get_object()
        if self.request.user == vacature.author:
            return True
        return False

class VacatureDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vacature
    success_url = '/'

    def test_func(self):
        vacature = self.get_object()
        if self.request.user == vacature.author:
            return True
        return False