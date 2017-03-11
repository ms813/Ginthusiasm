"""
Import all of the views so they can be accessed from outside the module
"""

from index import index
from about import about
from contact import contact
from login import user_login, signup, myaccount, user_logout
from wishlist import wishlist, wishlist_add
from map_helper import MapHelper
from article import article, article_listing, article_user_listing, article_month, add_article
from gin import show_gin, add_gin, gin_search_results, rate_gin, gin_keyword_filter_autocomplete, add_review
from distillery import show_distillery, distillery_search_results
from collections import collections
from review import my_reviews