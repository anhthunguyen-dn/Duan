from django.contrib import admin
from signup.models import NguoiDung
# Register your models here.
class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_link = ('name', 'email')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')
    list_per_page = 25
    
admin.site.register(NguoiDung, NguoiDungAdmin)