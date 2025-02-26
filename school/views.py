from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# Create your views here.

# function to get all students


def studentList(request):
    students = Student.objects.all()
    return render(request, 'studentlist.html', {'students': students})

# function to get a single student


def studentDetail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'studentdetail.html', {'student': student})

    # function to add a student


def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form .is_valid():
            form.save()
            return redirect('studentlist')

    else:
        form = StudentForm()
    return render(request, 'students/addstudent.html', {'form': form})


# function to update a student
def updateStudent(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm(instance=student)
    return render(request, 'updatestudent.html', {'form': form})

# function to delete a student


def deleteStudent(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('studentlist')
    return render(request, 'deletestudent.html', {'student': student})
