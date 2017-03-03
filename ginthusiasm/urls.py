from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

from ginthusiasm import views

##########     Gin     ##########
gin_patterns = [
    url(r'^gin-search/$', views.gin_autocomplete, name='gin_autocomplete'),
    url(r'^gin/$', views.gin_search_results, name='gin_search_results'),
    url(r'^gin/(?P<gin_name_slug>[\w\-]+)/$', views.show_gin, name='show_gin'),
    url(r'^gin/(?P<gin_name_slug>[\w\-]+)/rate/$', views.rate_gin, name='rate_gin'),
]

##########     User     ##########
user_patterns = [
    # User, login etc
    url(r'^login/$', views.user_login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^my-account/$', views.myaccount, name='myaccount'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^my-account/upload/$', views.myaccount, name='profile_image_upload'),

    # Password reset
    url(r'^password-reset/$',
        password_reset,
        {'post_reset_redirect': '/password-reset/done/'},
        name='password_reset'),

    url(r'^password-reset/done/$',
        password_reset_done),

    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'post_reset_redirect': '/password-reset/complete/'},
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$',
        password_reset_complete),
]

##########     Wishlist     ##########
wishlist_patterns = [
    url(r'^wishlist/add/$', views.wishlist_add, name='wishlist_add'),
    url(r'^wishlist/(?P<username>[\w\-]+)/$', views.wishlist, name='wishlist'),
]

##########     Distillery     ##########
distillery_patterns = [
    url(r'^distillery/$', views.distillery_search_results, name='distillery_search_results'),
    url(r'^distillery/(?P<distillery_name_slug>[\w\-]+)/$', views.show_distillery, name='show_distillery'),
    url(r'^distillery/(?P<distillery_name_slug>[\w\-]+)/add-gin/$', views.add_gin, name='add_gin'),
]

##########     Review     ##########
review_patterns = [

    url(r'^add-review/(?P<gin_name_slug>[\w\-]+)/$', views.add_review, name='add_review'),
    # url(r'^add-review/$', views.add_revzzzzzzzsiew, name='add_review'),

]

##########     Article     ##########
article_patterns = [
    url(r'^article/$', views.article_listing, name='article_listing'),
    url(r'^article/(?P<user_name>[\w\-]+)/$', views.article_user_listing, name='article_user_listing'),
    url(r'^article/(?P<user_name>[\w\-]+)/add-article/$', views.add_article, name='add_article'),
    url(r'^article/(?P<user_name>[\w\-]+)/(?P<article_name_slug>[\w\-]+)/$', views.article, name='article'),
    url(r'^gin-of-the-month/$', views.article_month, name='article_month'),

]

##########     Debug     ##########
debug_patterns = [
    url(r'^maptest/$', views.maptest, name='maptest'),
]

urlpatterns = [
    ##########     Index     ##########
    url(r'^$', views.index, name='index'),

    ##########     About     ##########
    url(r'^about/$', views.about, name='about'),

    ##########     Contact     ##########
    url(r'^contact/$', views.about, name='contact'),
]

urlpatterns += gin_patterns
urlpatterns += user_patterns
urlpatterns += wishlist_patterns
urlpatterns += distillery_patterns
urlpatterns += review_patterns
urlpatterns += article_patterns
urlpatterns += debug_patterns
