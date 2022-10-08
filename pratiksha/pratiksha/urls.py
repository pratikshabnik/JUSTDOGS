from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import urls
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('',include('JUSTDOGS.urls'),name="home"),
    path('register/', views.Register.as_view(),name="register")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
