from django.conf import settings
from django.contrib import admin
from django.urls import path

from {{cookiecutter.module_name}} import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
]

handler404 = "{{cookiecutter.module_name}}.views.page_not_found"
handler500 = "{{cookiecutter.module_name}}.views.server_error"

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
