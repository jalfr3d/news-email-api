import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "SENDER_MAIL"
    # Reset pycharm in case of change or error in password
    password = os.getenv("PASSWORD")

    receiver = "YOUR_EMAIL"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


