import requests
import datetime
from pytoque.utils import get_url, filter_data
from pytoque.validators import validate_date, validate_filters

class PyToque:
    def __init__(self, api_key: str):
        if not api_key:
            raise Exception('Please provide an api_key')

        if type(api_key) != str:
            raise TypeError('Please provide a correct api_key')

        self.headers = {
            'Authorization': f'Bearer {api_key}'
        }

    def get_today(self, filters: list = None) -> dict:
        if filters:
            if not validate_filters(filters):
                raise Exception('Incorrect filters')

        date = datetime.date.today()

        url = get_url(date)

        try:
            response = requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise e

        if response.status_code != 200:
            raise Exception(f'The response was not satisfactory, HTTP STATUS: {response.status_code}')

        data: dict = response.json()

        if not filters:
            return data

        data = data.get('tasas')

        return filter_data(data, filters)

    def get_date(self, date: str, filters: list = None) -> dict:
        if filters:
            if not validate_filters(filters):
                raise Exception('Incorrect filters')

        if not validate_date(date):
            raise Exception('Please provide a date in format "YYYY-MM-DD"')

        url = get_url(date)

        try:
            response = requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise e

        if response.status_code != 200:
            raise Exception(f'The response was not satisfactory, HTTP STATUS: {response.status_code}')

        data: dict = response.json()

        if not filters:
            return data

        data = data.get('tasas')

        return filter_data(data, filters)
