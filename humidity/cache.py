import redis
import json


class RedisCache:

    def __init__(self, host, port):
        self.cache = redis.Redis(host=host, port=port)
        self._init_humidity_cache()

    def _init_humidity_cache(self):
        """Init empty cache"""
        init_struct = {'yandex': [], 'accuweather': [], 'owm': []}
        self.cache.set('humidity', json.dumps(init_struct))

    def set_humidity(self, data_list):
        """Set humidity data to cache
        :param data_list: Contain data from different services
        """

        # Get data from cache
        humidity_data = json.loads(self.cache.get('humidity'))
        print(data_list)
        # Update cache
        for data in data_list:
            cached_data = humidity_data[data['source']]

            # Save 5 last values
            if len(cached_data) >= 5:
                cached_data.pop(0)
            cached_data.append(data)

            humidity_data[data['source']] = cached_data
        return self.cache.set('humidity', json.dumps(humidity_data))

    def get_humidity(self):
        """Get data from cache"""
        return self.cache.get('humidity')


cache = RedisCache('redis', 6379)
