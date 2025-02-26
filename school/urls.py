from django.urls import path
from .views import studentList, studentDetail, addStudent, updateStudent, deleteStudent

urlpatterns = [
    path('', studentList, name='studentlist'),
    path('<int:id>/', studentDetail, name='studentdetail'),
    path('add/', addStudent, name='addstudent'),
    path('student/update/<int:id>/', updateStudent, name='updatestudent'),
    path('student/delete/<int:id>/', deleteStudent, name='deletestudent'),
]
