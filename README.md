# Ginthusiasm

To run the debug email server (for password resets):
* `python -m smtpd -n -c DebuggingServer localhost:1025`
* Go to /password-reset/ and enter an email address that matches a user in the databases
* Check the console running the email server, go to the link in the body of the email
* Reset your password in the form provided

See settings.py for email server config (ports etc)
