from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='profile_picts',default='')

    def __str__(self):
        return f'{self.user} profile'
