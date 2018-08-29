from core.views import home, signin, dashboard, view_user, sign_out, view_user_detail, view_deposit, view_gain, \
    view_deposit_detail, view_gain_detail
from django.conf.urls import url, include

app_name = 'core'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^signin', signin, name='signin'),
    url(r'^dashbord', dashboard, name='dashboard'),

    url(r'^view-user-detail/(?P<pk>\d+)', view_user_detail ,name='view_user_detail'),
    url(r'^view-deposit-detail/(?P<pk>\d+)', view_deposit_detail ,name='view_deposit_detail'),
    url(r'^view-gain-detail/(?P<pk>\d+)', view_gain_detail ,name='view_gain_detail'),

    url(r'^view-user', view_user ,name='view_user'),
    url(r'^view-deposit', view_deposit ,name='view_deposit'),
    url(r'^view-gain', view_gain ,name='view_gain'),

    url(r'^logout', sign_out ,name='logout'),


]