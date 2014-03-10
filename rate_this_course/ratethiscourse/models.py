from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.

class University(models.Model):

    name = models.CharField(max_length=128,unique=True)
    location = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"

class Course(models.Model):

    name = models.CharField(max_length=128, unique=True)
    
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.name
        
class Module(models.Model):
    name = models.CharField(max_length=128, unique=True)
    year = models.IntegerField()
    lecturer = models.CharField(max_length=128)

    university = models.ForeignKey(University)
    course = models.ForeignKey(Course)
    students = models.ManyToManyField(User)
    
    def __unicode__(self):
        return self.name
    
    
class UserProfile(models.Model):

    user = models.OneToOneField(User)

    university = models.ForeignKey(University)
    course = models.ForeignKey(Course)

    def __unicode__(self):  
        return self.user.username

class Comment(models.Model):

    message = models.CharField(max_length=7000)
    date = models.DateTimeField(default=datetime.now, blank=True)

    #writer = models.ForeignKey(User)
    module = models.ForeignKey(Module) 

    def __unicode__(self):
        return self.message

class Rating(models.Model):

    value = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    #writer = models.OneToOneField(User)
    module = models.ForeignKey(Module) 

    def __unicode__(self):
        return str(self.value)











