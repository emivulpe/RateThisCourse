from django import forms
from ratethiscourse.models import University, Degree, Comment, Rating, UserProfile, Course
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
	username = forms.CharField(required = True)
	password = forms.CharField(widget = forms.PasswordInput(), required = True)
	
	class Meta:
		model = User
		fields = ('username', 'password', )

class UserForm(forms.ModelForm):
	username = forms.CharField(required =True)
	email = forms.EmailField(required = True)
	password = forms.CharField(widget = forms.PasswordInput(), required = True)
	confirm_password = forms.CharField(widget = forms.PasswordInput(), required = True)
	first_name = forms.CharField(required = True)
	last_name = forms.CharField(required = True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password','confirm_password', 'first_name', 'last_name')
		
	def clean_username(self):
		username = self.cleaned_data.get('username')
		if (User.objects.filter(username=username).count() == 0):
			return username
		raise forms.ValidationError(u'Username "%s" is already in use.' % username)

	def clean_(self):
		password1 = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('confirm_password')

		if password1 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return self.cleaned_data
	

class UserProfileForm(forms.ModelForm):
	university = forms.ModelChoiceField(queryset = University.objects.all(), required = True)
	degree = forms.ModelChoiceField(queryset = Degree.objects.all(), required = False)
	
	class Meta:
		model = UserProfile
		fields = ('university', 'degree', ) #must have comma after, otherwise error (weird)

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
		
class DegreeForm(forms.ModelForm):
	name = forms.CharField(required = True)
	university = forms.ModelChoiceField(queryset = University.objects.all(), required = True)
	
	class Meta:
		model = Degree
		fields = ('name', 'university',)
		
class CourseForm(forms.ModelForm):
	code = forms.CharField(required = True)
	name = forms.CharField(required = True)
	year = forms.IntegerField(required = True)
	lecturer = forms.CharField(required = True)
	description = forms.CharField(widget = forms.Textarea(), required = True)
	university = forms.ModelChoiceField(queryset = University.objects.all(), required = True)
	degree = forms.ModelChoiceField(queryset = Degree.objects.all(), required = True)
	
	class Meta:
		model = Course
		fields = ('code', 'name', 'year', 'lecturer', 'description', 'university', 'degree',)
