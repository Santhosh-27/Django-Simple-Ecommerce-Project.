from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

app_name='myapp'

urlpatterns=[
path('',views.products,name='products'),
path('cart/<pro_id>/',views.add_cart,name='cart'),
path('orders/',views.orders_summary,name='order')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
