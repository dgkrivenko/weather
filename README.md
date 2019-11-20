# weather
В рамках тестового задания необходимо реализовать 
сервер на Flask, который с частотой в 30 секунд собирает информацию об относительной влажности (в %) в Москве из источников:
1.      https://yandex.ru/pogoda
2.      https://www.accuweather.com/ru/
3.      https://openweathermap.org
 
Этот сервер кэширует последние 5  значений (для каждого источника) и отдавать их по одному-единственному REST-ендпоинту.
Каждое значение это (timestamp: long, humidity: float, source: str)
Сервис работает в docker-контейнерах

Технологический стек: Python/Flask, Docker
