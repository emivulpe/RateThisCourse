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


class RatingForm(forms.ModelForm):
	value = forms.ChoiceField(widget = forms.RadioSelect(), initial=3, choice=( (1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars') ))
	
	class Meta:
		model = Rating
		fields = ('value')