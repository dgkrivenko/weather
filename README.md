# weather
Небольшой сервис, котороый запрашивает информацию о влажности воздуха в Мосвке из трех различных источников.
Последние 5 значений кэшируются и отдаются по единому REST-ендпоинту.
Каждое значение это (timestamp: long, humidity: float, source: str)