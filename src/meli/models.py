from django.db import models
from django.contrib.auth import get_user_model


class Config(models.Model):
    SITE_CHOICES = (
        ('MLA', 'Argentina'),
        ('MLB', 'Brasil'),
        ('MCO', 'Colombia'),
        ('MCR', 'Costa Rica'),
        ('MEC', 'Equador'),
        ('MLC', 'Chile'),
        ('MLM', 'Mexico'),
        ('MLU', 'Uruguai'),
        ('MLV', 'Venezuela'),
        ('MPA', 'Panama'),
        ('MPE', 'Peru'),
        ('MPT', 'Portugal'),
        ('MRD', 'Republica Dominicana')
    )

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    client_id = models.CharField(max_length=254)
    secret_id = models.CharField(max_length=254)
    redirect_url = models.CharField(max_length=254)
    location = models.CharField(max_length=3, choices=SITE_CHOICES, default='MLB')

    def __str__(self):
        return self.client_id


class Store(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='lojas', on_delete=models.RESTRICT)
    name_store = models.CharField(max_length=150)
    access_token = models.CharField(max_length=254)
    refresh_token = models.CharField(max_length=254)
    client_id = models.CharField(max_length=150)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.access_token


class Order(models.Model):
    pass
