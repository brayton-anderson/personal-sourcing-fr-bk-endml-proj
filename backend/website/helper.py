import os
from flask_mail import Message
from website.utils.common import TokenGenerator
from . import mail


def send_forgot_password_email(request, user, code, token):
    current_site = request.url_root
    mail_subject = "Verification Code"
    domain = os.environ.get("API_URL")
    ml = os.environ.get("EMAIL_HOST_USER")
    print(domain)
    print(ml)
    print(user)
    print(token)
    print(code)
    msg = Message(
        mail_subject, sender=os.environ.get("EMAIL_HOST_USER"), recipients=[user]
    )
    msg.html = f"Please use the verification code as: {code}, or click this link: {domain}/pages/auth/reset-password/{user}/{token}"
    mail.send(msg)
