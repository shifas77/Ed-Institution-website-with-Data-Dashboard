

"""
Definition of models.
"""

from django.db import models

# Create your models here.
class student(models.Model):  
    eid = models.EmailField(max_length=100)  
    uname = models.CharField(max_length=100)
    mno=models.CharField(max_length=15)
    pswd = models.CharField(max_length=20)  
    cpswd = models.CharField(max_length=20)  

    class Meta:  
        db_table = "studenttb"


class professionals(models.Model):  
    id = models.AutoField(primary_key=True)
    eid = models.EmailField()  
    name = models.CharField(max_length=100)
    mno=models.CharField(max_length=15)
    pswd = models.CharField(max_length=20)  
    cpswd = models.CharField(max_length=20)  

    class Meta:  
        db_table = "proffesionaltb"

class admin_login(models.Model):  
    id = models.AutoField(primary_key=True)
    uname = models.EmailField()  
    pswd = models.CharField(max_length=20)  
    
    class Meta:  
        db_table = "admin_login"

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')


class UploadImage(models.Model):  
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')
    result=models.CharField(max_length=200,default='pending')  
  
    def __str__(self):  
        return self.caption  


class student_stat(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    color = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)

    class Meta:  
        db_table = "student_stat"



class Higher_S(models.Model):
    id = models.AutoField(primary_key=True)
    CT= models.CharField(max_length=50)
    col1= models.CharField(max_length=50)
    col2 = models.CharField(max_length=50)
    col3 = models.CharField(max_length=50)
    col4 = models.CharField(max_length=50)
    col5 = models.CharField(max_length=50)

    class Meta:  
        db_table = "hs_table"


class Final_HS(models.Model):
    id = models.AutoField(primary_key=True)
    eid= models.CharField(max_length=100)
    uname= models.CharField(max_length=50)
    Course= models.CharField(max_length=50)


    class Meta:  
        db_table = "Final_HS"



class course_selection(models.Model):  
    eid = models.EmailField()  
    uname = models.CharField(max_length=100)
    mno=models.CharField(max_length=15)
    pswd = models.CharField(max_length=20)  
    cpswd = models.CharField(max_length=20)
    Course=models.CharField(max_length=20)

    class Meta:  
        db_table = "course_selection"





