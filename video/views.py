from django.shortcuts import render, redirect, reverse
from .models import Video
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('video:homevideos')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email = email)
        if usuarios:
            return reverse('video:login')
        else:
            return reverse('video:criarconta')

class HomeVideos(LoginRequiredMixin, ListView):
    template_name = 'homevideos.html'
    model = Video

class DetalhesVideo(LoginRequiredMixin, DetailView):
    template_name = 'detalhesvideo.html'
    model = Video

    def get(self, request, *args, **kwargs):
        video = self.get_object()
        video.visualizacoes += 1
        video.save()
        usuario = request.user
        usuario.videos_vistos.add(video)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetalhesVideo, self).get_context_data(**kwargs)
        videos_relacionados = self.model.objects.filter(categoria = self.get_object().categoria)[0:4]
        context['videos_relacionados'] = videos_relacionados
        return context

class PesquisaVideo(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Video

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains = termo_pesquisa)
            return object_list
        else:
            return None

class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('video:homevideos')