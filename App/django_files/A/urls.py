"""
URL configuration for A project.

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
from django.urls import path,include
from . import views
app_name = "A_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('@hm/birthday/',include('birthday.urls'),name='birthday'),
    path('@hm/product/',include('product.urls'),name='product'),
    path('@hm/get_report/',include('get_the_report.urls'),name='get_the_report'),
    path('@hm/get_coin_report/',include('get_coin_report.urls'),name='get_coin_report'),
    path('@hm/honeymoonatr/',include('honeymoonatr.urls'),name='honeymoonatr'),
    path('@hm/analyse_excels/',include('analyse_excels.urls'),name='analyse_excels'),
    path('@hm/club/',include('club.urls'),name='club'),
    path('@hm/Lottery/',include('Lottery.urls'),name='Lottery'),
    # path('@hm/analyse_excels/result/',include('analyse_excels.urls'),name='sub_analyse_excels'),
    path('',views.home,name = 'home'),
    # path("__debug__/", include("debug_toolbar.urls")),
]

