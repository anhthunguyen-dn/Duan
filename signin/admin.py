from django.contrib import admin
from signup.models import NguoiDung
from signin.models import Nhanvien

# Register your models here.
class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('ten', 'chuc_vu', 'nam_sinh')
    list_display_link = ('ten', 'chuc_vu', 'nam_sinh')
    list_filter = ('ten', 'chuc_vu', 'nam_sinh')
    search_fields = ('ten', 'chuc_vu', 'nam_sinh')
    list_per_page = 25
    
admin.site.register(Nhanvien, NguoiDungAdmin)