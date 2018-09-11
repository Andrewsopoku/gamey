from api.views import account, signin, get_summary, get_deposit_list, get_gain_list, depositrequest, withdrawalrequest, \
    get_lose_list
from django.conf.urls import url, include

app_name = 'api'
urlpatterns = [
    url('api/v1/register', account, name='api_account'),
    url('api/v1/signin', signin, name='api_signin'),
    url('api/v1/summary', get_summary, name='api_summary'),
    url('api/v1/deposit-request', depositrequest, name='api_deposit_request'),
    url('api/v1/withdrawal-request', withdrawalrequest, name='api_deposit_request'),
    url('api/v1/deposit-list', get_deposit_list, name='api_deposit_list'),
    url('api/v1/gain-list', get_gain_list, name='api_gain_list'),
    url('api/v1/lose-list', get_lose_list, name='api_gain_list'),
]