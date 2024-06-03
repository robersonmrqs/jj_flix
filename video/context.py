from .models import Video

def lista_videos_recentes(request):
    lista_videos = Video.objects.all().order_by('-data_criacao')[0:8]
    if lista_videos:
        video_destaque = lista_videos[0]
    else:
        video_destaque = None
    return {'lista_videos_recentes': lista_videos, 'video_destaque': video_destaque}

def lista_videos_emalta(request):
    lista_videos = Video.objects.all().order_by('-visualizacoes')[0:8]
    return {'lista_videos_emalta': lista_videos}