"""Image_Detection URL Configuration

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
from . import views
from django.contrib.auth.views import LoginView
from criminal.views import crime_create
from missing.views import miss_create
from feedback.views import feedback_create
from news.views import news_detail_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', LoginView.as_view(), name='login' ),
        path('crime/', crime_create , name='crime'),
        path('miss/', miss_create, name='miss'),
        path('feedback/', feedback_create, name='feedback'),
        path('logout', views.user_logout, name='user_logout'),
        path('news/', news_detail_view, name='news')
        ]
urlpatterns += staticfiles_urlpatterns()
