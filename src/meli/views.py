from django.shortcuts import render
from datetime import datetime
from .api.sales import Orders
from .models import Store, Order, OrderItem, Payment


def orders(request):
    stores = Store.objects.all()

    for store in stores:
        order = Orders(store.client_id, store.access_token)
        pedidos = order.archived_orders()
        total = pedidos['paging']['total']

        for pedido in pedidos['results']:
            info_pedido = {
                'store': store,
                'ml_id': pedido['id'],
                'date_created': pedido['date_created'],
                'date_closed': pedido['date_closed'],
                'last_updated': pedido['last_updated'],
                'manufacturing_ending_date': pedido['manufacturing_ending_date'],
                'pack_id': pedido['pack_id'],
                'pickup_id': pedido['pickup_id'],
                'total_amount': pedido['total_amount'],
                'paid_amount': pedido['paid_amount'],
                'expiration_date': pedido['expiration_date'],
                'currency_id': pedido['currency_id'],
                'shipping_id': pedido['shipping']['id'],
                'status': pedido['status'],
                'status_detail': pedido['status_detail'],
                'buyer_id': pedido['buyer']['id'],
                'taxes_id': pedido['taxes']['id']
            }
            
            pedido_existe = Order.objects.filter(ml_id=info_pedido['ml_id']).first()  
            # if pedido_existe and pedido_existe.last_updated < datetime.strptime(info_pedido['last_updated'],'%Y-%m-%d %H:%M:%S'):
            if pedido_existe:
                pass
                # pedido_existe.objects.update(info_pedido)
            else:
                obj_order = Order(**info_pedido)
                obj_order.save()
                
            for items in pedido['order_items']:
                item = items['item']
                data = {
                    'order': ''
                }
                obj = OrderItem(item, mlb_id=item['id'])
            
    return render(request, 'meli/orders.html')