from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.

class University(models.Model):

    name = models.CharField(max_length = 128, unique = True)
    location = models.CharField(max_length = 256)
    uni_domain_code = models.CharField(max_length = 128, unique = True)
    description = models.CharField(max_length = 2048)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Universities"

class Degree(models.Model):

    name = models.CharField(max_length = 128)
    
    university = models.ForeignKey(University)

    def __unicode__(self):
        return self.name
        
    class Meta:
        unique_together = ("name", "university")
        
class Course(models.Model):
    
    code = models.CharField(max_length = 32)
    name = models.CharField(max_length = 128)
    year = models.IntegerField()
    lecturer = models.CharField(max_length = 128)
    description = models.CharField(max_length = 1024)

    university = models.ForeignKey(University)
    degree = models.ForeignKey(Degree)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        unique_together = ("name", "university", "degree")
    
    
class UserProfile(models.Model):

    isActive = models.BooleanField()
    
    user = models.OneToOneField(User)
    university = models.ForeignKey(University)
    degree = models.ForeignKey(Degree, blank = True, null = True)

    def __unicode__(self):  
        return self.user.username

class Comment(models.Model):

    message = models.CharField(max_length = 7000)
    date = models.DateTimeField(default = datetime.now, blank = True)

    #writer = models.ForeignKey(User)
    course = models.ForeignKey(Course) 

    def __unicode__(self):
        return self.message

class Rating(models.Model):

    value = models.IntegerField()
    date = models.DateTimeField(default = datetime.now, blank = True)

    #writer = models.ForeignKey(User)
    course = models.ForeignKey(Course) 

    def __unicode__(self):
        return str(self.value)











