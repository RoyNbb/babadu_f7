from django.urls import path
from rd_enrolled import views

app_name = 'rd_enrolled'

urlpatterns = [
    path('', views.rd_enrolled, name='rd_enrolled'),
]