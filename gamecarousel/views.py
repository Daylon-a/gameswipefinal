from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import GameData

# Create your views here.

def home(request):
    return render(request, 'splashpage.html')

def mainpage(request):

    selectedgame = GameData.objects.order_by('?')[0:1].get()
    gname = getattr(selectedgame, 'gname', 'Not Found')
    gdescription = getattr(selectedgame, 'description', 'No Description Found')
    
    secondselectedgame = GameData.objects.order_by('?')[1:2].get()
    secondgname = getattr(secondselectedgame, 'gname', 'Not Found')
    secondgdescription = getattr(secondselectedgame, 'description', 'No Description Found')

    thirdselectedgame = GameData.objects.order_by('?')[2:3].get()
    thirdgname = getattr(thirdselectedgame, 'gname', 'Not Found')
    thirdgdescription = getattr(thirdselectedgame, 'description', 'No Description Found')

    fourthselectedgame = GameData.objects.order_by('?')[3:4].get()
    fourthgname = getattr(fourthselectedgame, 'gname', 'Not Found')
    fourthgdescription = getattr(fourthselectedgame, 'description', 'No Description Found')
    

    return render(request, 'mainpage.html', 
    {'selectedgame': selectedgame, 
    'gname': gname, 
    'gdescription': gdescription, 
    'user': 'Daylon',
    'secondselectedgame': secondselectedgame,
    'secondgname': secondgname,
    'secondgdescription': secondgdescription,
    'thirdselectedgame': thirdselectedgame,
    'thirdgname': thirdgname,
    'thirdgdescription': thirdgdescription,
    'fourthselectedgame': fourthselectedgame,
    'fourthgname': fourthgname,
    'fourthgdescription': fourthgdescription})