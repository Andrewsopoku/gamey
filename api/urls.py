from api.views import account, signin
from django.conf.urls import url, include

app_name = 'api'
urlpatterns = [
    url('api/v1/register', account, name='api_account'),
    url('api/v1/signin', signin, name='api_signin')

]