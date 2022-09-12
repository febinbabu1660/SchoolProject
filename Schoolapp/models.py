from django.db import models

# Create your models here.
class tbl_studreg(models.Model):
    name=models.CharField(max_length=15)
    p_name=models.CharField(max_length=15)
    course = models.CharField(max_length=15)
    sl_course = models.CharField(max_length=15)
    phone=models.IntegerField()
    mark=models.IntegerField()
    place=models.CharField(max_length=15)
    username=models.CharField(max_length=15)
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class tbl_login(models.Model):
    email=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=15)


