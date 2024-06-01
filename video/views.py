from django.shortcuts import render, redirect, reverse
from .models import Video, Usuario
from .forms import CriaContaForm, FormHomePage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(FormView):
    template_name = 'homepage.html'
    form_class = FormHomePage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('video:homevideos')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('video:login')
        else:
            return reverse('video:criarconta')


class HomeVideos(LoginRequiredMixin, ListView):
    template_name = 'homevideos.html'
    model = Video