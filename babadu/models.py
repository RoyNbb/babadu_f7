from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
import uuid

BOOL_CHOICES1 = ((True, "Right"), (False, "Left"))
BOOL_CHOICES2 = ((True, "Putra"), (False, "Putri"))

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    is_atlet = models.BooleanField(default=False)
    is_pelatih = models.BooleanField(default=False)
    is_umpire = models.BooleanField(default=False)

class Atlet(models.Model):
    member = models.OneToOneField(Member, on_delete=models.SET_NULL, null=True)
    ngr_asal = models.CharField(max_length=50)
    tanggal_lahir = models.DateField(default=timezone.now)
    play_right = models.BooleanField(choices=BOOL_CHOICES1)
    height = models.IntegerField(default=0)
    jenis_kelamin = models.BooleanField(choices=BOOL_CHOICES2)
    world_rank = models.IntegerField(blank=True, null=True)

class Spesialisasi(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	kategori = models.CharField(max_length=30)

	def __str__(self):
		return self.kategori

class Pelatih(models.Model):
    member = models.OneToOneField(Member, on_delete=models.SET_NULL, null=True)
    negara = models.CharField(max_length=50, default="Indonesia")
    tanggal_mulai = models.DateField(default=timezone.now)
    kategori = models.ManyToManyField(Spesialisasi,blank=True, null=True)

class Umpire(models.Model):
    member = models.OneToOneField(Member, on_delete=models.SET_NULL, null=True)
    negara = models.CharField(max_length=50)
