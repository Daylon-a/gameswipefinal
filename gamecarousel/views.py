from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import GameData
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'splashpage.html')

def mainpage(request):

    print('enter if statement')
    system = request.POST.get('genrebutton', None)
    
    if request.method == 'POST' and system == "RPG":
        print('the RPG only request has been satisfied ;)')
        username = request.user.get_username()
        selectedgame = GameData.objects.filter(genre='RPG').order_by('?')[0:1].get()
        secondselectedgame = GameData.objects.filter(genre='RPG').order_by('?')[1:2].get()
        thirdselectedgame = GameData.objects.filter(genre='RPG').order_by('?')[2:3].get()
        fourthselectedgame = GameData.objects.filter(genre='RPG').order_by('?')[3:4].get()

        return render(request, 'mainpage.html', 
        {'selectedgame': selectedgame,
         'username': username, 
        'secondselectedgame': secondselectedgame,
        'thirdselectedgame': thirdselectedgame,
        'fourthselectedgame': fourthselectedgame,
        'system': system})

    if request.method == 'POST' and system == "Action-Adventure":
        print('the Action-Adventure only request has been satisfied ;)')
        username = request.user.get_username()
        selectedgame = GameData.objects.filter(genre='Action-Adventure').order_by('?')[0:1].get()
        secondselectedgame = GameData.objects.filter(genre='Action-Adventure').order_by('?')[1:2].get()
        thirdselectedgame = GameData.objects.filter(genre='Action-Adventure').order_by('?')[2:3].get()
        fourthselectedgame = GameData.objects.filter(genre='Action-Adventure').order_by('?')[3:4].get()

        return render(request, 'mainpage.html', 
        {'selectedgame': selectedgame,
         'username': username, 
        'secondselectedgame': secondselectedgame,
        'thirdselectedgame': thirdselectedgame,
        'fourthselectedgame': fourthselectedgame,
        'system': system})

    if request.method == 'POST' and system == "Shooter":
        print('the Sports only request has been satisfied ;)')
        username = request.user.get_username()
        selectedgame = GameData.objects.filter(genre='Shooter').order_by('?')[0:1].get()
        secondselectedgame = GameData.objects.filter(genre='Shooter').order_by('?')[1:2].get()
        thirdselectedgame = GameData.objects.filter(genre='Shooter').order_by('?')[2:3].get()
        fourthselectedgame = GameData.objects.filter(genre='Shooter').order_by('?')[3:4].get()

        return render(request, 'mainpage.html', 
        {'selectedgame': selectedgame,
         'username': username, 
        'secondselectedgame': secondselectedgame,
        'thirdselectedgame': thirdselectedgame,
        'fourthselectedgame': fourthselectedgame,
        'system': system})

    if request.method == 'POST' and system == "Random":
        print('the random get request was followed successfully!')
        username = request.user.get_username()
        selectedgame = GameData.objects.order_by('?')[0:1].get()
        secondselectedgame = GameData.objects.order_by('?')[1:2].get()
        thirdselectedgame = GameData.objects.order_by('?')[2:3].get()
        fourthselectedgame = GameData.objects.order_by('?')[3:4].get()

        return render(request, 'mainpage.html', 
        {'selectedgame': selectedgame,
         'username': username, 
        'secondselectedgame': secondselectedgame,
        'thirdselectedgame': thirdselectedgame,
        'fourthselectedgame': fourthselectedgame,
        'system': system})

    elif request.method == 'GET':
        context = {}
        print('the normal get request was followed successfully!')
        
        context[system] = system
        username = request.user.get_username()
        selectedgame = GameData.objects.order_by('?')[0:1].get()
        secondselectedgame = GameData.objects.order_by('?')[1:2].get()
        thirdselectedgame = GameData.objects.order_by('?')[2:3].get()
        fourthselectedgame = GameData.objects.order_by('?')[3:4].get()

        return render(request, 'mainpage.html', 
        {'selectedgame': selectedgame,
         'username': username, 
        'secondselectedgame': secondselectedgame,
        'thirdselectedgame': thirdselectedgame,
        'fourthselectedgame': fourthselectedgame,
        'system': system})
    else:
        print('the post request was not followed successfully')
    

class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get('button_text')
        print()
        print(text)
        print()
        return render(request, 'mainpage.html')
            


    