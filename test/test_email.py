from unittest import TestCase, mock
from alert_on_bad_air.functions.alerts.email import *


class BaseTests(TestCase):

    @mock.patch("smtplib.SMTP_SSL")
    def test_email(self, mock_smtp):
        email_alert("localhost", "sender_email@test.com", "receiver_email@test.com", "password", "bad air quality", 1025)
        message = '''Subject: Bad air quality

    This message is to alert you it looks like it there is bad air quality.
    '''
        mock_smtp.return_value.sendmail.assert_called_once_with("sender_email@test.com", "receiver_email@test.com",
                                                                message)
