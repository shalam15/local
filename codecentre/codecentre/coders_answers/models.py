from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.
class Answer(models.Model):
     #user = models.ForeignKey(User, related_name='Coders_Answer', on_delete=models.CASCADE)
     user=models.CharField(default='', max_length=30, primary_key=True)
     FirstName=models.CharField(default='',max_length=30)
     LastName=models.CharField(default='',max_length=30)
     Languages = (
         ('1', 'Python'),
         ('2', 'java'),
         ('3', 'javaScript'),
         ('4', 'c++')
     )
     answerLanguage= models.CharField(default='',max_length=3, choices=Languages)
     answerContent=models.TextField(default='',max_length=1000)

     def __str__(self):
         return self.user
