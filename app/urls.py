from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name ='home'),
    path('update/',views.student_update,name='update'),
    path('delete/<int:pk>/',views.student_delete,name='delete'),
    path('student_detail/<int:pk>/', views.student_details, name = 'student-det'),
    path('studentupdate/<int:pk>/', views.update_student, name = 'stu-update'),
    path('form1a/',views.formA,name='oneA'),
    path('form1a/',views.formB,name='oneB'),
    path('form1a/',views.formC,name='oneC'),



    


    

    
]