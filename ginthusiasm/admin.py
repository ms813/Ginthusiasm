from django.contrib import admin
from ginthusiasm.models import Article, Distillery, Gin, TasteTag, Review, UserProfile, Wishlist, Contact

"""
Register all of the models with the admin interface
"""

admin.site.register(Article)
admin.site.register(Distillery)
admin.site.register(Gin)
admin.site.register(TasteTag)
admin.site.register(Review)
admin.site.register(UserProfile)
admin.site.register(Wishlist)
admin.site.register(Contact)
