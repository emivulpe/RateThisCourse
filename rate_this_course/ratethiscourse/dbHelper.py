from ratethiscourse.models import Degree, Rating, Course

def getRecentRows(context_dict, table, context_dict_label, rowCount):
	""" Gets rowCount most recent entries to table and adds to context_dict
		a list labeled by context_dict_label containing a list of lists with
		each inner list being [<row of the ratings>, <university name(for urls)>, <degree name(for urls)>, <course name(for urls)>]
	"""
	rows = table.objects.all().order_by('-date')[:rowCount]
	result = []
	for row in rows:
		info = [row]
		course = Course.objects.get(id=row.course.id)
		info.append(str(course.university).replace(' ', '_'))
		info.append(str(course.degree).replace(' ', '_'))
		info.append(str(row.course).replace(' ', '_'))
		result.append(info)
			
	context_dict[context_dict_label] = result
	
def getAllDegreeRatings():
	""" Gets the ratings of all degrees in the db
		
		Returns:
			a list of lists with each inner list being
			[<degree object>, <degree rating>, <uni name(for urls)>, <degree name(for urls)>]
			Or "No ratings" if there are no courses in the degree
	"""
	degrees = Degree.objects.all()
	ratedDegrees = []
	for degree in degrees:
		rateddegree = [degree]
		degree_rating = 0
		j = 0
		degreeRatings = getDegreeRatings(degree.university, degree)
		if not isinstance(degreeRatings, str):
			for degreeRating in degreeRatings:
				if isinstance(degreeRating[2], str):
					continue
				else:
					degree_rating = degree_rating + degreeRating[2]
					j = j + 1
			if j>0:
				degree_rating = degree_rating/j
			else:
				degree_rating = "No Ratings"
				
			rateddegree.append(degree_rating)
			rateddegree.append(str(degree.university).replace(' ', '_'))
			rateddegree.append(str(degree).replace(' ', '_'))
			ratedDegrees.append(rateddegree)
	return ratedDegrees
	
def getUniDegreeRatings(uni):
	""" Gets the ratings of all degrees in the uni
		
		Returns:
			a list of lists with each inner list being
			[<degree object>, <degree name(for urls)>, <degree rating>]
			Or "No ratings" if there are no courses in the degree
	"""
	degrees = Degree.objects.filter(university=uni)
	ratedDegrees = []
	for degree in degrees:
		print degree
		rateddegree = [degree]
		degree_rating = 0
		j = 0
		degreeRatings = getDegreeRatings(degree.university, degree)
		if not isinstance(degreeRatings, str):
			for degreeRating in degreeRatings:
				if isinstance(degreeRating[2], str):
					continue
				else:
					degree_rating = degree_rating + degreeRating[2]
					j = j + 1
			if j>0:
				degree_rating = degree_rating/j
			else:
				degree_rating = "No Ratings"
		else:
			degree_rating = "No Ratings"		
		rateddegree.append(str(degree).replace(' ', '_'))
		rateddegree.append(degree_rating)
		ratedDegrees.append(rateddegree)
	return ratedDegrees

def getDegreeRatings(uni, degree):
	""" Gets the ratings of all courses in the degree at the uni.
	
		Returns:
			a list of lists with each inner list being
			[<course name>, <course name(for urls)>, <course rating>]
			Or "No ratings" if there are no courses in the degree
	"""
	courses = Course.objects.filter(university=uni, degree=degree)
	courseRatings = []
	if len(courses) > 0:
		for course in courses:
			ratingList = [str(course)]
			ratingList.append(str(course).replace(' ', '_'))
			ratingList.append(getCourseRating(course))
			courseRatings.append(ratingList)
		return courseRatings
	else:
		return "No Ratings"

def getCourseRating(course):
	""" Gets the average rating of the course.
		
		Returns:
			the average rating
			Or "No ratings" if the course has no ratings
	"""
	ratings = Rating.objects.filter(course=course)
	if len(ratings) > 0:
		avg_rating = 0.0
		i = 0
		for rating in ratings:
			avg_rating = avg_rating + int(str(rating))
			i = i+1
		avg_rating = avg_rating/i
		return avg_rating
	else:
		return "No Ratings"