from time import sleep

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.core.mail import send_mail
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from revproxy.views import ProxyView

from .models import User, Challenge, Container
from .forms import RegisterForm, LoginForm
from .docker import *

class Failure(JsonResponse):
    def __init__(self, msg={}):
        json = {"action" : "failure"}
        json.update(msg)
        JsonResponse.__init__(self, json)

class DockerMultiplexView(View):

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, path):
        if request.user.container is not None:
            container_addr = "http://"+\
            get_docker_ip(request.user.container.docker_id)
        else:
            return Failure()

        class DockerProxyView(ProxyView):
            upstream = container_addr

        return DockerProxyView.as_view()(request, path)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None: #and user.is_active: TODO
                login(request, user)
                return redirect('/')

    if request.method == "GET":
        return render(request, 'login.html', {'form' : LoginForm()})
    return Failure()

def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.\
                            create_user(request.POST['username'],
                                        request.POST['email'],
                                        request.POST['password'])
            new_user.creation_date = timezone.now()
            new_user.save()
            #send_mail TODO
            return redirect('/login')
        else:
            Failure({'errors' : form.errors})
    if request.method == "GET":
        return render(request, 'register.html', {'form' : RegisterForm()})

# def user_validate(request):
#     if request.method == "GET":
#         if not request.user.is_authenticated():
#             #TODO verify UUID
#             #request.user.is_active = True
#             #request.user.save()
#             return Success()
#     return Failure()

def index(request):
    return render(request, 'index.html')

def getListOf(cls):
    return [e.dict for e in cls.objects.all()]

@login_required
def get_user(request, Id):
    qs = User.objects.filter(pk=Id)
    if qs.exists():
        return render(request, 'user.html', {'user': qs[0].dict})
    return Failure()

@login_required
def get_challenge(request, Id):
    qs = Challenge.objects.filter(pk=Id)
    if qs.exists():
        return render(request, 'challenge.html',
                      {'challenge' : qs[0].getFullDict(request.user)})
    return Failure()

@login_required
def get_users(request):
    if request.method == "GET":
         return render(request, 'users.html',
                      {'users' : getListOf(User)})
    return Failure()

@login_required
def get_challenges(request):
    if request.method == "GET":
        l = [c.getFullDict(request.user) for c in Challenge.objects.all()]
        return render(request, 'challenges.html', {'challenges' : l})
    return Failure()

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')

@login_required
def start_challenge(request, Id):
    cf = Challenge.objects.filter(pk=Id)
    if cf.exists():
        if request.user.container is None:
            container = Container(creation_date=timezone.now(), challenge=cf[0])
            try:
                container.docker_id = create_docker(cf[0].docker_name)
            except CalledProccessError as e:
                return Failure({'error' : str(e)})
            container.save()
            request.user.container = container
            request.user.save()
            sleep(5) #waiting a few seconds before redirect is needed
            return redirect('/ex/')
        else:
            return Failure({'error' : 'A challenge is already started',
                            'challenge' : request.user.container.challenge.id})
    else:
        return Failure({'challenge' : 'not found'})

@login_required
def stop_challenge(request, Id):
    qs = Challenge.objects.filter(pk=Id)
    if qs.exists():
        if request.user.container is not None:
            try:
                stop_docker(request.user.container.docker_id)
            except CalledProccessError as e:
                return Failure({'error' : str(e)})
            request.user.container.delete()
            request.user.container = None
            request.user.save()
            return redirect('/challenges')
        else:
            return Failure({'error': 'Challenge not started'})
    return Failure({'error' : 'Challenge does not exist'})

@login_required
def validate_challenge(request, Id):
    if request.method == "POST":
        qs = Challenge.objects.filter(pk=Id)
        if qs.exists():
             if "flag" in request.POST and \
                 request.POST["flag"] == qs[0].flag:
                 if request.user.solved.filter(pk=qs[0].pk):
                     return Failure({'error' : 'Challenge already validated'})
                 request.user.solved.add(qs[0])
                 request.user.score += qs[0].value
                 request.user.save()
                 return redirect('/challenges')
             else:
                 return Failure({'error' : 'wrong flag'})
        else:
            return Failure({'error' : 'Challenge does not exist'})
