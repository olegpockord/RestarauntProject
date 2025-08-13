from celery import shared_task

from feedback.utils import send_email_to_staff


@shared_task
def send_email_to_staff_task(name, message, email):

    return send_email_to_staff(name, message, email)

