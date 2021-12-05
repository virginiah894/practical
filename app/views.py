from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from.forms import StudentForm

# Create your views here.


def home(request):
    students = Student.objects.all()
    streams = Stream.objects.all()
    return render(request, 'index.html',locals())



def student_update(request):
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form .save()
            return redirect('home')
        
         
    else:
        form = StudentForm()
    return render(request,'student_form.html',locals())
    

def student_delete(request,pk):
    student = Student.objects.get(id=pk)
    if request.method=='POST':
        student.delete()
        return redirect('home')
    
    return render(request,'delete.html',locals())


def student_details(request,pk):
    student = Student.objects.get(id=pk)
    context= {
        'student':student,
    }

    return render(request, 'student_details.html', locals())


def update_student(request,pk):
    student = Student.objects.get(id =pk)

    if  request.method == 'POST':
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = StudentForm( instance=student)


    context = {
        'form': form,

    }
    return render (request, 'student_update.html',locals())



def formA(request):
    students = Student.objects.filter(stream_name__stream_name='Form 1A')


    
    return render(request, 'form1a.html',locals())

    


def formB(request):
      students = Student.objects.filter(stream_name__stream_name='Form 1B')
      return render(request, 'form1b.html',locals())

def formC(request):
      students = Student.objects.filter(stream_name__stream_name='Form 1C')
      return render(request, 'form1c.html',locals())





    
  

