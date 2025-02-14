from requests import request

from API_KEYS.get_key import get_key


class Weather:

    def __init__(self,
                 url='https://api.openweathermap.org/data/2.5/weather'):

        self.response = None
        self.__api_key = get_key('WEATHER_KEY.txt')
        self.__url = url
        self.last_weather = ''

    def _get_request(self, city: str) -> None:

        params = {
            'q': city,
            'appid': self.__api_key,
            'units': 'metric',
            'lang': 'ru'
        }
        self.response = request('GET', self.__url, params=params).json()

    @staticmethod
    def _get_wind_direction(degrees: int) -> str:
        if 0 <= degrees <= 23 or 337 < degrees <= 360:
            return 'северный'
        elif 23 < degrees <= 67:
            return 'северо-восточный'
        elif 67 < degrees <= 113:
            return 'восточный'
        elif 113 < degrees <= 157:
            return 'юго-восточный'
        elif 157 < degrees <= 203:
            return 'южный'
        elif 203 < degrees <= 247:
            return 'юго-западный'
        elif 247 < degrees <= 293:
            return 'западный'
        elif 293 < degrees <= 337:
            return 'северо-западный'

    def get_weather(self, city: str) -> str:

        self._get_request(city)
        if self.response['cod'] == '404':
            self.last_weather = 'Город не найден. Попробуйте ещё раз.'
            return self.last_weather

        self.last_weather = (f"_____ {self.response['name']} _____\n"
                             f"Cейчас: {self.response['weather'][0]['description']}.\n"
                             f"Температура воздуха: {self.response['main']['temp']:.1f} ℃.\n"
                             f"Ощущается как: {self.response['main']['feels_like']:.1f} ℃.\n"
                             f"Ветер {self._get_wind_direction(self.response['wind']['deg'])}, {self.response['wind']['speed']:.1f} м\с.")

        return self.last_weather
