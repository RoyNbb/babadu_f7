from django.urls import path
from babadu.views import *

app_name = 'babadu'

urlpatterns = [
    path('', show_babadu, name='show_babadu'),
    path('register/', register, name='register'),
    path('register/atlet/', register_atlet, name='register_atlet'),
    path('register/pelatih/', register_pelatih, name='register_pelatih'),
    path('register/umpire/', register_umpire, name='register_umpire'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml')
]