from core.views import home, signin, dashboard, view_user, sign_out, view_user_detail, view_deposit, view_gain, \
    view_deposit_detail, view_gain_detail, add_deposit, add_gain, add_user_deposit, add_user_gain
from django.conf.urls import url, include

app_name = 'core'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^signin', signin, name='signin'),
    url(r'^dashbord', dashboard, name='dashboard'),

    url(r'^view-user-detail/(?P<pk>\d+)', view_user_detail ,name='view_user_detail'),
    url(r'^view-deposit-detail/(?P<pk>\d+)', view_deposit_detail ,name='view_deposit_detail'),
    url(r'^view-gain-detail/(?P<pk>\d+)', view_gain_detail ,name='view_gain_detail'),

    url(r'^add-user-deposit/(?P<pk>\d+)', add_user_deposit ,name='add_user_deposit'),
    url(r'^add-user-gain/(?P<pk>\d+)', add_user_gain ,name='add_user_gain'),


    url(r'^view-user', view_user ,name='view_user'),
    url(r'^view-deposit', view_deposit ,name='view_deposit'),
    url(r'^view-gain', view_gain ,name='view_gain'),

    url(r'^add-deposit', add_deposit ,name='add_deposit'),
    url(r'^add-gain', add_gain ,name='add_gain'),

    url(r'^logout', sign_out ,name='logout'),


]