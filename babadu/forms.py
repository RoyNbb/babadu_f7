from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from babadu.models import *
from bootstrap_datepicker_plus.widgets import DatePickerInput


class RegisterAtletForm(ModelForm):
    CHOICES1 = [
        (False, 'Left'),
        (True, 'Right'),
    ]
    play_right = forms.ChoiceField(choices=CHOICES1, widget=forms.RadioSelect(attrs={'id':'input-type'}))

    CHOICES2 = [
        (False, 'Putri'),
        (True, 'Putra'),
    ]
    jenis_kelamin = forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect(attrs={'id':'input-type'}))

    tanggal_lahir = forms.DateField()

    ngr_asal = forms.CharField(max_length=50)

    tinggi_badan = forms.IntegerField()

    nama = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class Meta:
        model = Atlet
        fields = ("nama", "email", "ngr_asal","tanggal_lahir", "play_right", "tinggi_badan", "jenis_kelamin")

class RegisterPelatihForm(ModelForm):
    kategori = forms.ModelMultipleChoiceField(
                        queryset=Spesialisasi.objects.all(),
                        label="Spesialisasi",
                        widget=forms.CheckboxSelectMultiple)
    negara = forms.CharField(max_length=50)


    nama = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class Meta:
        model = Pelatih
        fields = ("nama", "email", "negara","tanggal_mulai", "kategori")
        widgets = {
            "tanggal_mulai": DatePickerInput(),
        }

class RegisterUmpireForm(ModelForm):

    negara = forms.CharField(max_length=50)
    nama = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)

    class Meta:
        model = Umpire
        fields = ("nama", "email", "negara")