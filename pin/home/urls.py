from django.conf.urls import url
from home.views import HomeView, CreatePassword
from home import views
app_name = 'home'
urlpatterns = [
    #url(r'^$', views.home, name='home'), url(r'^$', views.home, name="home"),
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^password/$', views.passwords, name='modify_password'),
    url(r'^delete/(?P<password_id>[0-9]+)/$', views.password_delete, name='delete_view'),
    url(r'^password/create/$', CreatePassword.as_view(), name='create_password'),
]