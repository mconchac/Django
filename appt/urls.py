"""appt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from appt import views as local_views

# Módulo hoteles
from hoteles import views as hoteles_view

def test(request):
    return HttpResponse('Estoy en NivelPro')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
    path('test1/', local_views.test1),
    path('test2/', local_views.test2),
    path('hoteles', hoteles_view.lista_hoteles),

]
