from django.core.mail import send_mail


def send_email_to_staff(name, message, email):
    send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            email,
            fail_silently=False)
