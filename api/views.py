from core.models import AuthUserRegistration, Deposits, Gains, Losts, DepositRequest, WithdrawalRequest
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import random
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def account(request):
    if request.method == 'POST':
        print ("yes")
        username = request.POST.get('username','')
        print(username)
        password = request.POST.get('password','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        name = request.POST.get('name','')
        address = request.POST.get('address','')
        state = request.POST.get('state','')

        zipcode = request.POST.get('zipcode','')
        date_of_birth = request.POST.get('date_of_birth',None)
        country_of_citizenship = request.POST.get('country_of_citizenship','')
        country_of_residence = request.POST.get('country_of_residence','')
        emergency_contact = request.POST.get('emergency_contact','')
        account_type = request.POST.get('account_type','')
        response = {}


        if username and password:
            verifier = random.randint(1000,9999)


            try:
                user = User.objects.create_user(username=username, password=password,
                                               )

                user_info = AuthUserRegistration(user=user,email=email,phone=phone,
                                                name=name,address=address,state=state,
                                                zipcode=zipcode,date_of_birth=date_of_birth,
                                                country_of_citizenship=country_of_citizenship,
                                                country_of_residence=country_of_residence,
                                                emergency_contact=emergency_contact,
                                                account_type=account_type)
                user_info.save()
            except:

                response = json.dumps({'status': 'error', 'result': "Username already Exist"})
                return HttpResponse(response, content_type='application/json')



            response = json.dumps({'status': 'ok','user_id':user_info.id })
            return HttpResponse(response, content_type='application/json')

        response = json.dumps({'status': 'error', 'result': "Username or password not provided"})
        return HttpResponse(response, content_type='application/json')

    user_id = request.GET.get('user_id','')

    if( user_id ) :
        user = User.objects.get(id=user_id)
        user_info = AuthUserRegistration.objects.get(user=user)
        response = json.dumps({'status': 'ok', 'result': user_info})
        return HttpResponse(response, content_type='application/json')

    response = json.dumps({'status': 'error', 'result': "Id not provided"})
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        if username and password:

            user = authenticate(request, username=username, password=password)

            if user is not None:
                    user_serial = AuthUserRegistration.objects.get(user= user)



                    response = json.dumps({'status': 'ok', 'user_id': user_serial.id})

            else:
                    response = json.dumps({'status': 'error', 'result': "Wrong username or password"})
        else:
            response = json.dumps({'status': 'error', 'result': "Username or password not provided"})

    else:
        response = json.dumps({'status': 'error', 'result': "something went wrong"})

    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def get_summary(request):
    if request.method == 'POST':
        try:
            userid = request.POST['user_id']
        except:
            response = json.dumps({'status': 'error',"result": "user id missing"})
        else:
            response = {}

            user = AuthUserRegistration.objects.get(id= userid).user
            name = AuthUserRegistration.objects.get(id= userid).name
            if user:
                # Get Deposit sum:
                depo = Deposits.objects.filter(user=user)
                depo_total =0
                for i in depo:
                    depo_total +=i.amount

                # Get Gains sum:
                gain = Gains.objects.filter(user=user)
                gaintotal = 0
                for i in gain:
                    gaintotal+=i.amount

                lose = Losts.objects.filter(user=user)
                losttotal = 0
                for i in lose:
                    losttotal+=i.amount


                response = json.dumps({'status': 'ok', 'total_deposit': str(depo_total),"total_gain":str(gaintotal),'name':name, 'total_loss': str(losttotal)})

            else:
                        response = json.dumps({'status': 'error',"result": "user does not exist"})



        return HttpResponse(response, content_type='application/json')




@csrf_exempt
def depositrequest(request):
    if request.method == 'POST':
        try:
            userid = request.POST['user_id']
            amt = request.POST['amount']
        except:
            response = json.dumps({'status': 'error',"result": "user id missing"})
        else:
            response = {}

            user = AuthUserRegistration.objects.get(id= userid).user

            if user:
                # Get Deposit sum:
                depo = DepositRequest(user=user,amount=amt)
                depo.save()


                response = json.dumps({'status': 'ok', 'result': ""})

            else:
                        response = json.dumps({'status': 'error',"result": "user does not exist"})



        return HttpResponse(response, content_type='application/json')




@csrf_exempt
def withdrawalrequest(request):
    if request.method == 'POST':
        try:
            userid = request.POST['user_id']
            amt = request.POST['amount']
        except:
            response = json.dumps({'status': 'error',"result": "user id missing"})
        else:
            response = {}

            user = AuthUserRegistration.objects.get(id= userid).user

            if user:
                # Get Deposit sum:
                depo = WithdrawalRequest(user=user,amount=amt)
                depo.save()


                response = json.dumps({'status': 'ok', 'result': ""})

            else:
                        response = json.dumps({'status': 'error',"result": "user does not exist"})



        return HttpResponse(response, content_type='application/json')


@csrf_exempt
def get_deposit_list(request):
    if request.method == 'POST':
        try:
            userid = request.POST['user_id']
        except:
            response = json.dumps({'status': 'error',"result": "user id missing"})
        else:
            response = {}

            user = AuthUserRegistration.objects.get(id= userid).user
            if user:
                # Get Deposit sum:
                depo = Deposits.objects.filter(user=user)
                depo_total =0
                for i in depo:
                    depo_total +=i.amount

                # Get Gains sum:
                data = list(depo.values())
                return JsonResponse({"status":"ok","deposit":data,"deposit_total":str(depo_total)}, safe=False)  # or JsonResponse({'data': data})



            else:
                        response = json.dumps({'status': 'error',"result": "user does not exist"})



        return HttpResponse(response, content_type='application/json')
@csrf_exempt
def get_gain_list(request):
    if request.method == 'POST':
        try:
            userid = request.POST['user_id']
        except:
            response = json.dumps({'status': 'error',"result": "user id missing"})
        else:
            response = {}

            user = AuthUserRegistration.objects.get(id= userid).user
            if user:
                # Get Deposit sum:
                depo = Gains.objects.filter(user=user)
                depo_total =0
                for i in depo:
                    depo_total +=i.amount

                # Get Gains sum:
                data = list(depo.values())
                return JsonResponse({"status":"ok","gain":data,"gain_total":str(depo_total)}, safe=False)  # or JsonResponse({'data': data})



            else:
                        response = json.dumps({'status': 'error',"result": "user does not exist"})



        return HttpResponse(response, content_type='application/json')
@csrf_exempt
def get_lose_list(request):
    if request.method == 'POST':
        try:
            userid = request.POST['user_id']
        except:
            response = json.dumps({'status': 'error',"result": "user id missing"})
        else:
            response = {}

            user = AuthUserRegistration.objects.get(id= userid).user
            if user:
                # Get Deposit sum:
                depo = Losts.objects.filter(user=user)
                depo_total =0
                for i in depo:
                    depo_total +=i.amount

                # Get Gains sum:
                data = list(depo.values())
                return JsonResponse({"status":"ok","lose":data,"lose_total":str(depo_total)}, safe=False)  # or JsonResponse({'data': data})



            else:
                        response = json.dumps({'status': 'error',"result": "user does not exist"})



        return HttpResponse(response, content_type='application/json')



def sendSms(phone,code=None):
    pass


