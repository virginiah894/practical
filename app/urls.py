from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name ='home'),
    path('update/',views.student_update,name='update'),
    path('delete/<int:pk>/',views.student_delete,name='delete'),
    path('student_detail/<int:pk>/', views.student_details, name = 'student-det'),
    path('student_update/<int:pk>/', views.student_update, name = 'stu-update'),


    


    

    
]