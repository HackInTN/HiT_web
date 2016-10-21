from time import sleep

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
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
from .container import *
from .flag_validation import make_bin

def failure(request, d={}):
    d["action"] = "failure"
    return render(request, 'error.html', d)

class DockerMultiplexView(View):

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, path):
        if request.user.container is not None:
            container_addr = "http://"+\
            get_docker_ip(request.user.container.docker_id)
        else:
            return failure(request, {"errors" : ['No docker challenge started']})

        class DockerProxyView(ProxyView):
            upstream = container_addr

        return DockerProxyView.as_view()(request, path)

def reqLogin(request):
    return render(request, 'plzLog.html')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None: #and user.is_active: TODO
                login(request, user)
                return redirect('/')
            else:
                return failure(request, {'errors' : ['user does not exists']})
        else:
            return failure(request, {'errors' : form.errors})
    if request.method == "GET":
        return render(request, 'login.html', {'form' : LoginForm()})

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
            return redirect('/')
        else:
            return failure(request, {'errors' : form.errors})
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
    return failure(request)

@login_required
def get_challenge(request, Id):
    if request.method == "GET":
        qs = Challenge.objects.filter(pk=Id)
        if qs.exists():
            return render(request, 'challenge.html',
                          {'challenge' : qs[0].getFullDict(request.user)})
        else:
            return failure(request, {'errors': ['Challenge does not exists']})

@login_required
def get_users(request):
    if request.method == "GET":
         return render(request, 'users.html',
                      {'users' : getListOf(User)})

@login_required
def get_challenges(request):
    if request.method == "GET":
        l = [c.getFullDict(request.user) for c in Challenge.objects.all()]
        return render(request, 'challenges.html', {'challenges' : l})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'index.html')

@login_required
def start_challenge(request, Id):
    if request.method != "POST":
        return failure(request, {'errors' : ['Bad http method']})
    ch = Challenge.objects.filter(pk=Id).first()
    if ch is not None:
        if ch.is_docker:
            if request.user.container is None:
                container = Container(creation_date=timezone.now(), challenge=ch)
                try:
                    container.docker_id = create_docker(ch.docker_name)
                except Exception as e:
                    return failure(request, {'errors' : [str(e)]})
                container.save()
                request.user.container = container
                request.user.save()
                sleep(5) #waiting a few seconds before redirect is needed
                return redirect('/ex/')
            else:
                return failure(request, {'errors' : ['A docker challenge is already started'],
                                'challenge' : request.user.container.challenge.id})
        elif ch.is_binary:
            binary = make_bin(request.user, ch)
            response = HttpResponse(binary,
                            content_type="application/octet-stream")
            response['Content-disposition'] = "attachment; filename=crackme"

            return response



    else:
        return failure(request, {'errors' : ['Challenge not found']})

@login_required
def stop_challenge(request, Id):
    if request.method != "POST":
        return failure(request, {'errors' : ['Bad http method']})
    qs = Challenge.objects.filter(pk=Id)
    if qs.exists():
        if request.user.container is not None:
            try:
                stop_docker(request.user.container.docker_id)
            except:
                return failure(request, {'errors' : ['Internal error']})
            request.user.container.delete()
            request.user.container = None
            request.user.save()
            return redirect('/challenges')
        else:
            return failure(request, {'errors': ['Challenge not started']})
    return failure(request, {'errors' : ['Challenge does not exist']})

@login_required
def validate_challenge(request, Id):
    if request.method == "POST":
        ch = Challenge.objects.filter(pk=Id).first()
        if ch is not None:
             if "flag" in request.POST and \
                          ch.check_flag(request.user, request.POST["flag"]):
                 if request.user.solved.filter(pk=ch.pk):
                     return failure(request,
                                   {'errors' : ['Challenge already validated']})
                 request.user.solved.add(ch)
                 request.user.score += ch.value
                 request.user.save()
                 return redirect('/challenges')
             else:
                 return failure(request, {'errors' : ['wrong flag']})
        else:
            return failure(request, {'errors' : ['Challenge does not exist']})
