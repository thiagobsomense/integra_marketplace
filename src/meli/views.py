from django.shortcuts import render
from .api.sales import Orders
from .models import Store, Order, OrderItem, Payment


def orders(request):
    store = Store.objects.all().last()
    client_id = '627529294'
    token = 'APP_USR-5567700473549133-101318-b249ab38a4d1e05e9ff08ec2f2adfeea-627529294'
    order = Orders(client_id, token)
    pedidos = order.archived_orders()
    total = pedidos['paging']['total']

    for pedido in pedidos['results']:
        print(pedido['seller'])
        for items in pedido['order_items']:
            item = OrderItem(items)
            print(item)
    print()
    return render(request, 'meli/orders.html')