from django.shortcuts import render
from django.http import HttpResponse
from yahoo_fin.stock_info import *
import simplejson as json
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
@login_required(login_url='Login')
def stocks_Homepage(request):
	stock_picker = tickers_nifty50()
	context = {'stocklist':stock_picker}
	return render(request,'stockapp/homestock.html',context)


@login_required(login_url='Login')
def get_stock(request):
	stock = request.GET.get('stockpicker')
	available_stocks = tickers_nifty50()
	if stock in available_stocks:
		pass
	else:
		return HttpResponse('Error')
	details = get_quote_table(stock)

	today = datetime.date.today()
	month_age = today - datetime.timedelta(days=30)
	data = get_data(stock,start_date=month_age,end_date=today)
	data['date'] = pd.to_datetime(data.index)

	context = {
		'data1' : {
			'Label' : list(data['date'].dt.strftime('%m/%d/%Y')),
			'Values' : list(data['close'])
		},
		'data2' : {
			'Stock':stock[0],
			'Open':float(details['Open']),
			'Close':float(details['Previous Close']),
			'Price':round(float(details['Quote Price']),3),
			'Market':details['Market Cap'],
			'Volume':details['Volume'],
		},
		'room_name':'track'
	}
	return render(request,'stockapp/getStock.html',context)