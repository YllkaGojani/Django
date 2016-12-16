from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'disappear/index.html')

def ninjas(request, color):
    result ={}
    if color == "":
        result = {'ninja': 'all'}
    else:
        ninjas = {
        	'purple':'donatello',
        	'blue':'leonardo',
        	'orange':'michelangelo',
        	'red':'raphael'
        }
        if color in ninjas:
            result['ninja'] = ninjas[color]
        else:
            result['ninja'] = 'notapril'
    return render(request, 'disappear/ninjas.html', result)	