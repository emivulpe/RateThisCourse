from ratethiscourse.models import Course, Rating, Module

def getRecentRows(context_dict, table, context_dict_label, rowCount):
	""" Gets rowCount most recent entries to table and adds to context_dict
		a list labeled by context_dict_label containing a list of lists with
		each inner list being [<row of the ratings>, <university name(for urls)>, <course name(for urls)>, <module name(for urls)>]
	"""
	rows = table.objects.all().order_by('-date')[:rowCount]
	result = []
	for row in rows:
		info = [row]
		module = Module.objects.get(id=row.module.id)
		info.append(str(module.university).replace(' ', '_'))
		info.append(str(module.course).replace(' ', '_'))
		info.append(str(row.module).replace(' ', '_'))
		result.append(info)
			
	context_dict[context_dict_label] = result
	
def getAllCourseRatings():
	""" Gets the ratings of all courses in the db
		
		Returns:
			a list of lists with each inner list being
			[<course object>, <course rating>, <uni name(for urls)>, <course name(for urls)>]
			Or "No ratings" if there are no modules in the course
	"""
	courses = Course.objects.all()
	ratedCourses = []
	for course in courses:
		ratedCourse = [course]
		course_rating = 0
		j = 0
		courseRatings = getCourseRatings(course.university, course)
		if not isinstance(courseRatings, str):
			for courseRating in courseRatings:
				if isinstance(courseRating[2], str):
					continue
				else:
					course_rating = course_rating + courseRating[2]
					j = j + 1
			if j>0:
				course_rating = course_rating/j
			else:
				course_rating = "No ratings"
				
			ratedCourse.append(course_rating)
			ratedCourse.append(str(course.university).replace(' ', '_'))
			ratedCourse.append(str(course).replace(' ', '_'))
			ratedCourses.append(ratedCourse)
	return ratedCourses
	
def getUniCourseRatings(uni):
	""" Gets the ratings of all courses in the uni
		
		Returns:
			a list of lists with each inner list being
			[<course object>, <course name(for urls)>, <course rating>]
			Or "No ratings" if there are no modules in the course
	"""
	courses = Course.objects.filter(university=uni)
	courses = Course.objects.all()
	ratedCourses = []
	for course in courses:
		ratedCourse = [course]
		course_rating = 0
		j = 0
		courseRatings = getCourseRatings(course.university, course)
		if not isinstance(courseRatings, str):
			for courseRating in courseRatings:
				if isinstance(courseRating[2], str):
					continue
				else:
					course_rating = course_rating + courseRating[2]
					j = j + 1
			if j>0:
				course_rating = course_rating/j
			else:
				course_rating = "No ratings"
				
			ratedCourse.append(str(course).replace(' ', '_'))
			ratedCourse.append(course_rating)
			ratedCourses.append(ratedCourse)
	return ratedCourses

def getCourseRatings(uni, course):
	""" Gets the ratings of all modules in the course at the uni.
	
		Returns:
			a list of lists with each inner list being
			[<module name>, <module name(for urls)>, <module rating>]
			Or "No ratings" if there are no modules in the course
	"""
	modules = Module.objects.filter(university=uni, course=course)
	moduleRatings = []
	if len(modules) > 0:
		for module in modules:
			ratingList = [str(module)]
			ratingList.append(str(module).replace(' ', '_'))
			ratingList.append(getModuleRating(module))
			moduleRatings.append(ratingList)
		return moduleRatings
	else:
		return "No ratings"

def getModuleRating(module):
	""" Gets the average rating of the module.
		
		Returns:
			the average rating
			Or "No ratings" if the module has no ratings
	"""
	ratings = Rating.objects.filter(module=module)
	if len(ratings) > 0:
		avg_rating = 0.0
		i = 0
		for rating in ratings:
			avg_rating = avg_rating + int(str(rating))
			i = i+1
		avg_rating = avg_rating/i
		return avg_rating
	else:
		return "No ratings"