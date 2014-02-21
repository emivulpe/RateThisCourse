import os

def populate():
    glasgow_university = add_university(name = "University of Glasgow", location = "Glasgow")

    add_course(university=glasgow_university,
        name="DIM",
        year = 3,
	lecturer = "Leif")

    add_course(university=glasgow_university,
        name="PSD",
        year = 3,
	lecturer = "Jeremy")


    add_course(university=glasgow_university,
        name="DB",
        year = 3,
	lecturer = "Iadh")



    strathclyde_university = add_university(name = "University of Strathclyde", location = "Glasgow")

    management = add_course(university=strathclyde_university,
        name="Management",
        year = 1,
	lecturer = "Tores")

    add_course(university=strathclyde_university,
        name="Marketing",
        year = 1,
	lecturer = "Jean")


    add_course(university=strathclyde_university,
        name="Psychology",
        year = 1,
	lecturer = "John")


    add_comment(message="Very good course. Love the lecturer", course  = management)
    add_rating(value = 5, course = management)


    # Print out what we have added to the user.
    for u in University.objects.all():
        for c in Course.objects.filter(university=u):
            print "- {0} - {1}".format(str(u), str(c))

def add_course(university, name, year, lecturer):
    c = Course.objects.get_or_create(university=university, name=name,year = year, lecturer = lecturer)[0]
    return c

def add_university(name,location):
    u = University.objects.get_or_create(name=name,location=location)[0]
    return u

def add_comment(message,course):
    com = Comment.objects.get_or_create(message = message, course = course)[0]
    return com


def add_rating(value,course):
    r = Rating.objects.get_or_create(value=value,course = course)[0]
    return r

# Start execution here!
if __name__ == '__main__':
    print "Starting Ratemycourse population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_this_course.settings')
    from ratethiscourse.models import University, Course, Rating, Comment
    populate()
