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
    
    if request.method == 'GET':
        print('the get request was followed successfully!')
        username = request.user.get_username()
        selectedgame_list = GameData.objects.order_by('?')[0:4]
        for game in selectedgame_list.iterator():
            print (game)
            print (game.gname)
            print (game.description)
    
        return render(request, 'mainpage.html', 
        { 
        'gamename': game.gname, 'gamedescription': game.description, 'gamelist': selectedgame_list
        }) 
    

class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get('button_text')
        print()
        print(text)
        print()
        return render(request, 'mainpage.html')
            


    