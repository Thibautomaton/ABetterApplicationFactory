from app import mail
from threading import Thread
from flask_mail import Message
from flask import render_template, current_app


def send_mail_async(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, template, to, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['APP_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['APP_MAIL_SENDER'],
                  recipients=[to])
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_mail_async(), args=[app, msg])
    thr.start()
    return thr
