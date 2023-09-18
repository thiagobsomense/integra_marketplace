from django.urls import path
from .views import auth_meli

app_name  = 'meli'

urlpatterns = [
    path('', auth_meli, name='auth'),
    # path('<str:code>/?<str:state>/', auth_meli, name='auth'),
]
