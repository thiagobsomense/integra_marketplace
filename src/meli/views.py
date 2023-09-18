from django.shortcuts import render
from mercadolibre.client import Client


def auth_meli(request):
    CLIENT_ID = '5567700473549133'
    CLIENT_SECRET = 'NFlAtiFUEsf9KauUSxJiRPHXs1hojZBX'
    SITE = 'MLB'
    REDIRECT_URL = 'http://localhost:8000/mercadolivre/'
    CODE = request.GET.get('code')

    client = Client(CLIENT_ID, CLIENT_SECRET, site=SITE)
    url = client.authorization_url(REDIRECT_URL)
    # token = client.exchange_code(REDIRECT_URL, CODE)
    # client.set_token(token)

    # new_token = client.refresh_token()
    
    # print(new_token)

    return render(request, 'teste.html', {'url': url})
