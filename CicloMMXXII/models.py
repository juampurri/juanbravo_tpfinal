from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):
  name = models.CharField(max_length=40)
  section = models.IntegerField()

  def __str__(self):
    return f"Name: {self.name} - Section: {self.section}"

class Cadetes(models.Model):
  name = models.CharField(max_length=40)
  lastname = models.CharField(max_length=40)
  email = models.EmailField()
  
  def __str__(self):
    return f"Name: {self.name} - Lastname: {self.lastname} - Email: {self.email}"

class Instructor(models.Model):
  name = models.CharField(max_length=40)
  lastname = models.CharField(max_length=40)
  email = models.EmailField()
  subject = models.CharField(max_length=40)
  
  def __str__(self):
    return f"Name: {self.name} - Lastname: {self.lastname} - Email: {self.email} - Subject: {self.subject}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img  = models.ImageField(upload_to='avatares', null=True, blank=True)
