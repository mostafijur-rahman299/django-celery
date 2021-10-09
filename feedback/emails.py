from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_feedback_email(email, message):
    subject, from_email, to_email = 'Email Test',settings.FROM_EMAIL, [email]
    text_content = 'This is an important message.'
    to_email = str(to_email[0])

    mail = EmailMultiAlternatives(subject, text_content, from_email, [to_email,])
    
    context = {
		'message': message
	}
	
    html_content = render_to_string('feedback/email/test-mail.html', context) 

    mail.attach_alternative(html_content, "text/html")
    return mail.send()
