# Ginthusiasm

To run the debug email server (for password resets):
* `python -m smtpd -n -c DebuggingServer localhost:1025`
* Go to /password-reset/ and enter an email address that matches a user in the databases
* Check the console running the email server, go to the link in the body of the email
* Reset your password in the form provided

See settings.py for email server config (ports etc)

## Social authentication references
To add social authentication functionality, we used the Python Social Auth - Django open-source library,
available [here](https://github.com/python-social-auth/social-app-django). To help with integrating this,
we followed 'How to Add Social Login to Django’ tutorial available [here](https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html).
Additionally, we followed another tutorial, available [here](http://javaguirre.me/2013/11/06/creating-a-user-profile-in-python-social-auth-in-django/),
to understand how to hook into the social authentication flow to create instances of our own
User and UserProfile classes.
