from django.shortcuts import render,redirect
from .forms import StudentForm
# Create your views here.

def app_index(request):
    data=StudentForm()
    if request.method == 'POST':
        data=StudentForm(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return redirect('index')
    return render(request, 'app/index.html',{'data':data})

 