"""recipebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('author/', views.authors),
    path('author/<int:author_id>', views.author),
    path('', views.home_index),
    path('recipe/<int:recipe_id>', views.recipe),
    path('addauthor/', views.add_author),
    path('signup/', views.signup),
    path('login/', views.loginv),
    path('logout/', views.logoutv),
    path('addrecipe/', views.add_recipe),
    path('addauthor/', views.add_author),
]
