# -*- coding: utf-8 -*-
"""plasystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.contrib.auth import views as auth_views

admin.site.site_header = "Administración"
admin.site.site_title = "sitio administrativo"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
    url(r'^logout/$', auth_views.logout,{'next_page': '/'}),
    url(r'^$', index, name='index'),
    url(r'^productores/', include('productores.urls')),
    url(r'^organizaciones/', include('resultados.urls')),
]
