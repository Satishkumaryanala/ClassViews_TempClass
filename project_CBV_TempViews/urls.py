"""
URL configuration for project_CBV_TempViews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

# for rendering html page by using urls directly
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('TempViews/',TempViews.as_view(),name='TempViews'),

    path('TempView_by_url/',TemplateView.as_view(template_name='TempView_by_url.html'),name='TempView_by_url'),

    path('Temp_context/',Temp_context.as_view(),name='Temp_context'),

    path('Temp_form/',Temp_form.as_view(),name='Temp_form'),
]
