from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist  # This may be used instead of Users.DoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .forms import LoginForm
from .forms import SignupForm, studenLoginForm, StudentInfo, TestIdVal
# for older versoins of Django use:
# from django.core.urlresolvers import reverse
import ast
from .models import Users, studentProfile, question, quesFile, studentMark
import onlinetest.file_reader
import datetime


# from main.forms import SignupForm,LoginForm,SearchForm#,AddTopicForm,AddOpinionForm,

def index(request):
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
            ques_paper = quesFile.objects.get(client=str(request.session['user_id']))
            clientid = ques_paper.client
            tabledata = studentProfile.objects.all()
            return render(request, 'onlinetest/clientadmin.html', {'user_id': user, 'tabledata': tabledata, 'clientid': clientid})
        except Users.DoesNotExist:
            return render(request, 'onlinetest/clientlogin.html')
    else:
        return render(request, 'onlinetest/clientlogin.html')


def studenthome(request):
    return render(request, 'onlinetest/studenthome.html')


def yourtest(request):
    test_id = request.session.get('test_id')

    return render(request, 'onlinetest/yourtest.html')


def clientloginval(request):
    if request.method == 'POST':
        log = LoginForm(request.POST)
        if log.is_valid():
            try:
                user = Users.objects.get(email=log.cleaned_data.get('email'), pwd=log.cleaned_data.get('pwd'))
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
        test_id = request.POST.get('test_id')
        try:
            testfile_id = quesFile.objects.get(ques_paper_id=test_id)
            request.session['test_id'] = test_id
        except quesFile.DoesNotExist:
            return HttpResponse("Wrong Username Password")
        # return HttpResponse("car " + test_id)
        return render(request, 'onlinetest/studenthome.html', {'testfile_id': testfile_id})


def studentLogincheck(request):
    if request.method == 'POST':
        log = studenLoginForm(request.POST)
        if log.is_valid():
            try:
                # return HttpResponse("email" + log.cleaned_data.get('email') + "pass" + log.cleaned_data.get('password'))
                user = studentProfile.objects.get(email=log.cleaned_data.get('email'),
                                                  password=log.cleaned_data.get('password'))
                request.session['studentuid'] = user.id
                return HttpResponseRedirect(reverse('onlinetest:yourtest'))
            except Users.DoesNotExist:
                return HttpResponse("Wrong Username Password")


def register(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            p = Users(
                first_name=signup.cleaned_data.get('firstname'),
                email=signup.cleaned_data.get('email'),
                pwd=signup.cleaned_data.get('pwd'),
            )
            p.save()
            request.session['user_id'] = p.id
    return HttpResponseRedirect(reverse('onlinetest:clientadmin'))


def studentInfo(request):
    if request.method == 'POST':
        addstudent = StudentInfo(request.POST)
        if addstudent.is_valid():
            p = studentProfile.objects.create(
                name=addstudent.cleaned_data.get('name'),
                email=addstudent.cleaned_data.get('email'),
                institute=addstudent.cleaned_data.get('institute'),
                password=addstudent.cleaned_data.get('password'),
                client=addstudent.cleaned_data.get('client')
            )
            p.save()
            # return HttpResponse("yoyo" + p.id)
            request.session['studentuid'] = p.id
    # return HttpResponse("yoyo1" + addstudent.cleaned_data.get('name') + addstudent.cleaned_data.get('email') + addstudent.cleaned_data.get('institute') + addstudent.cleaned_data.get('password'))
    return HttpResponseRedirect(reverse('onlinetest:yourtest'))


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        now = str(datetime.datetime.now().strftime("%Y%m%d%H%M"))
        ques_paper = quesFile.objects.create(ques_paper_id=now, client=str(request.session['user_id']))
        ques_paper.save()
        myfile = request.FILES['myfile']
        ext = myfile.name[myfile.name.rfind('.'):]
        fs = FileSystemStorage()
        filename = fs.save(now + ext, myfile)
        onlinetest.file_reader.file_to_db(filename, str(request.session['user_id']))
        # return HttpResponse("now" + filename + "request.session['user_id']" + str(request.session['user_id']))
        uploaded_file_url = fs.url(filename)
        return render(request, 'onlinetest/clientadmin.html', {
            'uploaded_file_url': uploaded_file_url,
        })
    return render(request, 'onlinetest/clientadmin.html')


# def studentinfodisplay(request):
#     tabledata = studentProfile.objects.filter(client=)
#     return render(request, 'onlinetest/studentinfodisplay.html', {'tabledata': tabledata})
