from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=30)
    email= models.EmailField(max_length=30)
    phone=models.CharField(max_length=10)
    desc=models.TextField()


    def __str__(self):
        return self.name

class Hospital(models.Model):
    name=models.TextField()
    city=models.CharField(max_length=30)
    ownership =models.CharField(max_length=50)
    admissionCapacity = models.CharField(max_length=10)
    covidBeds=models.CharField(max_length=10)
    state=models.CharField(max_length=30)

    def __str__(self):
        return self.name