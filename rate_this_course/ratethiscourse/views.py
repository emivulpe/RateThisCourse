from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# Import the Category Model
from ratethiscourse.models import Course
from ratethiscourse.models import University

	
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
    return render_to_response('./university.html', context_dict, context)


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
