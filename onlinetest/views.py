from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist #This may be used instead of Users.DoesNotExist
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .forms import LoginForm, StudentInfo
from .forms import SignupForm
#for older versoins of Django use:
#from django.core.urlresolvers import reverse
import ast
from .models import Users, studentProfile


#from main.forms import SignupForm,LoginForm,SearchForm#,AddTopicForm,AddOpinionForm,


def index(request):
    # if request.session.has_key('user_id'):
    #     uid=request.session['user_id']
    #     try:
    #         user=Users.objects.get(pk=uid)
    #         return render(request, 'onlinetest/logged.html',{'user_id':user})
    #     except Users.DoesNotExist:
    #         return HttpResponse("Email not found")
    # else:
            return render(request, 'onlinetest/index.html')
    

def studentlogin(request):
    return render(request, 'onlinetest/studentlogin.html')

def clientlogin(request):
    return render(request, 'onlinetest/clientlogin.html')

def clientregister(request):
    return render(request, 'onlinetest/clientregister.html')

def clientadmin(request):
    if request.session.has_key('user_id'):
        uid = request.session['user_id']
        try:
            user = Users.objects.get(pk=uid)
            return render(request, 'onlinetest/clientadmin.html', {'user_id':user})
        except Users.DoesNotExist:
            return render(request, 'onlinetest/clientlogin.html')
    else:
        return render(request, 'onlinetest/clientlogin.html')
    #return render(request, 'onlinetest/clientadmin.html')

def studenthome(request):
    return render(request, 'onlinetest/studenthome.html')

def yourtest(request):
    return render(request, 'onlinetest/yourtest.html')

def clientloginval(request):
    if request.method == 'POST':
        log=LoginForm(request.POST)
        if log.is_valid():
            try:
                user=Users.objects.get(email=log.cleaned_data.get('email'),pwd=log.cleaned_data.get('pwd'))
                request.session['user_id'] = user.id
                useremail = user.email
                return HttpResponseRedirect(reverse('onlinetest:clientadmin'))
            except Users.DoesNotExist:
                return HttpResponse("Wrong Username Password")

def clientlogout(request):
        try:
            del request.session['user_id']
        except:
            pass
        return HttpResponseRedirect(reverse('onlinetest:index'))

def studentloginval(request):
    if request.method == 'POST':
        log=LoginForm(request.POST)
        if log.is_valid():
            try:
                user=Users.objects.get(email=log.cleaned_data.get('email'),pwd=log.cleaned_data.get('pwd'))
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('onlinetest:studenthome'))
            except Users.DoesNotExist:
                return HttpResponse("Wrong Username Password")

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
    return HttpResponseRedirect(reverse('onlinetest:clientadmin'))

def studentInfo(request):
    if request.method == 'POST':
        addstudent=StudentInfo(request.POST)
        if addstudent.is_valid():
            p=studentProfile(
                name=addstudent.cleaned_data.get('name'),
                email=addstudent.cleaned_data.get('email'),
                roll_number=addstudent.cleaned_data.get('rollnumber'),
                institute=addstudent.cleaned_data.get('institute'),
                department=addstudent.cleaned_data.get('department'),
            )
            p.save()
            request.session['user_id'] = p.id
    return HttpResponseRedirect(reverse('onlinetest:yourtest'))