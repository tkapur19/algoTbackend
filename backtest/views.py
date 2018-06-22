from django.http import HttpResponse
from django.template import loader
import pandas as pd
from . import backtest

def index(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render())


def submit(request):
    if request.method == 'GET':
        capital = int(request.GET.get('capital'))
        initial_share = int(request.GET.get('Initial share'))
        number_of_share = int(request.GET.get('Number of share'))
        start_day = request.GET.get('start-day')
        start_month = request.GET.get('start-month')
        start_year = request.GET.get('start-year')
        end_day = request.GET.get('end-day')
        end_month = request.GET.get('end-month')
        end_year = request.GET.get('end-year')

        start_date = start_year+'-'+start_month+'-'+start_day
        end_date = end_year + '-' + end_month + '-' + end_day
        ohlcv = pd.read_csv('/Users/vidur/dev/finance/algotbackend/backtest/daily_TSLA.csv'
                            , parse_dates=['timestamp']).sort_values('timestamp').set_index('timestamp')
        test = backtest.Backtest(ohlcv,
                                 capital,
                                 start_date,
                                 end_date,
                                 initial_share,
                                 algo='moving_average',
                                 params={
                                     'swindow': 20,
                                     'lwindow': 100
                                 })
        print(test.run_backtest(number_of_share))

    return HttpResponse("submission successful")
