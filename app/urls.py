from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name ='home'),
    path('update/',views.student_update,name='update'),
    path('delete/<int:pk>/',views.student_delete,name='delete'),
    path('student_detail/<int:pk>/', views.student_details, name = 'student-det'),
    path('studentupdate/<int:pk>/', views.update_student, name = 'stu-update'),
    path('form1a/',views.formA,name='oneA'),
    path('form1b/',views.formB,name='oneB'),
    path('form1c/',views.formC,name='oneC'),
    path(r'^search/', views.search_results, name = 'search_results'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

    