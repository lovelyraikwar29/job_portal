from imaplib import _Authenticator
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    return render(request,'admin_login.html')


def user_login(request):
    error = ""

    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)

        if user:
            try:
                user1 = StudentUser.objects.get(user=user)

                if user1.type == "student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"

            except StudentUser.DoesNotExist:
                error = "yes"
        else:
            error = "yes"

    d = {'error': error}
    return render(request, 'user_login.html', d)


def recruiter_login(request):
    return render(request, 'recruiter_login.html')

# def user_signup(request):
#     error=""
#     if request.method == 'POST':
#        f = request.POST['fname']
#        l = request.POST['lname']
#        c = request.POST['cnumber']
#        e = request.POST['email']
#        p = request.POST['pwd']
#        cp = request.POST['cpwd']
#        g = request.POST['gender']
#        i = request.FILES['image']
#        print(f, l, c, e, p, g, i)
#        try:
#         User=User.objects.create_user(first_name=f,last_name=l,username=e,password=p,)
#         StudentUser.objects.create(user=User,mobile=c,image=i,gender=g,type='student')
#         error="no"
#        except:
#           error="yes"
#     d={'error':error}
#     return render(request, 'user_signup.html',d)

def user_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        c = request.POST['cnumber']
        e = request.POST['email']
        p = request.POST['pwd']
        cp = request.POST['cpwd']
        g = request.POST['gender']
        i = request.FILES['image']
        print(request.POST)

        try:
            User = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            StudentUser.objects.create(user=User, mobile=c, image=i, gender=g, type='student')
            error = "no"
        except:
            error = "yes"

    d = {'error': error}
    return render(request, 'user_signup.html', d)



def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')