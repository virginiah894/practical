import datetime
from django.db import models
from django.utils import timezone
from PIL import Image



class Stream (models.Model):
    stream_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.stream_name




  
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    reg_num = models.CharField(max_length=3,null=True)
    date = models.DateTimeField(default=timezone.now)
    stream_name = models.ForeignKey(Stream, on_delete=models.CASCADE,null=True)
    photo = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name


    class Meta:
         ordering = ['-date']
    
    @classmethod
    def search_student(cls, name):
        student= Student.objects.filter(name__icontains = name)
        return student