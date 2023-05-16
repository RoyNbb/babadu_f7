from django.shortcuts import render

# Create your views here.
def show_daftar_hasil_pertandingan(request):
    role = 'umpire'

    data = {
        "role": role
    }
    return render(request, "list_hasil_pertandingan.html", data)

def show_detail_hasil_pertandingan(request):
    role = 'umpire'

    data = {
        "role": role
    }
    return render(request, "detail_hasil_pertandingan.html", data)