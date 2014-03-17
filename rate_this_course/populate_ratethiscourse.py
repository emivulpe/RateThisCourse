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
        code = "COMPSCI4048",
        name = "Distributed Information Management",
        year = 3,
	lecturer = "Leif",
    description = "The aims of the course are to:\
            introduce students to modern software development methods and techniques for building and maintaining large systems\
            provide an opportunity for the students to apply these methods and techniques presented to them in the context of an extended group-based software development exercise\
            make the students aware of the professional, social and ethical dimensions of software development.\
            instil in the students a professional attitude towards software development.")

    psd = add_course(university = glasgow_university,
        degree = computing_science,
        code = "COMPSCI4015",
        name = "Professional Software Development 3",
        year = 3,
	lecturer = "Jeremy",
    description = "The aim of this course is to provide students with a comprehensive overview of web application development. It will provide students with the skills to design and development distributed web applications in a disciplined manner, and strengthen their understanding of the context and rationale of distributed systems.")


    db = add_course(university = glasgow_university,
        degree = computing_science,
        code = "COMPSCI4013",
        name = "Database Systems 3",
        year = 3,
	lecturer = "Iadh",
    description = "From the basic skills derived in Information Management 2, to develop the software engineering and database administration skills required for designing, creating, running and developing a relational database application and its associated application software suite. This will include extension of pre-existing systems and arrangements for extending operational systems;\
            Understanding of how conventional programming languages interact with databases;\
            Understanding of the fundamental concepts, theories and methods of the relational data model;\
            Introduction to Information Retrieval concepts and techniques.")

    add_comment(message = "Very good course. Love the lecturer", course = dim)
    add_comment(message = "Fun course!", course = dim)
    add_comment(message = "WEBDEV IS 2 HARD", course = dim)
    add_comment(message = "It's very good and entertaining", course = dim)
    add_comment(message = "I really like this course", course = dim)
    add_comment(message = "Learning lots in this module!", course = dim)
    add_comment(message = "Django is amazing!", course = dim)
    add_comment(message = "Django; literally the best!", course = dim)
    add_comment(message = "Learn some useful stuff in this course and the lectures are a blast", course = dim)
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = dim)
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = db)
        
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = psd)
    
    
    ## PSYCHOLOGY
    psychology = add_degree(university = glasgow_university,
        name = "Psychology")
    
    psych2b = add_course(university = glasgow_university,
        degree = psychology,
        code = "PSYCH2011",
        name = "Psychology 2B",
        year = 2,
    lecturer = "Bill",
    description = "The aim is to broaden and, especially, to deepen knowledge of the subject area by building on the foundations laid in Psychology 1A, 1B, 2A.")

    psych2a = add_course(university = glasgow_university,
        degree = psychology,
        code = "PSYCH2010",
        name = "Psychology 2A",
        year = 2,
    lecturer = "Bob",
    description = "The aim is to broaden and, especially, to deepen knowledge of the subject area by building on the foundations laid in Psychology 1A and 1B")


    psych1b = add_course(university = glasgow_university,
        degree = psychology,
        code = "PSYCH1002",
        name = "Psychology 1B: Social, Developmental and Individual Differences",
        year = 1,
    lecturer = "Ben",
    description = "The aim is to introduce students to core material in the area of social and developmental psychology and individual differences")
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = psych1b)
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = psych2a)
        
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = psych2b)
        
        
    ## LAW
    LAW = add_degree(university = glasgow_university,
        name = "Law")
    
    buslaw = add_course(university = glasgow_university,
        degree = LAW,
        code = "LAW1001",
        name = "Business Law",
        year = 1,
    lecturer = "Amanda",
    description = "The aim of the course is to provide students with a knowledge of modern Business law in theory and practice.")

    famlaw = add_course(university = glasgow_university,
        degree = LAW,
        code = "LAW1004",
        name = "Family Law",
        year = 1,
    lecturer = "Jerry",
    description = "Family Law is designed to provide a grounding in the key elements of Family Law and to develop certain key skills.")


    busorg = add_course(university = glasgow_university,
        degree = LAW,
        code = "LAW2001",
        name = "Business Organisations",
        year = 2,
    lecturer = "Iadh",
    description = "The aim of the course is to enable students to acquire an understanding of the legal framework for business organisations. The course is structured so as to meet the relevant professional requirements of the Law Society of Scotland.")

    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = buslaw)
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = famlaw)
        
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = busorg)


    ## Maths
    Maths = add_degree(university = glasgow_university,
        name = "Maths")
    
    maths1r = add_course(university = glasgow_university,
        degree = Maths,
        code = "MATHS1001",
        name = "Mathematics 1R",
        year = 1,
    lecturer = "Jim",
    description = "Mathematics 1R is intended to provide a half-year's Mathematics course leading on from the level of SCE Higher Mathematics.")

    maths1s = add_course(university = glasgow_university,
        degree = Maths,
        code = "MATHS1002",
        name = "Mathematics 1S",
        year = 1,
    lecturer = "John",
    description = "Mathematics 1S is intended to build on Mathematics 1R and to provide a further half-year's Mathematics course both for students who intend to specialize in Mathematics and for others.")


    maths1x = add_course(university = glasgow_university,
        degree = Maths,
        code = "MATHS1004",
        name = "Mathematics 1X",
        year = 1,
    lecturer = "Jill",
    description = "To present an interesting level-1 course for well-qualified students which will enhance their mathematical knowledge, insights, skills and enjoyment as well as enhancing the transferable skills of reasoning, handling of abstract concepts, problem solving, communication, and clarity of presentation.")
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = maths1r)
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = maths1s)
        
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = maths1x)
        
    ## Chemistry
    Chemistry = add_degree(university = glasgow_university,
        name = "Chemistry")
    
    orgchem = add_course(university = glasgow_university,
        degree = Chemistry,
        code = "CHEM3012",
        name = "Organic Chemistry 3",
        year = 3,
    lecturer = "Jim",
    description = "Organic Chemistry course for students at level 3")

    inorgchem = add_course(university = glasgow_university,
        degree = Chemistry,
        code = "CHEM3010",
        name = "Inorganic Chemistry 3",
        year = 3,
    lecturer = "John",
    description = "Inorganic Chemistry course for students at level 3")


    chem2x = add_course(university = glasgow_university,
        degree = Chemistry,
        code = "CHEM2001",
        name = "Chemistry 2X",
        year = 2,
    lecturer = "Jill",
    description = "Following on from Chemistry 1, this course covers further topics and consolidates the basic theories of chemistry and develops laboratory and problem-solving skills.")
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = orgchem)
    
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = inorgchem)
        
    for i in range(20):
        rating = randint(1,5)
        add_rating(value = rating, course = chem2x)

        


    ## STRATHCLYDE UNI
    strathclyde_university = add_university(name = "University of Strathclyde", location = "Glasgow", uni_domain_code = "strath", description="The University of Strathclyde is a Scottish public research university located in Glasgow, Scotland. It is Glasgow's second university by age, being founded in 1796 as the Andersonian Institute, and receiving its Royal Charter in 1964 as the UK's first technological university. It takes its name from the historic Kingdom of Strathclyde.")


    ## COMPUTING SCIENCE
    computing_science = add_degree(university = strathclyde_university,
        name = "Computing Science")    
    
    ## PSYCHOLOGY
    psychology = add_degree(university = strathclyde_university,
        name = "Psychology")
        
    ## BUSINESS
    BUSINESS = add_degree(university = strathclyde_university,
        name = "Business")

    ## Maths
    Maths = add_degree(university = strathclyde_university,
        name = "Maths")

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
