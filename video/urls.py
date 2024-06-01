from django.urls import path, reverse_lazy
from .views import HomePage, HomeVideos, DetalhesVideo, PesquisaVideo, EditarPerfil, CriarConta
from django.contrib.auth import views as auth_view

app_name = 'video'

urlpatterns = [
    path('', HomePage.as_view(), name = 'homepage'),
    path('videos/', HomeVideos.as_view(), name = 'homevideos'),
    path('videos/<int:pk>', DetalhesVideo.as_view(), name = 'detalhesvideo'),
    path('pesquisa/', PesquisaVideo.as_view(), name = 'pesquisavideo'),
    path('login/', auth_view.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('editarperfil/<int:pk>', EditarPerfil.as_view(), name = 'editarperfil'),
    path('criarconta/', CriarConta.as_view(), name = 'criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name = 'editarperfil.html', success_url = reverse_lazy('video:homevideos')), name = 'mudarsenha'),
]