from django.contrib import admin
# from testapp.models import Employee
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','designation','location','salary']

admin.site.register(Employee,EmployeeAdmin)
