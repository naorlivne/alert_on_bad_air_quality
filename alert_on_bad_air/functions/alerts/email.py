import smtplib
import ssl


def email_alert(smtp_server: str, sender_email: str, receiver_email: str, password: str, alert_type: str,
                port: int = 465):
    """
    Will send an email alert saying there is bad air quality

    Arguments:
        :param port: The SMTP server port, default to 465 for SSL
        :param alert_type: the type of alert, can be 'rain' or 'storm'
        :param smtp_server: The SMTP server URL
        :param sender_email: The sender email address
        :param receiver_email: The receiver email address
        :param password: The SMTP pass
    """
    password = str(password)
    message = """Subject: {alert_type_capitalized}

    This message is to alert you it looks like it there is {alert_type}.
    """.format(alert_type_capitalized=alert_type.capitalize(), alert_type=alert_type)

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context=context)
    server.login(sender_email, password)
    email_result = server.sendmail(sender_email, receiver_email, message)
    return email_result
