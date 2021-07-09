#!/usr/bin/env python3
import shutil
import psutil
import emails
import socket


def cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return not cpu_usage > 80


def disk_space():
    disk_usage = shutil.disk_usage("/")
    disk_total = disk_usage.total
    disk_free = disk_usage.used
    threshold = disk_free / disk_total * 100
    return threshold > 20


def available_memory():
    available = psutil.virtual_memory().available
    available_in_MB = available / 1024 ** 2  # MB
    return available_in_MB > 500


def localhost():
    local_host_ip = socket.gethostbyname('localhost')
    return local_host_ip == "127.0.0.1"


def warning_email(error):
    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = error
    body = "An error has been detected. Please resolve it.\n\nError: " + error

    message = emails.generate_email(sender, recipient, subject, body)

    emails.send(message)


if not cpu_usage():
    subject = "Error - CPU usage is over 80%"
    warning_email(subject)

if not disk_space():
    subject = "Error - Available disk space is less than 20%"
    warning_email(subject)

if not available_memory():
    subject = "Error - Available memory is less than 500MB"
    warning_email(subject)

if not localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    warning_email(subject)
