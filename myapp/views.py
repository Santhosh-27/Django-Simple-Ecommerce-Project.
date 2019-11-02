from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Item,Order,OrderItem
from django.utils import timezone

@login_required
def products(request):
    product=Item.objects.all()
    context={
    'product':product,
    }
    return render(request,'myapp/products.html',context)
@login_required
def add_cart(request,pro_id):
    item=Item.objects.get(pk=pro_id)
    myorder, created=OrderItem.objects.get_or_create(item=item)
    order=Order.objects.filter(user=request.user, ordered=False)
    if order.exists():
        order=order[0]
        if order.items.filter(item__pk=item.pk).exists():
            myorder.quantity+=1
            myorder.save()
        else:
            order.items.add(myorder)
    else:
        ordered_date=timezone.now()
        order=Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(myorder)

    context={
    'item':item
    }
    #return render(request,'myapp/cart.html',context)
    return HttpResponseRedirect("/myapp/")
@login_required
def orders_summary(request):
    order=OrderItem.objects.all()
    context={
    'order':order
    }
    return render(request,'myapp/orders.html',context)
