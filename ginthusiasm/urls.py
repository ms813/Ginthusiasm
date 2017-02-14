from django.conf.urls import url

from ginthusiasm import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^my-account/$', views.myaccount, name='myaccount'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^wishlist/(?P<username>[\w\-]+)/$', views.wishlist, name='wishlist'),
    url(r'^$', views.index, name ='index'),
]
