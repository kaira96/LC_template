from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student


def add_student(request):
    if request.method == 'POST':
         form = StudentForm(request.POST)
         if form.is_valid():
             student = form.save()
             return redirect(student)
    else:
        form = StudentForm()
    return render(request, 'crm/add_student.html', {'form': form})


def all_students(request):
    students = Student.objects.all()
    return render(request, 'crm/all_students.html', {'students': students})