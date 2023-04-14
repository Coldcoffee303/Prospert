from django.shortcuts import render
from django.http import HttpResponse
from yahoo_fin.stock_info import *

# Create your views here.

def stocks_Homepage(request):
	stock_picker = tickers_nifty50()
	context = {'stocklist':stock_picker}
	return render(request,'stockapp/homestock.html',context)
def get_stock(request):
	stock = request.GET.get('stockpicker')
	print(stock)
	available_stocks = tickers_nifty50()
	if stock in available_stocks:
		pass
	else:
		return HttpResponse('Error')
	details = get_quote_table(stock)
	context =  {
		'stock':stock,
		'Open':float(details['Open']),
		'Close':float(details['Previous Close']),
		'Price':round(float(details['Quote Price']),3),
		'Market':details['Market Cap'],
		'Volume':details['Volume']
	}
	print(type(details))
	return render(request,'stockapp/getStock.html',context)