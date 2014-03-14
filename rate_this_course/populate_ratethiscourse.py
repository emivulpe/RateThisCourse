import os
from random import randint

def populate():
    ## GLASGOW UNI
    glasgow_university = add_university(name = "University of Glasgow", location = "Glasgow", uni_domain_code = "gla")


    ## COMPUTING SCIENCE
    computing_science = add_course(university = glasgow_university,
        name = "Computing Science")
    
    dim = add_module(university = glasgow_university,
        course = computing_science,
        name = "DIM",
        year = 3,
	lecturer = "Leif")

    psd = add_module(university = glasgow_university,
        course = computing_science,
        name = "PSD",
        year = 3,
	lecturer = "Jeremy")


    db = add_module(university = glasgow_university,
        course = computing_science,
        name = "DB",
        year = 3,
	lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)
    
    
    ## PSYCHOLOGY
    psychology = add_course(university = glasgow_university,
        name = "Psychology")
    
    dim = add_module(university = glasgow_university,
        course = psychology,
        name = "DIM",
        year = 3,
    lecturer = "Leif")

    psd = add_module(university = glasgow_university,
        course = psychology,
        name = "PSD",
        year = 3,
    lecturer = "Jeremy")


    db = add_module(university = glasgow_university,
        course = psychology,
        name = "DB",
        year = 3,
    lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)
        
        
    ## BUSINESS
    BUSINESS = add_course(university = glasgow_university,
        name = "Business")
    
    dim = add_module(university = glasgow_university,
        course = BUSINESS,
        name = "DIM",
        year = 3,
    lecturer = "Leif")

    psd = add_module(university = glasgow_university,
        course = BUSINESS,
        name = "PSD",
        year = 3,
    lecturer = "Jeremy")


    db = add_module(university = glasgow_university,
        course = BUSINESS,
        name = "DB",
        year = 3,
    lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)


    ## Maths
    Maths = add_course(university = glasgow_university,
        name = "Maths")
    
    dim = add_module(university = glasgow_university,
        course = Maths,
        name = "DIM",
        year = 3,
    lecturer = "Leif")

    psd = add_module(university = glasgow_university,
        course = Maths,
        name = "PSD",
        year = 3,
    lecturer = "Jeremy")


    db = add_module(university = glasgow_university,
        course = Maths,
        name = "DB",
        year = 3,
    lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)
        


    ## STRATHCLYDE UNI
    strathclyde_university = add_university(name = "University of Strathclyde", location = "Glasgow", uni_domain_code = "strath")


    ## COMPUTING SCIENCE
    computing_science = add_course(university = strathclyde_university,
        name = "Computing Science")
    
    dim = add_module(university = strathclyde_university,
        course = computing_science,
        name = "DIM",
        year = 3,
    lecturer = "Leif")

    psd = add_module(university = strathclyde_university,
        course = computing_science,
        name = "PSD",
        year = 3,
    lecturer = "Jeremy")


    db = add_module(university = strathclyde_university,
        course = computing_science,
        name = "DB",
        year = 3,
    lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)
    
    
    ## PSYCHOLOGY
    psychology = add_course(university = strathclyde_university,
        name = "Psychology")
    
    dim = add_module(university = strathclyde_university,
        course = psychology,
        name = "DIM",
        year = 3,
    lecturer = "Leif")

    psd = add_module(university = strathclyde_university,
        course = psychology,
        name = "PSD",
        year = 3,
    lecturer = "Jeremy")


    db = add_module(university = strathclyde_university,
        course = psychology,
        name = "DB",
        year = 3,
    lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)
        
    
    ## BUSINESS
    BUSINESS = add_course(university = strathclyde_university,
        name = "Business")
    
    dim = add_module(university = strathclyde_university,
        course = BUSINESS,
        name = "DIM",
        year = 3,
    lecturer = "Leif")

    psd = add_module(university = strathclyde_university,
        course = BUSINESS,
        name = "PSD",
        year = 3,
    lecturer = "Jeremy")


    db = add_module(university = strathclyde_university,
        course = BUSINESS,
        name = "DB",
        year = 3,
    lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)


    ## Maths
    Maths = add_course(university = strathclyde_university,
        name = "Maths")
    
    dim = add_module(university = strathclyde_university,
        course = Maths,
        name = "DIM",
        year = 3,
    lecturer = "Leif")

    psd = add_module(university = strathclyde_university,
        course = Maths,
        name = "PSD",
        year = 3,
    lecturer = "Jeremy")


    db = add_module(university = strathclyde_university,
        course = Maths,
        name = "DB",
        year = 3,
    lecturer = "Iadh")

    add_comment(message = "Very good course. Love the lecturer", module  = dim)
    add_comment(message = "Fun course!", module  = dim)
    add_comment(message = "It's very good and entertaining", module  = dim)
    add_comment(message = "I really like this course", module  = dim)
    add_comment(message = "Learning lots in this module!", module  = dim)
    add_comment(message = "Django is amazing!", module  = dim)
    
    add_comment(message = "Very good course. Love the lecturer", module  = psd)
    add_comment(message = "Fun course!", module  = psd)
    add_comment(message = "It's very good and entertaining", module  = psd)
    add_comment(message = "I really like this course", module  = psd)
    add_comment(message = "Learning lots in this module!", module  = psd)
    add_comment(message = "Django is amazing!", module  = psd)
    
    add_comment(message = "Very good course. Love the lecturer", module  = db)
    add_comment(message = "Fun course!", module  = db)
    add_comment(message = "It's very good and entertaining", module  = db)
    add_comment(message = "I really like this course", module  = db)
    add_comment(message = "Learning lots in this module!", module  = db)
    add_comment(message = "Django is amazing!", module  = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, module = psd)


    # Print out what we have added to the user.
    for u in University.objects.all():
        for c in Course.objects.filter(university=u):
            for m in Module.objects.filter(course=c, university=u):
                print "-{0} -{1} -{2}".format(str(u), str(c), str(m))

def add_module(university, course, name, year, lecturer):
    m = Module.objects.get_or_create(university = university, course = course, name = name, year = year, lecturer = lecturer)[0]
    return m

def add_course(university, name):
    c = Course.objects.get_or_create(university = university, name = name)[0]
    return c

def add_university(name, location, uni_domain_code):
    u = University.objects.get_or_create(name = name, location = location, uni_domain_code=uni_domain_code)[0]
    return u

def add_comment(message, module):
    com = Comment.objects.get_or_create(message = message, module = module)[0]
    return com


def add_rating(value, module):
    r = Rating.objects.get_or_create(value = value, module = module)[0]
    return r

# Start execution here!
if __name__ == '__main__':
    print "Starting Ratemycourse population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_this_course.settings')
    from ratethiscourse.models import University, Course, Module, Rating, Comment 
    populate()
