from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd
from . import backtest, ticker_data


def index(request):
    template = loader.get_template('new_form.html')
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
        ticker = request.GET.get('ticker')

        start_date = start_year+'-'+start_month+'-'+start_day
        end_date = end_year + '-' + end_month + '-' + end_day
        ohlcv = ticker_data.Data('U93z8Z-2erhNJgpJ1mNy').get_data(start_date, ticker, end_date, 'daily')
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
        return render(request, 'summary.html', {'content': test.run_backtest(number_of_share)})
