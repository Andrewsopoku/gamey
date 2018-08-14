from api.views import account
from django.conf.urls import url, include

app_name = 'api'
urlpatterns = [
    url('api/v1/register', account, name='account'),

]