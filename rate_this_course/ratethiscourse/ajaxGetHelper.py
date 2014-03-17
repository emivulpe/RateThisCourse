from ratethiscourse.models import UserProfile

def getUserData(request, filter):
	"""	Gets the id from the UserProfile table using the filter to get a specific value
		
		Returns:
			the id
	"""
	requested_id = None
	
	if request.method == 'GET':
		user = request.user
		if not user.is_anonymous():
			user = request.user
			user_profile = UserProfile.objects.filter(user=user).values(filter)
			if (len(user_profile) > 0):
				requested_id = user_profile[0][filter]
			else:
				requested_id = None
		else:
			requested_id = None
	
	if requested_id:
		requested_id = str(requested_id)
	else:
		requested_id = ""
	
	return requested_id