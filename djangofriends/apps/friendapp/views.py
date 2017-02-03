from django.shortcuts import render
from . import models
from django.db.models import Q
# Create your views here.
def index(req):
    # users =models.Users.objects.all()

# 1    
    # users = models.Users.objects.all().filter(last_name = "Rodriguez")

# 2
    # users = models.Users.objects.all().exclude(last_name = "Rodriguez")

# 3
    # users = models.Users.objects.all().filter(last_name = "Rodriguez") | models.Users.objects.all().filter(first_name = "Daniel")

# 4
    # users = models.Users.objects.all().filter(last_name = "Rodriguez").exclude(first_name = "Madison")
  
# 5
    # users = models.Users.objects.all().exclude(first_name = "Daniel") | models.Users.objects.all().exclude(first_name = "Michael")

# 6 AttributeError: 'Users' object has no attribute 'query'
	# users = models.Users.objects.get(id=1)


# 7	MultipleObjectsReturned: get() returned more than one Users -- it returned 3!
	# users = models.Users.objects.get(last_name = "Rodriguez")

# 8	DoesNotExist: Users matching query does not exist.
	# users =  models.Users.objects.get(id=10000)	

# 9
	# users = models.Users.objects.all().order_by('first_name')

# 10
	# users = models.Users.objects.all().order_by('-last_name')
	# print users.query
	# print users
	# context = {'users':users}     
	# return render(req, "friendapp/index.html",context)

# We are briefly going to touch the Friendships model.

# 11
	# friendships = models.Friendships.objects.all()
	# for friend in friendships:
	# 	print friend

# 12
	# user = models.Users.objects.get(id=4)	
	# print user.first_name
	# friendships = models.Friendships.objects.filter(user = user)
	# for friend in friendships:
	# 	print friend.friend.first_name	

# 13
	# user = models.Users.objects.get(id=4)	
	# print user.first_name
	# friendships = models.Friendships.objects.filter(friend = user)
	# for friend in friendships:
	# 	print friend.user.first_name

# 14
#     exclude_users = models.Users.objects.filter(id__in = [4,5,6])
#     friendships = models.Friendships.objects.exclude(user__in=exclude_users)
#     friend = dict()
#     for f in friendships:
#         if f.user not in exclude_users:
#             friend[f.user.id] = f.user
#     print friend
#     print friendships
#     context = {'friendships':friendships}
#     return render(req, "friendapp/index.html",context)	



# ====== FRIENDSHIPS II ======

# 1
	# friend = models.Friendships.objects.all()
	# print friend.query

# 2
	# friend = models.Friendships.objects.filter(user__first_name='Michael')
	# print friend.query

# 3
	# friend = models.Friendships.objects.exclude(user__first_name='Daniel')
	# print friend.query

# 4
	# friend = models.Friendships.objects.filter(user__id=1) | models.Friendships.objects.filter(user__last_name='Hernandez')
	# print friend.query

# 5
	# friend = models.Friendships.objects.order_by('friend__first_name').distinct()
	# print friend.query
	# context = {'friendships' : friend}

# 6,7
	# users = models.Users.objects.filter(usersfriend__friend__id=2)
	# print (users.query)

# 8
	users = models.Users.objects.filter(usersfriend__friend__id=1) | models.Users.objects.filter(usersfriend__friend__last_name='Hernandez') 
	context = {'users' : users}
	return render(req, "friendapp/index.html", context)
