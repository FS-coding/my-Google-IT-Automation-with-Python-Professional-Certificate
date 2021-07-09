#!/usr/bin/env python3
import email.message
import smtplib
import mimetypes
import os.path


def generate_email(sender, recipient, subject, body, attachment_path=None):
    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment_path != None:
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as files:
            message.add_attachment(files.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)
    return message


def send_email(message):
    mail_server = smtplib('localhost')
    mail_server.send_message(message)
    mail_server.quit()
