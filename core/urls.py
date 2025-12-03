from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from core import settings

urlpatterns = [
    path('', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path ('projects/', include('projects.urls')),
    path ('tasks/', include('tasks.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
