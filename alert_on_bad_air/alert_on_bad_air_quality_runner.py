from parse_it import ParseIt
from alert_on_bad_air.functions.air_quality.aqi import *
from alert_on_bad_air.functions.alerts.email import *
from alert_on_bad_air.functions.alerts.telegram import *


def init():
    """
    Run the logic which will take the variables (OWM api key & location) no matter how they are provided and will alert
    if it looks like it will rain there tomorrow
    """
    parser = ParseIt(recurse=False, config_type_priority=["envvars"])
    aqicn_api_key = parser.read_configuration_variable("aqicn_api_key", required=True)
    city = parser.read_configuration_variable("city", required=True)
    smtp_server = parser.read_configuration_variable("smtp_server", required=True)
    sender_email = parser.read_configuration_variable("sender_email", required=True)
    receiver_email = parser.read_configuration_variable("receiver_email", required=True)
    email_password = parser.read_configuration_variable("email_password", required=True)
    email_port = parser.read_configuration_variable("email_port", required=True)
    telegram_token = parser.read_configuration_variable("telegram_token", required=True)
    chat_id = parser.read_configuration_variable("chat_id", required=True)
    aq_alert_level = parser.read_configuration_variable("aq_alert_level", default_value=150)

    telegram_object = Telegram(telegram_token)

    current_air_quality = air_quality_index(aqicn_api_key, city)
    if current_air_quality > aq_alert_level:
        print("air quality is bad! air quality is " + str(current_air_quality))
        telegram_object.send_alert(chat_id, "bad air quality")
        email_alert(smtp_server, sender_email, receiver_email, email_password, "bad air quality", email_port)
        print("air quality alert sent")
    else:
        print("air quality is ok, air quality is " + str(current_air_quality))
