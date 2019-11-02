from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings
app_name='accounts'
urlpatterns=[
path('register/',views.registration,name='register'),
path('',auth_view.LoginView.as_view(template_name='accounts/login.html'),name='login'),
path('logout/',auth_view.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
path('profile/',views.profile, name='profile'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
