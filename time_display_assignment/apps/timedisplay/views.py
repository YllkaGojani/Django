from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
	date = datetime.datetime.now().date()
	time = datetime.datetime.now().time()
	data = {
		'someValue' : 'The current time and date:',
		'date' : date,
		'time' : time
	}
	return render(request, 'timedisplay/index.html', data)