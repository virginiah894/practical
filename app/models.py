from django.db import models


class Stream (models.Model):
    stream_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.stream_name




  
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    reg_num = models.CharField(max_length=3,null=True)
    stream_name = models.ForeignKey(Stream, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.name
