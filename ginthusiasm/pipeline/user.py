from django.contrib.auth.models import User

from ginthusiasm.models import UserProfile, Wishlist


def create_user(strategy, details, response, user=None, *args, **kwargs):
    if user:
        user = User.objects.get(username=details['username'])
        user_profile = getattr(user, 'userprofile', None)

        if user_profile is None:
            user.first_name = details['first_name']
            user.last_name = details['last_name']
            user.email = details['email']
            user.password = ''
            user.user_type = UserProfile.BASIC
            user.is_staff = False
            user.is_superuser = False
            user.save()

            profile = UserProfile(
               user=user,
               user_type=UserProfile.BASIC,
            )
            profile.save()

            wishlist = Wishlist(user=profile)
            wishlist.save()
