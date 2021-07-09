#!/usr/bin/env python3
import os
import datetime
import reports
import emails

current_date = datetime.datetime.now().strftime("%Y-%m-%d")


def generate_pdf(path):
    pdf = ""
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(path + file, 'r') as f:
                inline = f.readlines()
                name = inline[0].strip()
                weight = inline[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"

    return pdf


if __name__ == "__main__":
    # info given
    path = "supplier-data/descriptions/"
    title = "Report " + current_date
    attachment = "/tmp/processed.pdf"

    data = generate_pdf(path)

    # generate report
    reports.generate_report(attachment, title, data)

    # generate_email info:
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/report.pdf"

    message = emails.generate_email(
        sender, recipient, subject, body, attachment_path)

    emails.send(message)
