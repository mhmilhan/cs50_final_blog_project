from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from en_learning import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('account.urls')),
    path('blog/', include('blog.urls')),

    # External package
    path("__reload__/", include("django_browser_reload.urls")),
    path('ckeditor/', include('django_ckeditor_5.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def custom_404(request, exception):
    return render(request, '404.html', status=404)


handler404 = custom_404
