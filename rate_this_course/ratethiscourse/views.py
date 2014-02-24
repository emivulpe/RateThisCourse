from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from ratethiscourse.models import Course, University, Rating, Comment
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from ratethiscourse.forms import UserForm, UserProfileForm, RatingForm

	
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

    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        university = University.objects.get(name=uni_name)

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        courses = Course.objects.filter(university=university)

        # Adds our results list to the template context under name pages.
        context_dict['courses'] = courses
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['university'] = university
    except University.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('ratethiscourse/university.html', context_dict, context)


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
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('./index.html', context_dict, context)

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
			user=user_form.save()

			#hash pwd with set_password with the set_password method
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user=user

			#process profile photo if user provides one
			#if 'picture' in request.FILES:
			#	profile.picture = request.FILES['picture']
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

		username = request.POST['username']
		password = request.POST['password']

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
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details provided.")
	else:
		return render_to_response('ratethiscourse/login.html', {}, context)

def user_logout(request):

	#we know user is logged in, we can just logout
	logout(request)

	return HttpResponseRedirect('/ratethiscourse/')		

def course(request, uni_name_url, course_name_url):
    
    context = RequestContext(request)
    course_name = course_name_url.replace('_', ' ')
    uni_name = uni_name_url.replace('_', ' ')
    context_dict = {'uni_name': uni_name, 'course_name': course_name, 'uni_name_url': uni_name_url, 'course_name_url': course_name_url}
    
    course = Course.objects.get(name=course_name)
    
    if request.method == 'POST':
        
        ratingform =  RatingForm(request.POST)
        
        if ratingform.is_valid():
            rating = ratingform.save(commit=False)
            rating.course = course
            rating.save()
        else:
            print ratingform.errors
    
    else:
        ratingform = RatingForm()
    
    ratings = Rating.objects.filter(course=course)
    avg_rating = 0.0
    i = 0
    for rating in ratings:
        avg_rating = avg_rating + int(str(rating))
        i = i+1
    avg_rating = avg_rating/i
    context_dict['rating'] = avg_rating
    
    context_dict['rating_form'] = ratingform
    return render_to_response('ratethiscourse/course.html', context_dict, context)