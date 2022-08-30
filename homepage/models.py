from distutils.command import upload
from django.db import models

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=100)
    site_link = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics')
    github_link = models.CharField(max_length=500)
    view_code = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    



class FrondEndLanguages(models.Model):
    name = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name



class BackEndLanguages(models.Model):
    name = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name


class ServerLanguages(models.Model):
    name = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name




class NonTechnologySkill(models.Model):
    name = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name




