from django.conf.urls import url

from ginthusiasm import views

urlpatterns = [
    url(r'^gin/$', views.gin_search_results, name='gin_search_results'),
    url(r'^gin/(?P<gin_name_slug>[\w\-]+)/$', views.show_gin, name='show_gin'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^my-account/$', views.myaccount, name='myaccount'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^wishlist/(?P<username>[\w\-]+)/$', views.wishlist, name='wishlist'),
    url(r'^$', views.index, name ='index'),

    # debug
    url(r'^maptest/$', views.maptest, name ='maptest'),
]
