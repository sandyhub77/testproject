from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def my_fun(request):
    obj = Employee.objects.filter(salary__lt=60000)  # ORM
    # obj = Employee.objects.filter(id__in=[1,3])  # ORM
    # obj = Employee.objects.get(id=3)  # disable for loop in html
    # obj = Employee.objects.all()  # all records
    #obj = Employee.objects.filter(name__contains='s')  # ORM




    # dct={'obj':obj}


    return render(request,'testapp/first.html',{'obj':obj})  #can send only dict to html
