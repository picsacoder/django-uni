from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

def formContact(req):
    return render(req, 'contactForm.html')

def contacting(req):
    if req.method == 'POST':
        subject = req.POST['subject']
        email = req.POST['email']
        message = req.POST['message'] + "\n {}".format(email)
        emailFrom = settings.EMAIL_HOST_USER
        emailTo = ['email']

        send_mail(subject, message ,emailFrom, emailTo, fail_silently=False)
        return render(req, 'contactForm.html')