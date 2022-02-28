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
        form = StudentForm(request.POST,request.FILES)
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
        form = StudentForm(request.POST,request.FILES, instance = student)
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

def search_results(request):
    if 'name' in request.GET and request.GET['name']:
        search_term = request.GET.get('name')
        searched_stu = Student.objects.filter(name__icontains = search_term)
        if not search_term :
            search_term = ""
        message = f"{search_term}"
        profile_pic = Student.objects.all()
        return render(request, 'search.html', {'message':message, 'stu':searched_stu, 'profile_pic':profile_pic})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message':message})






    
  

