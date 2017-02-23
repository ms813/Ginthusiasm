from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from ginthusiasm import views

urlpatterns = [

    #gin
    url(r'^gin/$', views.gin_search_results, name='gin_search_results'),
    url(r'^gin/(?P<gin_name_slug>[\w\-]+)/$', views.show_gin, name='show_gin'),

    # user
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^my-account/$', views.myaccount, name='myaccount'),
    url(r'^logout/$', views.user_logout, name='logout'),

    # password reset
    url(r'^password-reset/$',
        password_reset,
        {'post_reset_redirect' : '/password-reset/done/'},
        name='password_reset'),

    url(r'^password-reset/done/$',
        password_reset_done),

    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'post_reset_redirect' : '/password-reset/complete/'},
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$',
        password_reset_complete),

    # wishlist
    url(r'^wishlist/(?P<username>[\w\-]+)/$', views.wishlist, name='wishlist'),

    # root
    url(r'^$', views.index, name ='index'),

    # debug
    url(r'^maptest/$', views.maptest, name ='maptest'),

    # article

    url(r'^article/(?P<article_name_slug>[\w\-]+)/$', views.article, name ='article'),
    #url(r'^article/$', views.article, name ='article'),

]
