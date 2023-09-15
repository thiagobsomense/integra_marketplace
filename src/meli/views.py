from django.shortcuts import render
from mercadolibre.client import Client


def auth_meli(request):
    CLIENT_ID = '2100982055659711'
    CLIENT_SECRET = 'svGW52JquU2tBObFjrDU7iQeQqJWOAAO'
    SITE = 'MLB'
    REDIRECT_URL = 'http://localhost:8000/mercadolivre/'
    CODE = ''

    client = Client(CLIENT_ID, CLIENT_SECRET, site=SITE)
    url = client.authorization_url(REDIRECT_URL)
    token = client.exchange_code(REDIRECT_URL, CODE)
    client.set_token(token)

    new_token = client.refresh_token()

    return render(request, 'teste.html', {'url':url})
