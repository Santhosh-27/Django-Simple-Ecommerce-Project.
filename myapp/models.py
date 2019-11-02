from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Item(models.Model):
    category_choice=(
    ('Shirt','shirt'),
    ("Sport Wear",'sport wear'),
    ('Out Wear','Out wear')
    )
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to='picts')
    price=models.FloatField(default=0.00)
    discount_price=models.FloatField(blank=True,null=True)
    category=models.CharField(choices=category_choice,max_length=20,default='Shirt')
    description=models.TextField(default='')

    def __str__(self):
        return self.title
class OrderItem(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return self.item.title

    def get_total_price(self):
        return self.quantity * self.item.price

class Order(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items=models.ManyToManyField(OrderItem)
    start_date=models.DateTimeField(auto_now_add=True)
    ordered_date=models.DateTimeField()
    ordered=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
