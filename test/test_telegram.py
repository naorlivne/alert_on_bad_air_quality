from unittest import TestCase
from alert_on_bad_air.functions.alerts.telegram import *
import requests_mock


class BaseTests(TestCase):

    def test_telegram_init(self):
        telegram_object = Telegram("123:now_with_colon")
        self.assertEqual(telegram_object.bot.token, "123:now_with_colon")

    def test_telegram_send_alert(self):
        with requests_mock.Mocker() as request_mocker:
            request_mocker.post('https://api.telegram.org/123:now_with_colon/sendMessage?chat_id=123'
                                '&text=Subject%3A+Bad+air+quality%0A%0A++++++++++++This+message+is+to+alert+you+it+'
                                'looks+like+there+is+bad+air+quality.%0A++++++++++++',
                                status_code=200, text='{"ok":true,"result":{"message_id":85,"from":{"id":123,'
                                                      '"is_bot":true,"first_name":"blabla",'
                                                      '"username":"blablason"},"chat":{'
                                                      '"id":123,"first_name":"blabla","last_name":"son",'
                                                      '"username":"Naorlivne","type":"private"},"date":123,'
                                                      '"text":"test api is working"}}')
            telegram_object = Telegram("123:now_with_colon")
            reply = telegram_object.send_alert("123", "bad air quality")
            self.assertTrue(reply.json['from']['is_bot'])
