from django.urls import path
from .import views

urlpatterns = [
    path('', views.teacherList, name='teacherlist'),
    path('<int:id>/', views.teacherDetail, name='teacherdetail'),
    path('add/', views.addTeacher, name='addteacher'),

]
