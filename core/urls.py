from core.views import home, signin
from django.conf.urls import url, include

app_name = 'core'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^signin', signin, name='signin'),

]