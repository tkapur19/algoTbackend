import requests
import pandas as pd


class Data:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_data(self, start_date, ticker, end_date, freq='daily'):
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'frequency': freq
        }
        response = requests.get(
                'https://www.quandl.com/api/v3/datasets/WIKI/{}/data.json?api_key={}'
                .format(ticker, self.api_key), params).json()

        data = pd.DataFrame(response['dataset_data']['data'],
                            columns=[x.lower() for x in response['dataset_data']['column_names']]).sort_values('date').set_index('date')

        data.index = pd.to_datetime(data.index)
        return data


