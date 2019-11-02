from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegisterForm
from accounts.models import ProfileModel
from django.contrib.auth.models import User

def registration(request):
    if request.method=='POST':
        form=RegisterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            item2=form.save(commit=False)
            item2.save()
            return HttpResponseRedirect('/')
    else:
        form=RegisterForm()
    context={
    'form':form,
    }
    return render(request,'accounts/register.html',context)
















































def profile(request):

    obj=ProfileModel.objects.all()
    context={
    'obj':obj,
    }
    return render(request,'accounts/profile.html',context)
