from django.shortcuts import render

# Create your views here.

def show_daftarAtlet(request):
    role = 'pelatih'

    if role == 'pelatih':
        data = {
            "role": role
        }
        return render(request, "daftar_atlet.html", data)
    
    elif role == 'umpire':
        data = {
            "role": role
        }
        return render(request, "daftar_atlet.html", data)
    
    

def show_registAtlet(request):
    role = 'pelatih'

    data = {
            "role": role
        }
    return render(request, "regist_atlet.html", data)
