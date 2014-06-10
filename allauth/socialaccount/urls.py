from django.conf.urls import patterns, url

from . import views

from houselogic.accounts.views import account_social

urlpatterns = patterns('',
    url('^login/cancelled/$', views.login_cancelled,
        name='socialaccount_login_cancelled'),
    url('^login/error/$', views.login_error, name='socialaccount_login_error'),
    url('^signup/$', account_social, name='socialaccount_signup'),
    url('^connections/$', views.connections, name='socialaccount_connections'))
