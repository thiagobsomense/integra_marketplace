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
        return self.name_store


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    ml_id = models.CharField(max_length=60, unique=True)
    date_created = models.DateTimeField()
    date_closed = models.DateTimeField()
    last_updated =  models.DateTimeField()
    manufacturing_ending_date = models.DateTimeField()
    pack_id = models.CharField(max_length=45, blank=True, null=True)
    pickup_id = models.CharField(max_length=45, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateTimeField()
    currency_id = models.CharField(max_length=45)
    shipping_id = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    status_detail = models.TextField(blank=True, null=True)
    buyer_id = models.CharField(max_length=45)
    taxes_id = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.ml_id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    mlb_id = models.CharField(max_length=45)
    mlb_item_id = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    category_id = models.CharField(max_length=45)
    variation_id = models.CharField(max_length=45)
    seller_custom_field = models.CharField(max_length=45)
    variation_attributes = models.TextField()
    warranty = models.CharField(max_length=45)
    condition = models.CharField(max_length=45)
    seller_sku = models.CharField(max_length=45)
    global_price = models.CharField(max_length=45)
    quantity = models.CharField(max_length=45)
    unit_price = models.CharField(max_length=30)
    full_unit_price = models.CharField(max_length=30)
    currency_id = models.CharField(max_length=45)
    manufacturing_days = models.CharField(max_length=45)
    sale_fee = models.CharField(max_length=45)
    listing_type_id = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Shipping(models.Model):
    pass


class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    store_id = models.CharField(max_length=30)
    payer_id = models.CharField(max_length=30, blank=True, null=True)
    collector_id = models.CharField(max_length=30, blank=True, null=True)
    site_id = models.CharField(max_length=30)
    card_id = models.CharField(max_length=30, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    payment_method_id = models.CharField(max_length=30)
    currency_id = models.CharField(max_length=30)
    installments = models.IntegerField()
    coupon_id = models.CharField(max_length=30, blank=True, null=True)
    atm_transfer_reference = models.TextField(blank=True, null=True)
    operation_type = models.CharField(max_length=30)
    payment_type = models.CharField(max_length=30)
    available_actions = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30)
    status_code = models.CharField(max_length=30, blank=True, null=True)
    status_detail = models.CharField(max_length=30)
    transaction_amount = models.CharField(max_length=30)
    transaction_amount_refunded = models.CharField(max_length=30, blank=True, null=True)
    taxes_amount = models.CharField(max_length=30, blank=True, null=True)
    shipping_cost = models.CharField(max_length=30, blank=True, null=True)
    coupon_amount = models.CharField(max_length=30, blank=True, null=True)
    overpaid_amount = models.CharField(max_length=30, blank=True, null=True)
    total_paid_amount = models.CharField(max_length=30)
    installments_amount = models.CharField(max_length=30, blank=True, null=True)
    deferred_period = models.CharField(max_length=30, blank=True, null=True)
    date_approved = models.CharField(max_length=30, blank=True, null=True)
    authorization_code = models.CharField(max_length=30, blank=True, null=True)
    transaction_order_id = models.CharField(max_length=30, blank=True, null=True)
    date_created = models.CharField(max_length=30)
    date_last_modified = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    