from django import forms
from ratethiscourse.models import University, Course, Comment, Rating, UserProfile
from django.contrib.auth.models import User
 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('university',) #must have comma after, otherwise error (weird)
