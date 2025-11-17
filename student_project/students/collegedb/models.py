from django.db import models
class Student(models.Model):
     name=models.CharField(max_length=40)
     usn=models.CharField(max_length=10, primary_key=True)
     cgpa=models.FloatField()
     branch=models.CharField(max_length=5)
     gender=models.CharField(max_length=10)
     phone= models.BigIntegerField(max_length=10)


class Professor(models.Model):
     name=models.CharField(max_length=40)
     prof_id=models.CharField(max_length=10,primary_key=True)
     rating=models.FloatField()
     branch=models.CharField(max_length=5)
     gender=models.CharField(max_length=10)
     phone= models.BigIntegerField(max_length=10)
     

