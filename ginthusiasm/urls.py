from django.conf.urls import url

from ginthusiasm import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^$', views.index, name ='index'),

]
