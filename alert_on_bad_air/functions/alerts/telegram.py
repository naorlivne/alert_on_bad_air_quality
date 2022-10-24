import telebot


class Telegram:

    def __init__(self, telegram_token):
        """
        Will create a telegram object

        Arguments:
            :param telegram_token: the telegram token
        """

        self.bot = telebot.TeleBot(telegram_token)

    def send_alert(self, chat_id, alert_type):
        """
        Will send an alert about the bad air quality via telegram

        Arguments:
            :param chat_id: the id of the telegram chat to send alerts to
            :param alert_type: the type of alert to send, can be 'rain' or 'storm'
        Returns:

        """

        message = """Subject: {alert_type_capitalized}

            This message is to alert you it looks like there is {alert_type}.
            """.format(alert_type_capitalized=alert_type.capitalize(), alert_type=alert_type)

        return self.bot.send_message(chat_id, message)
