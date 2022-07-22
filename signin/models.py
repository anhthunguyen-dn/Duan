from django.db import models
from signup.models import NguoiDung
# Create your models here.

class Nhanvien(models.Model):
    ten = models.CharField(max_length = 100)
    chuc_vu = models.CharField(max_length = 100)
    nam_sinh = models.CharField(max_length = 100)

    def __str__(self):
        return self.ten