"""
URL configuration for portafolio_pagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from mainapp import views
from photoVlogApp import views as vistasPhoto
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.index, name='index'),
    path('', views.index, name = 'inicio'),
    path('about/', views.about, name ='acerca'),
    path('contact/', views.contacto, name= 'contacto'),
    path('imagen<int:id>/',  vistasPhoto.publicacionDetalle, name="imagen"),
    path('imagenes/' , vistasPhoto.publicaciones, name='imagenes'),
    path('experiencia/' ,views.experiencia, name = 'experiencia'),
    path('categorias', vistasPhoto.returnThumbCategorias, name ="categorias"),
    path('nasaApod', views.nasaAPOD, name= "APOD"),
    path('ImgLugares', vistasPhoto.LugaresImgs, name="imglugares"),
    path('ImgColores', vistasPhoto.ColoresImgs, name="imgcolores"),
    path('thumbnails/', vistasPhoto.returnThumbnails, name='thumbnails'),
    path('lugar/<str:lugar>/', vistasPhoto.returnLugares, name="lugar"),
    path('categoria/<str:categoria>/', vistasPhoto.returnCategoria, name="categoria")
    
]





