from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import GameData
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'splashpage.html')

def mainpage(request):

    print('enter if statement')
    if request.method == 'GET':
        print('the get request was followed successfully!')
        username = request.user.get_username()

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
        'username': username,
        'secondselectedgame': secondselectedgame,
        'secondgname': secondgname,
        'secondgdescription': secondgdescription,
        'thirdselectedgame': thirdselectedgame,
        'thirdgname': thirdgname,
        'thirdgdescription': thirdgdescription,
        'fourthselectedgame': fourthselectedgame,
        'fourthgname': fourthgname,
        'fourthgdescription': fourthgdescription})
    
    else:
        print('the post request was not followed successfully')