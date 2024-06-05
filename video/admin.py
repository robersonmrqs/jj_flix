from django.contrib import admin
from .models import Video, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(('Histórico', {'fields': ('videos_vistos',)}))
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Video)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)