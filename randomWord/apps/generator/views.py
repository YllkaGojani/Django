from django.shortcuts import render,redirect
import string
import random

# Create your views here.
def index(request):
	return render(request,'generator/index.html')

#chars concatenates uppercase letters and digits
def generator(size = 14,chars = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))	

word = generator()

def random(request):


	if request.method == 'POST':
		try:
			request.session['num']
		except:
			request.session['num'] = 0
		request.session['num'] += 1			
		request.session['word'] = word
		return redirect('/')
	else:
		return redirect('/')
