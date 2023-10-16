import requests
from urllib.parse import urlencode


class Orders():
    api_orders = 'https://api.mercadolibre.com/orders/search'

    def __init__(self, client_id, token):
        self.client_id = client_id
        self.token = token
        self.headers = { 'Authorization': f'Bearer {self.token}', }

    def orders_period(self, date_start, date_end):
        params = {
            'seller': self.client_id,
            'order.date_created.from': date_start,
            'order.date_created.to': date_end,
            'order.status': 'paid'
        }
        url = self.api_orders

        response = requests.request('GET', url, headers=self.headers, data=urlencode(params))
        return response.json()

    def archived_orders(self):
        params = {}
        url = f'{self.api_orders}/archived?seller={self.client_id}'

        response = requests.request('GET', url, headers=self.headers, data=urlencode(params))
        return response.json()

    def recents_orders(self):
        params = {}
        url = f'{self.api_orders}/recent?seller={self.client_id}'

        response = requests.request('GET', url, headers=self.headers, data=params)
        return response.json()
    
    def products():
        pass

    def shipping(self):
        pass

    def payments():
        pass
