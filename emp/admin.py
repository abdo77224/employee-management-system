from django.contrib import admin
from django.contrib import admin
from .models import Emp

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'emp_id', 'phone', 'department', 'salary', 'working')

admin.site.register(Emp, EmpAdmin)

# Register your models here.
