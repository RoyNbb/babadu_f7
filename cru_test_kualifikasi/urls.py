from django.urls import path
from cru_test_kualifikasi import views

app_name = 'test_kualifikasi'

urlpatterns = [
    path('', views.test_kualifikasi, name='test_kualifikasi'),
    path('pertanyaan_kualifikasi', views.pertanyaan_kualifikasi, name='pertanyaan_kualifikasi')
]