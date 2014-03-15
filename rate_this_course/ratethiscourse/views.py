from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response 
from ratethiscourse.models import Course, University, Rating, Comment, Module, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from ratethiscourse.forms import UserForm, UserProfileForm, RatingForm, CommentForm, CourseForm, ModuleForm, LoginForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from operator import itemgetter
import json


def index(request):
	# Request the context of the request.
	# The context contains information such as the client's machine details, for example.
	context = RequestContext(request)
   
	
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	uni_list = University.objects.order_by('-name')[:30]
	context_dict = {'universities': uni_list}
	for university in uni_list:
		university.url = university.name.replace(' ', '_')
		
	ratings = Rating.objects.all().order_by('-date')[:10]
	ratingList = []
	for rating in ratings:
		ratingInfo = [rating]
		module = Module.objects.get(id=rating.module.id)
		ratingInfo.append(str(module.university).replace(' ', '_'))
		ratingInfo.append(str(module.course).replace(' ', '_'))
		ratingInfo.append(str(rating.module).replace(' ', '_'))
		ratingList.append(ratingInfo)
	print ratingList
	context_dict['ratings'] = ratingList;
	
	comments = Comment.objects.all().order_by('-date')[:10]
	commentList = []
	for comment in comments:
		commentInfo = [comment]
		module = Module.objects.get(id=comment.module.id)
		commentInfo.append(str(module.university).replace(' ', '_'))
		commentInfo.append(str(module.course).replace(' ', '_'))
		commentInfo.append(str(comment.module).replace(' ', '_'))
		commentList.append(commentInfo)
	
	print commentList
	context_dict['comments'] = commentList;
	
	courses = Course.objects.all()
	ratedCourses = []
	for course in courses:
		ratedCourse = [course]
		course_rating = 0
		j = 0
		modules = Module.objects.filter(course=course)
		if len(modules) > 0:
			for module in modules:
				avg_rating = 0
				i = 0
				ratings = Rating.objects.filter(module=module)
				if len(ratings) > 0:
					for rating in ratings:
						avg_rating = avg_rating + int(str(rating))
						i = i+1
					avg_rating = avg_rating/i
					course_rating = course_rating + avg_rating
					j = j+1
				else:
					continue
			if j>0:
				course_rating = course_rating/j
			else:
				course_rating = "No Ratings"
			ratedCourse.append(course_rating)
			ratedCourse.append(str(course.university).replace(' ', '_'))
			ratedCourse.append(str(course).replace(' ', '_'))
			ratedCourses.append(ratedCourse)
	ratedCourses.sort(key=itemgetter(1))
	ratedCourses.reverse()
	topFive = ratedCourses[:5]
	bottomFive = ratedCourses[:-6:-1]
	
	context_dict['topfive'] = topFive
	context_dict['bottomfive'] = bottomFive
		
	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render_to_response('ratethiscourse/index.html', context_dict, context)

def register(request):

	context = RequestContext(request)

	#boolean for telling the template whether the registration was successful
	#set to False initially
	registered = False

	#if http post, process form data
	if request.method == 'POST':
		token_generator = PasswordResetTokenGenerator()
		
		#attempt to grab info from form
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		#if the 2 forms are valid
		if user_form.is_valid() and profile_form.is_valid():
			#save user form data to db
			user = user_form.save()

			#hash pwd with set_password with the set_password method
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.isActive = False
			profile.save()
			
			token = token_generator.make_token(user)
			url = 'http://gucsteamh.pythonanywhere.com/ratethiscourse/validate_user?user=%(user)s&token=%(token)s'%{'user': user.id, 'token': token}
			
			send_mail('Rate This Course User Verification', 'Please verify your account by clicking this link.\n%s\nThis link will only last 1 day. If you did not request this email please ignore it.'%url, 'gucsteamh@gmail.com', [user.email], fail_silently=False)
			#process profile photo if user provides one
			#if 'picture' in request.FILES:
			#   profile.picture = request.FILES['picture']
			#profile.save()
	
			registered = True
		#invalid form
		else:
			print user_form.errors, profile_form.errors

	#not http, render form with 2 model form instances
	#forms will be blank, ready for input

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	#render template depending on context
	return render_to_response('ratethiscourse/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}, context)

def validate_user(request):
	
	context = RequestContext(request)
	context_dict = {}
	
	if request.method == 'GET':
		userid = request.GET.get('user')
		token = request.GET.get('token')
		
		if userid and token:
			user = User.objects.get(id=userid)
			
			token_generator = PasswordResetTokenGenerator()
			
			verify = token_generator.check_token(user, token)
			
			if verify:
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
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
	else:
		context_dict['userauth'] = 'anon'
		return render_to_response('ratethiscourse/resend_validation_email.html', context_dict, context)
	
	if(userprofile.isActive == False):
		token_generator = PasswordResetTokenGenerator()
		token = token_generator.make_token(user)
		url = 'http://gucsteamh.pythonanywhere.com/ratethiscourse/validate_user?user=%(user)s&token=%(token)s'%{'user': user.id, 'token': token}
		user.email_user('Rate This Course User Verification', 'Please verify your account by clicking this link.\n%s\nThis link will only last 1 day. If you did not request this email please ignore it.'%url, 'gucsteamh@gmail.com')
		context_dict['sent'] = True
	else:
		context_dict['sent'] = False
		
	return render_to_response('ratethiscourse/resend_validation_email.html', context_dict, context)
	
def user_login(request):
	
	context = RequestContext(request)
	if request.method == 'POST':
		
		form = LoginForm(request.POST)
		username = form.data['username']
		password = form.data['password']

		#use Django to see if user + pass is valid, return object if it is
		user = authenticate(username=username, password=password)

		#if object, the details are correct
		if user is not None:
			#is account active?
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/ratethiscourse/')
			else:
				return HttpResponse("Your Rango account is disabled")
		else:
			#bad login details
			return render_to_response('ratethiscourse/login.html', {'form': form}, context)

	else:
		form = LoginForm()
		return render_to_response('ratethiscourse/login.html', {'form': form}, context)

def user_logout(request):

	#we know user is logged in, we can just logout
	logout(request)

	return HttpResponseRedirect('/ratethiscourse/')     

def universities(request):
	
	context = RequestContext(request)
	context_dict = {}
	
	universities = University.objects.all().order_by('name')
	univerisityList = []
	for uni in universities:
		university = [uni]
		university.append(str(uni).replace(' ', '_'))
		univerisityList.append(university)
	context_dict['universities'] = univerisityList
	
	return render_to_response('ratethiscourse/universities.html', context_dict, context)
	

def university(request, uni_name_url):
	# Request our context from the request passed to us.
	context = RequestContext(request)

	# Change underscores in the category name to spaces.
	# URLs don't handle spaces well, so we encode them as underscores.
	# We can then simply replace the underscores with spaces again to get the name.
	uni_name = uni_name_url.replace('_', ' ')

	# Create a context dictionary which we can pass to the template rendering engine.
	# We start by containing the name of the category passed by the user.
	context_dict = {'uni_name': uni_name}
	context_dict['uni_name_url'] = uni_name_url

	try:
		# Can we find a category with the given name?
		# If we can't, the .get() method raises a DoesNotExist exception.
		# So the .get() method returns one model instance or raises an exception.
		university = University.objects.get(name=uni_name)

		# Retrieve all of the associated pages.
		# Note that filter returns >= 1 model instance.
		courseList = []
		for course in Course.objects.filter(university=university):
			details = [str(course)]
			details.append(str(course).replace(' ', '_'))
			courseList.append(details)
			
		courses = Course.objects.filter(university=university)
		ratedCourses = []
		for course in courses:
			ratedCourse = [course]
			ratedCourse.append(str(course).replace(' ', '_'))
			course_rating = 0
			j = 0
			modules = Module.objects.filter(course=course)
			if len(modules) > 0:
				for module in modules:
					avg_rating = 0
					i = 0
					ratings = Rating.objects.filter(module=module)
					if len(ratings) > 0:
						for rating in ratings:
							avg_rating = avg_rating + int(str(rating))
							i = i+1
						avg_rating = avg_rating/i
						course_rating = course_rating + avg_rating
						j = j+1
					else:
						continue
				if j>0:
					course_rating = course_rating/j
				else:
					course_rating = "No ratings"
			else:
				course_rating = "No ratings"
			ratedCourse.append(course_rating)
			ratedCourses.append(ratedCourse)
			
		# Adds our results list to the template context under name pages.
		context_dict['courses'] = ratedCourses
		# We also add the category object from the database to the context dictionary.
		# We'll use this in the template to verify that the category exists.
		context_dict['university'] = university
	except University.DoesNotExist:
		# We get here if we didn't find the specified category.
		# Don't do anything - the template displays the "no category" message for us.
		pass

	# Go render the response and return it to the client.
	return render_to_response('ratethiscourse/university.html', context_dict, context)

def course(request, uni_name_url, course_name_url):
	
	context = RequestContext(request)
	course_name = course_name_url.replace('_', ' ')
	uni_name = uni_name_url.replace('_', ' ')
	context_dict = {'uni_name': uni_name, 'course_name': course_name, 'uni_name_url': uni_name_url, 'course_name_url': course_name_url}
	
	
	uni = University.objects.get(name=uni_name)
	course = Course.objects.get(name=course_name, university=uni)
	
	modules = []
	for module in Module.objects.filter(university=uni, course=course):
		ratingList = [str(module)]
		ratingList.append(str(module).replace(' ', '_'))
		ratings = Rating.objects.filter(module=module)
		if len(ratings) > 0:
			avg_rating = 0.0
			i = 0
			for rating in ratings:
				avg_rating = avg_rating + int(str(rating))
				i = i+1
			avg_rating = avg_rating/i
			ratingList.append(avg_rating)
		else:
			ratingList.append("No Ratings")
		modules.append(ratingList)
	context_dict['modules'] = modules
	return render_to_response('ratethiscourse/course.html', context_dict, context)
	
def module(request, uni_name_url, course_name_url, module_name_url):
	
	context = RequestContext(request)
	module_name = module_name_url.replace('_', ' ')
	course_name = course_name_url.replace('_', ' ')
	uni_name = uni_name_url.replace('_', ' ')
	context_dict = {'uni_name': uni_name, 'course_name': course_name, 'module_name': module_name, 'uni_name_url': uni_name_url, 'course_name_url': course_name_url, 'module_name_url': module_name_url}
	
	uni = University.objects.get(name=uni_name)
	course = Course.objects.get(name=course_name, university=uni)
	module = Module.objects.get(name=module_name, course=course, university=uni)
	context_dict['module'] = module
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
		auth = str(userprofile.course) == course_name
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
				comment.module = module
				comment.save()
			else:
				print commentform.errors
		
		if ratingform.data.has_key('value'):
			if ratingform.is_valid():
				rating = ratingform.save(commit=False)
				rating.module = module
				rating.save()
			else:
				print ratingform.errors

	else:
		commentform = CommentForm()
		ratingform = RatingForm()
	
	comments = Comment.objects.filter(module=module)
	context_dict['comments'] = comments
	
	ratings = Rating.objects.filter(module=module)
	if len(ratings) > 0:
		avg_rating = 0.0
		i = 0
		for rating in ratings:
			avg_rating = avg_rating + int(str(rating))
			i = i+1
		avg_rating = avg_rating/i
		context_dict['rating'] = avg_rating
	else:
		context_dict['rating'] = "No Ratings"
	
	context_dict['comment_form'] = commentform
	context_dict['rating_form'] = ratingform
	return render_to_response('ratethiscourse/module.html', context_dict, context)
	
def add_course(request):
	
	context = RequestContext(request)
	context_dict = {}
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
		
	if request.method == 'POST':

		name = request.POST['name']
		university = request.POST['university']
		
		courseform = CourseForm(request.POST)
		
		if courseform.is_valid():
			course = courseform.save()
			context_dict['name'] = name
		else:
			print courseform.errors
	else:
		context_dict['name'] = 'NotPosted'
		courseform = CourseForm()
		
	context_dict['courseform'] = courseform
	return render_to_response('ratethiscourse/add_course.html', context_dict, context)
	
def add_module(request):
	
	context = RequestContext(request)
	context_dict = {}
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
	
	if request.method == 'POST':

		name = request.POST['name']
		university = request.POST['university']
		course = request.POST['course']
		
		moduleform = ModuleForm(request.POST)
		
		if moduleform.is_valid():
			module = moduleform.save()
			context_dict['name'] = name
		else:
			print moduleform.errors
	else:
		context_dict['name'] = 'NotPosted'
		moduleform = ModuleForm()
		
	context_dict['moduleform'] = moduleform
	return render_to_response('ratethiscourse/add_module.html', context_dict, context)    

def change_course(request):
	
	context = RequestContext(request)
	context_dict = {}
	
	user = request.user
	if not user.is_anonymous():
		userprofile = UserProfile.objects.get(user=user)
		context_dict['userprofile'] = userprofile
	
	if request.method == 'POST':
		context_dict['posted'] = True
		userprofileform = UserProfileForm(request.POST)
		
		if userprofileform.is_valid():
			user = request.user
			userprofile.course = userprofileform.cleaned_data['course']
			userprofile.save()
			context_dict['success'] = True
		else:
			context_dict['success'] = False
			print userprofileform.errors
	
	else:
		context_dict['posted'] = False
		userprofileform = UserProfileForm()
	
	context_dict['userprofileform'] = userprofileform
	return render_to_response('ratethiscourse/change_course.html', context_dict, context)
		

def get_courses(request):
	
	context = RequestContext(request)
	university_id = None
	
	if request.method == 'GET':
		university_id = request.GET['university_id']
		
	courses = [["", "---------"]]
	
	if university_id:
		for course in Course.objects.filter(university=university_id).values('id', 'name'):
			courses.append([course['id'], course['name']])
		
	return HttpResponse(json.dumps(courses), content_type="application/json")
	
def get_user_uni(request):
	context = RequestContext(request)
	
	university_id = None
	university = None
	
	if request.method == 'GET':
		try:
			user = request.user
			user_profile = UserProfile.objects.filter(user=user).values('university')
			if (len(user_profile) > 0):
				university_id = user_profile[0]['university']
			else:
				university_id = None
		except (UserProfile.DoesNotExist) as e:
			university_id = None
	
	if university_id:
		university_id = str(university_id)
	else:
		university_id = ""
		
	return HttpResponse(university_id)

def get_user_course(request):
	context = RequestContext(request)
	
	course_id = None
	course = None
	
	if request.method == 'GET':
		user = request.user
		if not user.is_anonymous():
			user = request.user
			user_profile = UserProfile.objects.filter(user=user).values('course')
			if (len(user_profile) > 0):
				course_id = user_profile[0]['course']
			else:
				course_id = None
		else:
			course_id = None
	
	if course_id:
		course_id = str(course_id)
	else:
		course_id = ""
		
	return HttpResponse(course_id)