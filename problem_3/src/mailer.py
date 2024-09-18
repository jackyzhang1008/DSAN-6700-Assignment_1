from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from smtplib import SMTP


def send_email(sender, recipient, subject, body):
    """
    Sends an email using SMTP.

    Args:
        sender (str): Email address of the sender.
        recipient (str): Email address of the recipient.
        subject (str): Subject of the email.
        body (str): Body of the email.

    Returns:
        None
    """
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    if body is not None:
        msg.attach(MIMEText(body, "plain"))

    s = SMTP("localhost", 1025)
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()
