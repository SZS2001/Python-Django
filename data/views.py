from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.

#For adding and showing the students info
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)

        if form.is_valid():
            form.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    stud = Student.objects.all()
    return render(request,'AddShow.html',{'form':form, 'stud':stud})

# For updating the data
def update_data(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = Student.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
    return render(request,'update.html',{'form':form})



#for deleting data

def delete_data(request,id):
    if request.method=='POST':
        pi = Student.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')

