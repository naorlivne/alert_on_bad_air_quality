from cachetools import cached, TTLCache
import requests


@cached(cache=TTLCache(maxsize=32, ttl=60))
def air_quality_index(api_key: str, city: str) -> int:
    """
    Returns current air quality

    Arguments:
        :param api_key: the aqicn api key
        :param city: the city to check the air quality in it

    Returns:
        :return bool, True if it will be rainy, False otherwise

    """
    url = "http://api.waqi.info/feed/" + city + "/?token=" + api_key

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()['data']['aqi']
