from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def rd_enrolled(request):
    # if(request.session["user_type"] != "pelatih"):
    #     return redirect("home")
        
    # if request.method == "POST":
    #     no_batch = request.POST.get('no_batch')
    #     tempat = request.POST.get('tempat')
    #     tanggal = request.POST.get('tanggal')

        # with connection.cursor() as cursor:
        #     cursor.execute("INSERT INTO rs_cabang values (%s,%s,%s)",[no_batch, tempat, tanggal])
        #     cursor.execute("SELECT * FROM rs_cabang where kode_rs=%s", [kode_rs])
        #     row_rs_cabang = dictfetchall(cursor)[0]
        #     return redirect("sesi-konsultasi:daftar_rs_cabang")
    
    return render(request, 'rd_enrolled.html')