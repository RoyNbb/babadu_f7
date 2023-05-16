from django.shortcuts import render

# Create your views here.
def show_dashboard(request):
    role = 'umpire'

    if role == 'atlet':
        data = {
            "nama_lengkap": "Westleigh Pengilley",
            "negara": "Indonesia",
            "email": "wpengilley0@instagram.com",
            "tanggal_lahir": "03/12/1990",
            "play": "Left",
            "tinggi_badan": "174cm",
            "jenis_kelamin": "Laki-laki",
            "pelatih": "Mirabel Dicte",
            "status": "Qualified",
            "world_rank": "1",
            "total_poin": "2200",
            "role": role
        }
        return render(request, "dashboard_atlet.html", data)
    elif role == "pelatih":
        data = {
            "role": role,
            "nama": "Mirabel Dicte",
            "negara": "Argentina",
            "email": "mdictee@ucla.edu",
            "spesialisasi_kategori":  "Tunggal Putra & Tunggal Putri",
            "tanggal_mulai": "29/05/2022"
        }
        return render(request, "dashboard_pelatih.html", data)
    elif role == "umpire":
        data = {
            "role": role,
            "nama_lengkap": "Constance Marioneau",
            "negara": "Rusia",
            "email": "cmarioneau7@live.com"
        }
        return render(request, "dashboard_umpire.html", data)
    else:
        return render(request, "error_page.html")