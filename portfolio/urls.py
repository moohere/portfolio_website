from django.contrib import admin
from django.urls import path, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import projects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]