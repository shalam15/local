from django.db import models

# Create your models here.
from django.db import models



class questionToBeAnswerd(models.Model):
    #this is super bad programming but till i know how to figure it out
    Usernames=(
        ('1', 'shalam15'),
        ('2', 'ajayiabdulsalam'),
    )
    #the model from Question will be the one here represented as an uneditable TextField
    listOfQuestion=(
        ('1','The Question Goes Here'),
    )
    whoAsked=models.CharField(default='',max_length=1, choices=Usernames)
    theQuestion = models.CharField(default='',max_length=30, choices=listOfQuestion)

    def __str__(self):
        return self.theQuestion


class answeringTheQuestion(models.Model):
    Usernames = (
        ('1', 'shalam15'),
        ('2', 'ajayiabdulsalam'),
    )
    # the model from Question will be the one here represented as an uneditable TextField
    listOfQuestion = (
        ('1', 'The Question Goes Here'),
    )


    Languages=(
        ('1', 'Pyhton'),
        ('2','Java'),
        ('3','JavaScript'),
        ('4','c++'),
    )
    whoAsked = models.CharField(default='', max_length=1, choices=Usernames)
    theQuestion=models.TextField(default=listOfQuestion , max_length=10000)
    answerRequestedIn=models.CharField(default='', max_length=1, choices= Languages)
    #depending on the amount of languages specifed to be answerd, the amount of textfield would be populated(no more than 2 answering at once)
    answerWith=models.CharField(default='',max_length=2, choices=Languages)
    theAnswers=models.TextField(default='',max_length=10000)

    def __str__(self):
        return self.theAnswers
