import requests
import json
from config import keys

class ApiException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ApiException(f'одинаковые значения {base}')

        try:
            quote_ticker = keys[quote]
        except  KeyError:
            raise ApiException(f'Неправельнные данные {quote}')

        try:
            base_ticker = keys[base]
        except  KeyError:
            raise ApiException(f'Неправельнные данные {base}')

        try:
            amount = float(amount)
        except  ValueError:
            raise ApiException(f'Неправельнные данные количество {quote}')

        url = f"https://api.apilayer.com/fixer/convert?to={quote_ticker}&from={base_ticker}&amount={amount}"
        headers = {"apikey": "wjfG3OLSfyzzgJcjV9ivRE35aTaEcQoc"}
        response = requests.request("GET", url, headers=headers)
        total_base = json.loads(response.content)['result']

        return total_base