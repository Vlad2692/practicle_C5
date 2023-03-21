import requests
import json
from config import keys, headers


class APIException(Exception):
    pass

class APIExceptionConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неудалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неудалось обработать количество {amount}')


        r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?to={quote_ticker}&from={base_ticker}&amount={amount}', headers=headers)

        result = json.loads(r.content)['result']

        return result



