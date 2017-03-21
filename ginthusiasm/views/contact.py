from django.shortcuts import render

from ginthusiasm.forms import ContactForm

"""
Renders the contact form, and sends information from the contact form to the database
"""


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            context = {
                'success': True,
                'message': 'We\'ve received your message successfully, thank you. We will get in touch as soon as possible.'
            }
            return render(request, 'ginthusiasm/contact.html', context)

    else:
        context = {
            'contact_form': ContactForm(),
        }
        return render(request, 'ginthusiasm/contact.html', context)
