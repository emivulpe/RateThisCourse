import os
from random import randint

def populate():
    ## GLASGOW UNI
    glasgow_university = add_university(name = "University of Glasgow", location = "Glasgow", uni_domain_code = "gla", description="The University of Glasgow is the fourth-oldest university in the English-speaking world and one of Scotland's four ancient universities.")


    ## COMPUTING SCIENCE
    computing_science = add_degree(university = glasgow_university,
        name = "Computing Science")
    
    dim = add_course(university = glasgow_university,
        degree = computing_science,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
	lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = glasgow_university,
        degree = computing_science,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
	lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = glasgow_university,
        degree = computing_science,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
	lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)
    
    
    ## PSYCHOLOGY
    psychology = add_degree(university = glasgow_university,
        name = "Psychology")
    
    dim = add_course(university = glasgow_university,
        degree = psychology,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
    lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = glasgow_university,
        degree = psychology,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
    lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = glasgow_university,
        degree = psychology,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
    lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)
        
        
    ## BUSINESS
    BUSINESS = add_degree(university = glasgow_university,
        name = "Business")
    
    dim = add_course(university = glasgow_university,
        degree = BUSINESS,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
    lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = glasgow_university,
        degree = BUSINESS,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
    lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = glasgow_university,
        degree = BUSINESS,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
    lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)


    ## Maths
    Maths = add_degree(university = glasgow_university,
        name = "Maths")
    
    dim = add_course(university = glasgow_university,
        degree = Maths,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
    lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = glasgow_university,
        degree = Maths,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
    lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = glasgow_university,
        degree = Maths,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
    lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)
        


    ## STRATHCLYDE UNI
    strathclyde_university = add_university(name = "University of Strathclyde", location = "Glasgow", uni_domain_code = "strath", description="The University of Strathclyde is a Scottish public research university located in Glasgow, Scotland. It is Glasgow's second university by age, being founded in 1796 as the Andersonian Institute, and receiving its Royal Charter in 1964 as the UK's first technological university. It takes its name from the historic Kingdom of Strathclyde.")


    ## COMPUTING SCIENCE
    computing_science = add_degree(university = strathclyde_university,
        name = "Computing Science")
    
    dim = add_course(university = strathclyde_university,
        degree = computing_science,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
    lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = strathclyde_university,
        degree = computing_science,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
    lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = strathclyde_university,
        degree = computing_science,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
    lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)
    
    
    ## PSYCHOLOGY
    psychology = add_degree(university = strathclyde_university,
        name = "Psychology")
    
    dim = add_course(university = strathclyde_university,
        degree = psychology,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
    lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = strathclyde_university,
        degree = psychology,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
    lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = strathclyde_university,
        degree = psychology,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
    lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)
        
    
    ## BUSINESS
    BUSINESS = add_degree(university = strathclyde_university,
        name = "Business")
    
    dim = add_course(university = strathclyde_university,
        degree = BUSINESS,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
    lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = strathclyde_university,
        degree = BUSINESS,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
    lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = strathclyde_university,
        degree = BUSINESS,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
    lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)


    ## Maths
    Maths = add_degree(university = strathclyde_university,
        name = "Maths")
    
    dim = add_course(university = strathclyde_university,
        degree = Maths,
        code = "DIM3",
        name = "Distributed Information Management",
        year = 3,
    lecturer = "Leif",
    description = "A course designed to teach you django or something")

    psd = add_course(university = strathclyde_university,
        degree = Maths,
        code = "PSD3",
        name = "Professional Software Development 3",
        year = 3,
    lecturer = "Jeremy",
    description = "A cours teaching you about theory and practices of software development and the software development lifecycle.")


    db = add_course(university = strathclyde_university,
        degree = Maths,
        code = "DB3",
        name = "Database Systems 3",
        year = 3,
    lecturer = "Iadh",
    description = "A course about advanced SQL techniques as well as using api's like JDBC to communicate with databases in application code.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    
    add_comment(message = "Very good course. Love the lecturer", course = psd)
    add_comment(message = "Fun course!", course = psd)
    add_comment(message = "It's very good and entertaining", course = psd)
    add_comment(message = "I really like this course", course = psd)
    add_comment(message = "Learning lots in this module!", course = psd)
    add_comment(message = "Django is amazing!", course = psd)
    
    add_comment(message = "Very good course. Love the lecturer", course = db)
    add_comment(message = "Fun course!", course = db)
    add_comment(message = "It's very good and entertaining", course = db)
    add_comment(message = "I really like this course", course = db)
    add_comment(message = "Learning lots in this module!", course = db)
    add_comment(message = "Django is amazing!", course = db)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(10):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)


    # Print out what we have added to the user.
    for u in University.objects.all():
        for d in Degree.objects.filter(university=u):
            for c in Course.objects.filter(degree=d, university=u):
                print "-{0} -{1} -{2}".format(str(u), str(d), str(c))

def add_course(university, code, degree, name, year, lecturer, description):
    m = Course.objects.get_or_create(university = university, code = code, degree = degree, name = name, year = year, lecturer = lecturer, description = description)[0]
    return m

def add_degree(university, name):
    c = Degree.objects.get_or_create(university = university, name = name)[0]
    return c

def add_university(name, location, uni_domain_code, description):
    u = University.objects.get_or_create(name = name, location = location, uni_domain_code=uni_domain_code, description=description)[0]
    return u

def add_comment(message, course):
    com = Comment.objects.get_or_create(message = message, course = course)[0]
    return com


def add_rating(value, course):
    r = Rating.objects.get_or_create(value = value, course = course)[0]
    return r

# Start execution here!
if __name__ == '__main__':
    print "Starting Ratemycourse population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_this_course.settings')
    from ratethiscourse.models import University, Degree, Course, Rating, Comment 
    populate()
