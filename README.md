# alert_on_bad_air_quality

A simple job designed to run inside a cron wrapper of some sort (pick your poison as each orchestrator/cloud provider has its own way of doing scheduled jobs nowadays) that will alert via telegram & email when it looks like it the air quality is bad then exit (it's not long-running as again it's designed to run inside a cron scheduler of some kind).

Github actions CI unit tests & auto dockerhub push status: [![CI/CD](https://github.com/naorlivne/alert_on_bad_air_quality/actions/workflows/full_ci_cd_workflow.yml/badge.svg)](https://github.com/naorlivne/alert_on_bad_air_quality/actions/workflows/full_ci_cd_workflow.yml)

Code coverage: [![codecov](https://codecov.io/gh/naorlivne/alert_on_bad_air_quality/branch/master/graph/badge.svg)](https://codecov.io/gh/naorlivne/alert_on_bad_air_quality)

# Running

The container will run with the following command, check the air quality API and alert if the AQI level is higher then `AQ_ALERT_LEVEL` (150 is the default, higher then that is considered unhealthy to be outside for long periods for everyone), It's designed to run under some cron scheduler (k8s, metronome/mesos or linux OS cron), below is the example command needed to run the container one off

```shell
docker run -e AQICN_API_KEY="my_token" -e CITY="Tel Aviv" -e SMTP_SERVER="smtp.gmail.com" -e SENDER_EMAIL="mymail@example.com" -e RECEIVER_EMAIL="mymail@example.com" -e EMAIL_PASSWORD="pass" -e EMAIL_PORT="465" -e TELEGRAM_TOKEN="my_token" -e CHAT_ID="123" naorlivne/alert_on_bad_air_quality
```

# Configuration options

alert_on_bad_air_quality uses sane defaults, but they can all be easily changed:

| value                  | envvar                 | default value          | notes                                                                                                  |
|------------------------|------------------------|------------------------|--------------------------------------------------------------------------------------------------------|
|  aqicn_api_key         | AQICN_API_KEY          |                        | You can get a free one at https://aqicn.org/api/                                                       |
|  city                  | CITY                   |                        | The city you want to be alerted should it air quality will go bad (make sure to check https://aqicn.org/api/ it's available first) |
| smtp_server            | SMTP_SERVER            |                        | SMTP server address which mail is sent through (SSL/TLS enabled)                                       |
| sender_email           | SENDER_EMAIL           |                        | Email address to send the alert out of                                                                 |
| receiver_email         | RECEIVER_EMAIL         |                        | Email address to send the alert to                                                                     |
| email_password         | EMAIL_PASSWORD         |                        | `sender_email` account password                                                                        |
| email_port             | EMAIL_PORT             |                        | SMTP server port                                                                                       |
| telegram_token         | TELEGRAM_TOKEN         |                        | Telegram API token                                                                                     |
| chat_id                | CHAT_ID                |                        | Telegram `chat_id` with the bot which you'll be alerted through                                        |
| aq_alert_level         | AQ_ALERT_LEVEL         | 150                    | the air quality level above which an alert will be triggered                                           |

The easiest way to change a default value is to pass the envvar key\value to the docker container with the `-e` cli arg but if you want you can also create a configuration file with the settings you wish (in whatever of the standard format you desire) & place it in the /www/config folder inside the container.

Most providers also allow setting their configuration access_keys\etc via envvars use `-e` cli args to configure them is ideal as well but should you wish to configure a file you can also easily mount\copy it into the container as well.
