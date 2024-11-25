import requests
import datetime
from utils import validate_date

class PyToque:
    def __init__(self, api_key: str):
        if not api_key:
            raise Exception('Please provide an api_key')

        if type(api_key) != str:
            raise TypeError('Please provide a correct api_key')

        self.headers = {
            'Authorization': f'Bearer {api_key}'
        }

    def get_today(self) -> dict:
        date = datetime.date.today()

        url = f"https://tasas.eltoque.com/v1/trmi?date_from={date}%2000%3A00%3A01&date_to={date}%2023%3A59%3A01"

        try:
            response = requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise e

        if response.status_code != 200:
            raise Exception(f'The response was not satisfactory, HTTP STATUS: {response.status_code}')

        data = response.json()

        return data

    def get_date(self, date: str) -> dict:
        if not validate_date(date):
            raise Exception('Please provide a date in format "YYYY-MM-DD"')

        url = f"https://tasas.eltoque.com/v1/trmi?date_from={date}%2000%3A00%3A01&date_to={date}%2023%3A59%3A01"

        try:
            response = requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            raise e

        if response.status_code != 200:
            raise Exception(f'The response was not satisfactory, HTTP STATUS: {response.status_code}')

        data = response.json()

        return data

