from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
import projects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)