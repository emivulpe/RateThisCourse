from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response 
from ratethiscourse.models import Course, University, Rating, Comment, Module, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from ratethiscourse.forms import UserForm, UserProfileForm, RatingForm, CommentForm, CourseForm, ModuleForm, LoginForm


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
	context_dict['ratings'] = ratings;
	
	comments = Comment.objects.all().order_by('-date')[:10]
	context_dict['comments'] = comments;
	
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
			ratedCourses.append(ratedCourse)
	ratedCourses.sort()
	topFive = ratedCourses[:5]
	bottomFive = ratedCourses[-1:-6]
	
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
			profile.user=user
			profile.save()

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
	print context_dict
	
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
	try:
		user = User.objects.get(username=request.user.get_username())
		user_profile = UserProfile.objects.get(user=user)
		auth = str(user_profile.course) == course_name
		context_dict['auth'] = auth
	except (UserProfile.DoesNotExist, AttributeError) as e:
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
