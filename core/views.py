from core.forms import LoginForm, DepositForm, GainForm, AmtForm
from core.models import AuthUserRegistration, Deposits, Gains
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
def view_deposit(request):
    deposits = Deposits.objects.all()
    context = {"deposits":deposits}
    return render(request,'view_deposits.html',context)


@login_required(login_url=('core:signin'))
def view_gain(request):
    gains = Gains.objects.all()
    context = {"gains":gains}
    return render(request,'view_gains.html',context)




@login_required(login_url=('core:signin'))
def view_user_detail(request,pk):

    users = AuthUserRegistration.objects.get(id=pk)
    context = {"users":users}
    return render(request,'view_user_detail.html',context)


@login_required(login_url=('core:signin'))
def view_deposit_detail(request,pk):

    deposits = Deposits.objects.filter(id=pk)
    users = AuthUserRegistration.objects.get(id=pk)
    total = 0
    for i in deposits:
        total += i.amount

    context = {"deposits":deposits,"users":users, "total":total}
    return render(request,'view_deposit_detail.html',context)


@login_required(login_url=('core:signin'))
def view_gain_detail(request,pk):

    gains = Gains.objects.filter(id=pk)
    users = AuthUserRegistration.objects.get(id=pk)
    total = 0
    for i in gains:
        total += i.amount

    context = {"gains":gains,"users":users, "total":total}
    return render(request,'view_gain_detail.html',context)

@login_required(login_url=('core:signin'))
def add_deposit(request):

    if request.method == "POST":
        deposit_form = DepositForm(data=request.POST)
        print(deposit_form)
        if deposit_form.is_valid():
            user_id = deposit_form.cleaned_data['user_id']
            amount = deposit_form.cleaned_data['amount']

            user = AuthUserRegistration.objects.get(id = user_id)
            dep = Deposits(user = user.user,amount = amount)
            dep.save()
            messages.success(request, 'Successfully added')


    deposit_form = DepositForm()

    context = { "deposit_form":deposit_form}
    return render(request,'add_deposit.html',context)

def add_gain(request):

    if request.method == "POST":
        gain_form = GainForm(data=request.POST)

        if gain_form.is_valid():
            user_id = gain_form.cleaned_data['user_id']
            amount = gain_form.cleaned_data['amount']

            user = AuthUserRegistration.objects.get(id = user_id)
            dep = Gains(user = user.user,amount = amount)
            dep.save()
            messages.success(request, 'Successfully added')


    gain_form = GainForm()

    context = { "gain_form":gain_form}
    return render(request,'add_deposit.html',context)



@login_required(login_url=('core:signin'))
def add_user_deposit(request,pk):
    user = AuthUserRegistration.objects.get(id = pk)
    if request.method == "POST":
        amt_form = AmtForm(data=request.POST)

        if amt_form.is_valid():

            amount = amt_form.cleaned_data['amt']


            dep = Deposits(user = user.user,amount = amount)
            dep.save()
            messages.success(request, 'Successfully added')


    amt_form = AmtForm()

    context = { "amt_form":amt_form,"user":user}
    return render(request,'add_user_deposit.html',context)


@login_required(login_url=('core:signin'))
def add_user_gain(request,pk):
    user = AuthUserRegistration.objects.get(id = pk)
    if request.method == "POST":
        amt_form = AmtForm(data=request.POST)

        if amt_form.is_valid():

            amount = amt_form.cleaned_data['amt']


            dep = Gains(user = user.user,amount = amount)
            dep.save()
            messages.success(request, 'Successfully added')


    amt_form = AmtForm()

    context = { "amt_form":amt_form,"user":user}
    return render(request,'add_user_gain.html',context)

@login_required(login_url=('core:signin'))
def sign_out(request):
    logout(request)
    return redirect("core:home")



