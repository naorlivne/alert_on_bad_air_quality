# it's offical so i'm using it + alpine so damn small
FROM python:3.10.0b2-alpine3.12

# set python to be unbuffered
ENV PYTHONUNBUFFERED=1

# install requirements
COPY requirements.txt /alert_on_bad_air_quality/requirements.txt
RUN pip install -r /alert_on_bad_air_quality/requirements.txt

# copy the codebase
COPY . /alert_on_bad_air_quality
RUN chmod +x /alert_on_bad_air_quality/alert_on_bad_air_quality.py

# and running it
WORKDIR /alert_on_bad_air_quality
CMD ["python", "/alert_on_bad_air_quality/alert_on_bad_air_quality.py"]
