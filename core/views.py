from core.forms import LoginForm
from core.models import AuthUserRegistration
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return  render(request,'index.html')

def signin(request):

    if request.method == "POST":
        signin_form = LoginForm(data=request.POST)
        if signin_form.is_valid():
            name = signin_form.cleaned_data['username']
            password = signin_form.cleaned_data['password']

            user = authenticate(request, username=name, password=password,is_staff=0)

            if user is not None and user.is_staff:

                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('core:view_user')

            signin_form = LoginForm(data=request.POST)
            context = {'signin_form': signin_form}
            messages.error(request, 'Wrong username or password')
            return render(request, 'login.html', context)

    signin_form = LoginForm()
    context = {'signin_form':signin_form}
    return  render(request, 'login.html',context)

def dashboard(request):
    return redirect('core:view_user')

@login_required(login_url=('core:signin'))
def view_user(request):
    users = AuthUserRegistration.objects.all()
    context = {"users":users}
    return render(request,'view_users.html',context)



@login_required(login_url=('core:signin'))
def view_user_detail(request,pk):
    print(pk)
    users = AuthUserRegistration.objects.get(id=pk)
    context = {"users":users}
    return render(request,'view_user_detail.html',context)

@login_required(login_url=('core:signin'))
def sign_out(request):
    logout(request)
    return redirect("core:home")



