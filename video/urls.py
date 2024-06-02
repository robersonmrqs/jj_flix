from django.urls import path, reverse_lazy
from .views import HomePage, HomeVideos, DetalhesVideo
from django.contrib.auth import views as auth_view

app_name = 'video'

urlpatterns = [path('', HomePage.as_view(), name = 'homepage'),
               path('videos/', HomeVideos.as_view(), name = 'homevideos'),
               path('videos/<int:pk>', DetalhesVideo.as_view(), name = 'detalhesvideo'),]