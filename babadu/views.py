from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from babadu.models import *
from babadu.forms import *
from django.http import HttpResponse
from django.core import serializers
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

def show_babadu(request):
    return render(request, "main.html")

def register(request):
    return render(request, "register.html")

def register_atlet(request):
    form = RegisterAtletForm()
    if request.method == "POST":
        form = RegisterAtletForm(request.POST)
        if form.is_valid():
            member = Member.objects.create(
                nama=form.cleaned_data['nama'],  
                email=form.cleaned_data['email'], 
                is_atlet=True
            )
            atlet = Atlet.objects.create(
                member=member,
                ngr_asal=form.cleaned_data['ngr_asal'],
                tanggal_lahir=form.cleaned_data['tanggal_lahir'],
                play_right=form.cleaned_data['play_right'],
                height=form.cleaned_data['tinggi_badan'],
                jenis_kelamin=form.cleaned_data['jenis_kelamin'],
            )
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('babadu:login')
    context = {'form':form}
    return render(request, 'register_atlet.html', context)

def register_pelatih(request):
    try:
        kategori = Spesialisasi.objects.get(kategori="Ganda Putra")
    except:
        Spesialisasi.objects.create(kategori="Tunggal Putra")
        Spesialisasi.objects.create(kategori="Tunggal Putri")
        Spesialisasi.objects.create(kategori="Ganda Putra")
        Spesialisasi.objects.create(kategori="Ganda Putri")
        Spesialisasi.objects.create(kategori="Ganda Campuran")

    form = RegisterPelatihForm()
    if request.method == "POST":
        form = RegisterPelatihForm(request.POST)
        if form.is_valid():
            member = Member.objects.create(
                nama=form.cleaned_data['nama'],  
                email=form.cleaned_data['email'], 
                is_pelatih=True
            )

            pelatih = Pelatih(
                member=member,
                negara=form.cleaned_data['negara'],
                tanggal_mulai=form.cleaned_data['tanggal_mulai'],
            )
            pelatih.save()
            form2 = RegisterPelatihForm(request.POST, instance=pelatih)
            form2.save(commit=False)
            form2.save_m2m()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('babadu:login')
    context = {'form':form}
    return render(request, 'register_pelatih.html', context)

def register_umpire(request):
    form = RegisterUmpireForm()
    if request.method == "POST":
        form = RegisterUmpireForm(request.POST)
        if form.is_valid():
            member = Member.objects.create(
                nama=form.cleaned_data['nama'],  
                email=form.cleaned_data['email'], 
                is_umpire=True
            )

            umpire = Umpire.objects.create(
                member=member,
                negara=form.cleaned_data['negara'],
            )
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('babadu:login')
    context = {'form':form}
    return render(request, 'register_umpire.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('babadu:show_babadu')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('babadu:login')

def show_xml(request):
    data = Pelatih.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")