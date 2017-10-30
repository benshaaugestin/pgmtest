from django.db import models


class Candidate(models.Model):
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    college_name=models.CharField(max_length=100)
    year_of_passout=models.IntegerField()
    code = models.FileField(upload_to='media/file', verbose_name='Code File',null=True)
    exam_date = models.DateTimeField()

    def __str__(self):
        return self.name



class Question(models.Model):
    ques_no=models.IntegerField()
    question=models.TextField()
    mark=models.IntegerField()

    def __str__(self):
        return self.question
