from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from .models import Config, Store, Order
from .api.auth import Client
import requests


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    readonly_fields = ['user']

    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # form.base_fields['user'].initial = request.user
        # form.base_fields['user'].disabled = True
        return form

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Store)
class RegisterStoreAdmin(admin.ModelAdmin):
    change_form_template = 'meli/stores_changeform.html'
    readonly_fields = ['user', 'access_token', 'refresh_token', 'client_id']
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('autorizar/', self.set_auth_url),
        ]
        return custom_urls + urls
    
    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        self.code = request.GET.get('code')
        return form
    
    def save_model(self, request, obj, form, change):
        config = Config.objects.filter(user=request.user).first()
        client_id = config.client_id
        client_secret = config.secret_id
        redirect_url = config.redirect_url
        site = config.location

        client = Client(client_id, client_secret, site)
        url = client.authorization_url(redirect_url)
        token = client.exchange_code(redirect_url, code)
        client.set_token(token)
        
        obj.access_token = token['access_token']
        obj.refresh_token = token['refresh_token']
        obj.client_id = token['user_id']
        obj.user = request.user
        return super().save_model(request, obj, form, change)
    
    def set_auth_url(self, request):
        print('teste')
        config = Config.objects.filter(user=request.user).first()
        client_id = config.client_id
        client_secret = config.secret_id
        redirect_url = config.redirect_url
        site = config.location

        client = Client(client_id, client_secret, site)
        url = client.authorization_url(redirect_url)
        print(url)
        return HttpResponseRedirect(url)

    def add_store(self, request):
        config = Config.objects.filter(user=request.user).first()
        client_id = config.client_id
        client_secret = config.secret_id
        redirect_url = config.redirect_url
        site = config.location

        client = Client(client_id, client_secret, site)
        url = client.authorization_url(redirect_url)

        token = client.exchange_code(redirect_url, response.json()['code'])
        client.set_token(token)
        # new_token = client.refresh_token()


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    pass
