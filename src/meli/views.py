from django.shortcuts import render



class Store():
    def add_store(request):
        CLIENT_ID = '5567700473549133'
        CLIENT_SECRET = 'NFlAtiFUEsf9KauUSxJiRPHXs1hojZBX'
        SITE = 'MLB'
        REDIRECT_URL = 'http://localhost:8000/mercadolivre/'
        CODE = request.GET.get('code')
        
        
        ACCESS_TOKEN = request.GET.get('access_token')
        REFRESH_TOKEN = token['refresh_token']
        USER_ID = token['user_id']
        
        print(new_token)

        return render(request, 'meli/auth.html', {'url': url})


def orders(request):
    return render(request, 'meli/orders.html')