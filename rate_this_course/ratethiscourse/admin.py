from django.contrib import admin
from ratethiscourse.models import University, Course, UserProfile, Comment, Rating, Degree

admin.site.register(University)
admin.site.register(Course)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Degree)
