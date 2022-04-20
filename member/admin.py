from django.contrib import admin
from .models import *
# Register your models here.

class AdminMember(admin.ModelAdmin):
    list_display = ['company_name', 'contact_number', 'category']


admin.site.register(Member, AdminMember)