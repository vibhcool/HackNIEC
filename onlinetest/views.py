from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist #This may be used instead of Users.DoesNotExist
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse
import ast

#from .models import Users
#from main.forms import SignupForm,LoginForm,SearchForm#,AddTopicForm,AddOpinionForm,


def index(request):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=Users.objects.get(pk=uid)
            return render(request, 'onlinetest/logged.html',{'user_id':user})
        except Users.DoesNotExist:
            return HttpResponse("UserName not found")
    else:
        return render(request, 'onlinetest/main.html')

def login(request):
    return render(request, 'onlinetest/login.html')

def signup(request):
    return render(request, 'onlinetest/signup.html')

def logInReq(request):
    if request.method == 'POST':
        log=LoginForm(request.POST)
        if log.is_valid():
            try:
                user=Users.objects.get(user_name=log.cleaned_data.get('username'),pwd=log.cleaned_data.get('pwd'))
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('main:index'))
            except Users.DoesNotExist:
                return HttpResponse("WRONG USERNAME OR PASSWORD")

def register(request):
    if request.method == 'POST':
        signup=SignupForm(request.POST)
        if signup.is_valid():
            p=Users(
                first_name=signup.cleaned_data.get('firstname'),
                email=signup.cleaned_data.get('email'),
                pwd=signup.cleaned_data.get('pwd'),
            )
            p.save()
            request.session['user_id'] = p.id
    return HttpResponseRedirect(reverse('main:index'))

