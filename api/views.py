from core.models import AuthUserRegistration
from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import HttpResponse
import random
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def account(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
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



        if username and password:
            verifier = random.randint(1000,9999)
            user = User.objects.create_user(username=username, password=password,
                                           )
            user_info = AuthUserRegistration(user=user,email=email,phone=phone,
                                            name=name,address=address,state=state,
                                            zipcode=zipcode,date_of_birth=date_of_birth,
                                            country_of_citizenship=country_of_citizenship,
                                            country_of_residence=country_of_residence)
            user_info.save()
            response = json.dumps({'response': 'ok', 'result': user_info})
            return HttpResponse(response, content_type='application/json')

        response = json.dumps({'response': 'error', 'result': "Username or password not provided"})
        return HttpResponse(response, content_type='application/json')

    user_id = request.GET.get('user_id','')
    if( user_id):
        user = User.objects.get(id=user_id)
        user_info = AuthUserRegistration.objects.get(user=user)
        response = json.dumps({'response': 'ok', 'result': user_info})
        return HttpResponse(response, content_type='application/json')

    response = json.dumps({'response': 'error', 'result': "Id not provided"})
    return HttpResponse(response, content_type='application/json')





def sendSms(phone,code=None):
    pass

