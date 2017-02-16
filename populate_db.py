import sys
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ginthusiasm_project.settings')

import django
django.setup()

from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password

from ginthusiasm.models import Article, Distillery, Gin, Review, UserProfile, Wishlist

def populate_article():
    print("Populating articles...")
    # article population here...

def populate_distillery():
    print("Populating distilleries...")
    # distillery population here...

def populate_gin():
    print("Populating gins...")

    gins = [
        {
            "name" : "Isle of Harris Gin",
            "price" : "35.00",
            "short_description" : "Test short description",
            "long_description" : "Test long description",
            "taste_tags" : "Sugar Kelp, Juniper, Coriander, Angelica Root, Orris Root, Cubebs, Bitter Orange Peel, Licorice, Cassia Bark",
            "image" : "desert.png",
        }
    ]

    for data in gins:
        gin, created = Gin.objects.get_or_create(name = data['name'])

        if created:
            gin.price = data['price']
            gin.short_description = data['short_description']
            gin.long_description = data['long_description']
            gin.taste_tags = data['taste_tags']
            gin.image = data['image']

            gin.save()

def populate_review():
    print("Populating reviews...")
    # review population here...

def populate_wishlist():
    print("Populating wishlist...")
    users = UserProfile.objects.all()
    if len(users) == 0:
        populate_users()

    for user in UserProfile.objects.all():
        wishlist = Wishlist.objects.get_or_create(user=user)

def populate_users():
    print("Populating users...")

    users = [
        {
            "username" : "Catherine",
            "first_name" : "Catherine",
            "last_name" : "Daly",
            "email" : "2283461d@student.gla.ac.uk",
            "password" : make_password("catherineadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Robert",
            "first_name" : "Robert",
            "last_name" : "Gilmour",
            "email" : "2022607g@student.gla.ac.uk",
            "password" : make_password("robertadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Matt",
            "first_name" : "Matthew",
            "last_name" : "Smith",
            "email" : "2283142s@student.gla.ac.uk",
            "password" : make_password("mattadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Rozz",
            "first_name" : "Rosalyn",
            "last_name" : "Taylor",
            "email" : "2226947t@student.gla.ac.uk",
            "password" : make_password("rozzadmin"),
            "user_type" : UserProfile.ADMIN
        },
        {
            "username" : "Alice",
            "first_name" : "Alice",
            "last_name" : "Alison",
            "email" : "12345@doesntexist.com",
            "password" : make_password("alicetest"),
            "user_type" : UserProfile.EXPERT
        },
        {
            "username" : "Bob",
            "first_name" : "Bob",
            "last_name" : "Bobertson",
            "email" : "54321@doesntexist.com",
            "password" : make_password("bobtest"),
            "user_type" : UserProfile.BASIC
        },
    ]

    for data in users:
        user, created = User.objects.get_or_create(username = data['username'])

        if created:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.password = data['password']
            user.is_staff = data['user_type'] == UserProfile.ADMIN
            user.is_superuser = data['user_type'] == UserProfile.ADMIN
            user.save()

            profile = UserProfile(
               user = User.objects.get(username=data['username']),
               user_type = data['user_type'],
            )
            profile.save()

if __name__ == '__main__':

    # dictionary linking each population function to a keyword
    models = {
        'article': populate_article,
        'distillery': populate_distillery,
        'gin': populate_gin,
        'review': populate_review,
        'user': populate_users,
        'wishlist': populate_wishlist
    }

    print("Starting population script...")

    if len(sys.argv) <= 1:
        # if no command line arguments, populate every model
        # note first cmd arg is 'populate_db.py'
        for key in models:
            models[key]();
        print("Successfully finished populating all models")
    else:
        # populate each model as specified from the command line arguments
        for arg in sys.argv:
            if not arg.endswith('.py') and models[arg]:
                # execute the function in the models dict corresponding to the keyword
                models[arg]()

        print("Successfully finished populating " + ", ".join(sys.argv[1:]))
