from django import forms
from ratethiscourse.models import University, Course, Comment, Rating, UserProfile, Module
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
	username = forms.CharField(required = True)
	password = forms.CharField(widget = forms.PasswordInput(), required = True)
	
	class Meta:
		model = User
		fields = ('username', 'password', )

class UserForm(forms.ModelForm):
	username = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	password = forms.CharField(widget = forms.PasswordInput(), required = True)
	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
	university = forms.ModelChoiceField(queryset = University.objects.all(), required = True)
	course = forms.ModelChoiceField(queryset = Course.objects.all(), required = False)
	
	class Meta:
		model = UserProfile
		fields = ('university', 'course', ) #must have comma after, otherwise error (weird)

class RatingForm(forms.ModelForm):
	value = forms.ChoiceField(widget = forms.RadioSelect(), choices = ( (1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars') ), required = False)
	
	class Meta:
		model = Rating
		fields = ('value',)
		
class CommentForm(forms.ModelForm):
	message = forms.CharField(widget = forms.Textarea(), required = False)
	
	class Meta:
		model = Comment
		fields = ('message',)
		
class CourseForm(forms.ModelForm):
	name = forms.CharField(required = True)
	university = forms.ModelChoiceField(queryset = University.objects.all(), required = True)
	
	class Meta:
		model = Course
		
class ModuleForm(forms.ModelForm):
	code = forms.CharField(required = True)
	name = forms.CharField(required = True)
	year = forms.IntegerField(required = True)
	lecturer = forms.CharField(required = True)
	description = forms.CharField(widget = forms.Textarea(), required = True)
	university = forms.ModelChoiceField(queryset = University.objects.all(), required = True)
	course = forms.ModelChoiceField(queryset = Course.objects.all(), required = True)
	
	class Meta:
		model = Module
		fields = ('code', 'name', 'year', 'lecturer', 'description', 'university', 'course',)