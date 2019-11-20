
"""Load humidity data from different sources"""

import json
import requests
import time
from cache import cache

# Key for yandex weather API
YANDEX_KEY = "#"

# Key for accuweather API
ACCUWEATHER_KEY = "#"

# Key for open weather map API
OWM_KEY = "#"


def yandex_humidity():
    """Get information from yandex and return necessary data"""

    api_url = "https://api.weather.yandex.ru/v1/forecast?lat=55.75396&lon=37.620393&lang={ru_RU}&hours=false"
    response = requests.get(api_url, headers={"X-Yandex-API-Key": YANDEX_KEY})
    if response.status_code == 200:
        data = json.loads(response.text)
        result = {
            'timestamp': data['fact']['obs_time'],  # Time of data calculation
            'humidity': data['fact']['humidity'],
            'source': 'yandex'
        }
        return result

    # Print status of failed request
    print('yandex code: ', response.status_code)


def accuweather_humidity():
    """Get information from accuweather and return necessary data"""

    api_url = f'http://dataservice.accuweather.com/currentconditions/v1/294021?apikey={ACCUWEATHER_KEY}&language=ru&details=true'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = json.loads(response.text)[0]
        result = {
            # Datetime of the current observation
            'timestamp': data['EpochTime'],  # Time of the current observation
            'humidity': data['RelativeHumidity'],
            'source': 'accuweather'
        }
        return result

    # Print status of failed request
    print('accuweather code: ', response.status_code)


def owm_humidity():
    """Get information from open weather map and return necessary data"""
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID={OWM_KEY}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        result = {
            'timestamp': data['dt'],  # Time of data calculation
            'humidity': data['main']['humidity'],
            'source': 'owm'
        }
        return result

    # Print status of failed request
    print('open weather map code: ', response.status_code)


def demand():
    """
    Request different resources with a periodicity of 30 seconds
    """
    humidity_functions = [yandex_humidity, accuweather_humidity, owm_humidity]

    while True:
        humidity_data = []
        for func in humidity_functions:
            data = func()
            if data is not None:
                humidity_data.append(data)

        cache.set_humidity(humidity_data)
        time.sleep(30)


demand()
