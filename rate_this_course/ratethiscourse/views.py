from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response 
from ratethiscourse.models import University, Rating, Comment, Course, Degree, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from ratethiscourse.forms import UserForm, UserProfileForm, RatingForm, CommentForm, CourseForm, DegreeForm, LoginForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from operator import itemgetter
import dbHelper, ajaxGetHelper
import json

token_generator = PasswordResetTokenGenerator()

def index(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	## Get n most recent rows from tables and add to the context dict
	dbHelper.getRecentRows(context_dict, Rating, 'ratings', 10)
	dbHelper.getRecentRows(context_dict, Comment, 'comments', 10)

	## Get all the courses in the db and their ratings, then sort them by their ratings
	ratedCourses = dbHelper.getAllDegreeRatings()
	## Round ratings to 2 decimal places
	for course in ratedCourses:
		course[1] = round(course[1], 2)
	## Sorts all elements in the list using the element at index 1 of each inner list(the rating)
	ratedCourses.sort(key=itemgetter(1))
	## Sort will sort from low to high so we select the last 5 elements as the top 5 and first 5 as the botttom 5
	topFive = ratedCourses[:-6:-1]
	bottomFive = ratedCourses[:5]
	
	context_dict['topfive'] = topFive
	context_dict['bottomfive'] = bottomFive

	return render_to_response('ratethiscourse/index.html', context_dict, context)

def register(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm

	registered = False
	if request.method == 'POST':
		
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		#if the 2 forms are valid
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			#hash pwd with set_password with the set_password method
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.isActive = False
			profile.save()
	
			registered = True
			loggedInUser = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request, loggedInUser)
			
			token = token_generator.make_token(user)
			url = 'http://gucsteamh.pythonanywhere.com/ratethiscourse/validate_user?user=%(user)s&token=%(token)s'%{'user': user.id, 'token': token}

			send_mail('Rate This Course User Verification', 'Please verify your account by clicking this link.\n%s\nThis link will only last 1 day. If you did not request this email please ignore it.'%url, 'gucsteamh@gmail.com', [user.email], fail_silently=False)
		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	context_dict['user_form'] = user_form
	context_dict['profile_form'] = profile_form
	context_dict['registered'] = registered
	return render_to_response('ratethiscourse/register.html', context_dict, context)

def validate_user(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	if request.method == 'GET':
		userid = request.GET.get('user')
		token = request.GET.get('token')
		
		## Check that user and token are in the url
		if userid and token:
			user = User.objects.get(id=userid)
			verify = token_generator.check_token(user, token)
			
			if verify:
				## Set the user to be active when validated
				userprofile = UserProfile.objects.get(user=userid)
				userprofile.isActive = True
				userprofile.save()
		
			context_dict['verify'] = verify
		else:
			context_dict['malformed'] = True
		
		return render_to_response('ratethiscourse/validate_user.html', context_dict, context)
	
def resend_validation_email(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
	else:
		context_dict['userauth'] = 'anon'
		return render_to_response('ratethiscourse/resend_validation_email.html', context_dict, context)
	
	if (userprofile.isActive == False):
		token = token_generator.make_token(user)
		url = 'http://gucsteamh.pythonanywhere.com/ratethiscourse/validate_user?user=%(user)s&token=%(token)s'%{'user': user.id, 'token': token}
		user.email_user('Rate This Course User Verification', 'Please verify your account by clicking this link.\n%s\nThis link will only last 1 day. If you did not request this email please ignore it.'%url, 'gucsteamh@gmail.com')
		context_dict['sent'] = True
	else:
		context_dict['sent'] = False
		
	return render_to_response('ratethiscourse/resend_validation_email.html', context_dict, context)
	
def user_login(request):
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'POST':
		
		loginForm = LoginForm(request.POST)
		username = form.data['username']
		password = form.data['password']
		
		user = authenticate(username=username, password=password)

		#if object, the details are correct
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/ratethiscourse/')
			else:
				return HttpResponse("Your Rango account is disabled")
		else:
			context_dict['form'] = form
			return render_to_response('ratethiscourse/login.html', context_dict, context)

	else:
		form = LoginForm()
		context_dict['form'] = form
		return render_to_response('ratethiscourse/login.html', context_dict, context)
		
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/ratethiscourse/')
	
def user_profile(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
		
	if request.method == 'POST':
		context_dict['posted'] = True
		userprofileform = UserProfileForm(request.POST)
		
		if userprofileform.is_valid():
			user = request.user
			userprofile.degree = userprofileform.cleaned_data['degree']
			userprofile.save()
			context_dict['success'] = True
		else:
			context_dict['success'] = False
	
	else:
		context_dict['posted'] = False
		userprofileform = UserProfileForm()
	
	context_dict['userprofileform'] = userprofileform
	return render_to_response('ratethiscourse/user_profile.html', context_dict, context)

def universities(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	universities = University.objects.all().order_by('name')
	univerisityList = []
	for uni in universities:
		university = [uni]
		university.append(str(uni).replace(' ', '_'))
		univerisityList.append(university)
	context_dict['universities'] = univerisityList
	
	return render_to_response('ratethiscourse/universities.html', context_dict, context)
	

def university(request, uni_name_url):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm

	# Change underscores in the category name to spaces.
	# URLs don't handle spaces well, so we encode them as underscores.
	# We can then simply replace the underscores with spaces again to get the name.
	uni_name = uni_name_url.replace('_', ' ')

	context_dict['uni_name'] = uni_name
	context_dict['uni_name_url'] = uni_name_url

	try:
		university = University.objects.get(name=uni_name)
		## Get all ratings for the courses at the university
		ratedCourses = dbHelper.getUniDegreeRatings(university)
		for course in ratedCourses:
			if isinstance(course[2], str):
				continue
			else:
				course[2] = round(course[2], 2)
			
		context_dict['courses'] = ratedCourses
		context_dict['university'] = university
	except University.DoesNotExist:
		pass

	return render_to_response('ratethiscourse/university.html', context_dict, context)

def course(request, uni_name_url, course_name_url):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	course_name = course_name_url.replace('_', ' ')
	uni_name = uni_name_url.replace('_', ' ')
	context_dict['uni_name'] = uni_name 
	context_dict['course_name'] = course_name 
	context_dict['uni_name_url'] = uni_name_url
	context_dict['course_name_url'] = course_name_url
	
	
	uni = University.objects.get(name=uni_name)
	course = Degree.objects.get(name=course_name, university=uni)
	## Get all the ratings for each module in the course at the uni
	modules = dbHelper.getDegreeRatings(uni, course)
	## Round ratings to 2 decimal places
	for module in modules:
		if isinstance(module[2], str):
			continue
		else:
			module[2] = round(module[2], 2)
	context_dict['modules'] = modules
	
	return render_to_response('ratethiscourse/course.html', context_dict, context)
	
def module(request, uni_name_url, course_name_url, module_name_url):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	module_name = module_name_url.replace('_', ' ')
	course_name = course_name_url.replace('_', ' ')
	uni_name = uni_name_url.replace('_', ' ')
	context_dict['uni_name'] = uni_name
	context_dict['course_name'] = course_name
	context_dict['module_name'] = module_name
	context_dict['uni_name_url'] = uni_name_url
	context_dict['course_name_url'] = course_name_url
	context_dict['module_name_url'] = module_name_url
	
	uni = University.objects.get(name=uni_name)
	degree = Degree.objects.get(name=course_name, university=uni)
	course = Course.objects.get(name=module_name, degree=degree, university=uni)
	context_dict['module'] = course
	user = request.user
	
	## Check if user is logged in
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
		
		auth = str(userprofile.degree) == course_name
		context_dict['auth'] = auth
	else:
		context_dict['auth'] = False
	
	if request.method == 'POST':
		commentform = CommentForm(request.POST)
		ratingform =  RatingForm(request.POST)

		commentformdata = commentform.data
		ratingformdata = ratingform.data
		
		if commentform.data['message']:
			if commentform.is_valid():
				comment = commentform.save(commit=False)
				comment.course = course
				comment.save()
			else:
				print commentform.errors
		
		if ratingform.data.has_key('value'):
			if ratingform.is_valid():
				rating = ratingform.save(commit=False)
				rating.course = course
				rating.save()
			else:
				print ratingform.errors

	else:
		commentform = CommentForm()
		ratingform = RatingForm()
	
	comments = Comment.objects.filter(course=course)
	context_dict['comments'] = comments
	## Round ratings to 2 decimal places
	rating = dbHelper.getCourseRating(course)
	if isinstance(rating, str):
		context_dict['rating'] = rating
	else:
		context_dict['rating'] = round(rating, 2)
	context_dict['comment_form'] = commentform
	context_dict['rating_form'] = ratingform
	
	return render_to_response('ratethiscourse/module.html', context_dict, context)
	
def add_course(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
		
	if request.method == 'POST':

		name = request.POST['name']
		university = request.POST['university']
		
		courseform = DegreeForm(request.POST)
		
		if courseform.is_valid():
			course = courseform.save()
			context_dict['name'] = name
		else:
			print courseform.errors
	else:
		context_dict['name'] = 'NotPosted'
		courseform = DegreeForm()
		
	context_dict['courseform'] = courseform
	return render_to_response('ratethiscourse/add_course.html', context_dict, context)
	
def add_module(request):
	context = RequestContext(request)
	context_dict = {}
	
	loginForm = LoginForm()
	context_dict['loginform'] = loginForm
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
	
	if request.method == 'POST':

		name = request.POST['name']
		university = request.POST['university']
		degree = request.POST['degree']
		
		moduleform = CourseForm(request.POST)
		
		if moduleform.is_valid():
			module = moduleform.save()
			context_dict['name'] = name
		else:
			print moduleform.errors
	else:
		context_dict['name'] = 'NotPosted'
		moduleform = CourseForm()
		
	context_dict['moduleform'] = moduleform
	return render_to_response('ratethiscourse/add_module.html', context_dict, context)    	

def get_courses(request):
	context = RequestContext(request)
	university_id = None
	
	if request.method == 'GET':
		university_id = request.GET.get('university_id')
		
	courses = [["", "---------"]]
	
	if university_id:
		for course in Degree.objects.filter(university=university_id).values('id', 'name'):
			courses.append([course['id'], course['name']])
		
	return HttpResponse(json.dumps(courses), content_type="application/json")
	
def get_user_uni(request):
	context = RequestContext(request)
	
	university_id = ajaxGetHelper.getUserData(request, 'university')
	
	return HttpResponse(university_id)

def get_user_course(request):
	context = RequestContext(request)
	
	course_id = ajaxGetHelper.getUserData(request, 'degree')
		
	return HttpResponse(course_id)

def ajax_login(request):
	context = RequestContext(request)
	response = None
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		username = form.data['username']
		password = form.data['password']
		
		user = authenticate(username=username, password=password)

		#if object, the details are correct
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponse('valid')
			else:
				return HttpResponse('inactive')
		else:
			return HttpResponse('invalid')
			
def ajax_logout(request):
	logout(request)
	
	return HttpResponse(True)