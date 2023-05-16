"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from dashboard.views import show_dashboard
from Daftar_Atlet.views import show_daftarAtlet
from Daftar_Atlet.views import show_registAtlet
from Hasil_Pertandingan.views import show_daftar_hasil_pertandingan
from Hasil_Pertandingan.views import show_detail_hasil_pertandingan




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('dashboard/', show_dashboard, name='show_dashboard'),
    path('daftar_atlet/', show_daftarAtlet, name='show_daftarAtlet'),
    path('regist_atlet/', show_registAtlet, name='show_registAtlet'),
    path('hasil_pertandingan/', show_daftar_hasil_pertandingan, name='show_daftar_hasil_pertandingan'),
    path('detail_hasil_pertandingan/', show_detail_hasil_pertandingan, name='show_detail_hasil_pertandingan'),
]
