from django.shortcuts import render, get_list_or_404, redirect
from .models import Teacher
from forms import TeacherForm

# Create your views here.
# function to get all teachers


def teacherList(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

# function to get a single teacher


def teacherDetail(request, id):
    teacher = get_list_or_404(Teacher, id=id)
    return render(request, 'teacher.html', {'teacher': teacher})

# function to add a new teacher


def addTeacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm()
    return render(request, 'addteacher.html', {'form': form})
