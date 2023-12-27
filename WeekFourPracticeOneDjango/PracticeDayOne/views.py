from django.shortcuts import render
from app.models import StudentModel

def home(request):
    data=StudentModel.objects.all()
    print(data)
    return render(request, 'home.html',{'data':data})
