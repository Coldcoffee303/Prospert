from django.shortcuts import render
from django.http import HttpResponse
from yahoo_fin.stock_info import *
import simplejson as json
# Create your views here.

def stocks_Homepage(request):
	stock_picker = tickers_nifty50()
	context = {'stocklist':stock_picker}
	return render(request,'stockapp/homestock.html',context)
def get_stock(request):
	stock = request.GET.get('stockpicker')
	available_stocks = tickers_nifty50()
	if stock in available_stocks:
		pass
	else:
		return HttpResponse('Error')
	details = get_quote_table(stock[0])
	print(type(details))
	context =  {
		'stock':stock[0],
		'Open':float(details['Open']),
		'Close':float(details['Previous Close']),
		'Price':round(float(details['Quote Price']),3),
		'Market':details['Market Cap'],
		'Volume':details['Volume'],
		'room_name':'track'
	}
	return render(request,'stockapp/getStock.html',context)