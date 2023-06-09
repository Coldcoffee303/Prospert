from celery import shared_task
from yahoo_fin.stock_info import *
from channels.layers import get_channel_layer
import asyncio
import simplejson as json
from django.http import HttpResponse
import datetime

@shared_task(bind=True)
def update_stock(self,stock):
	available_stocks = tickers_nifty50()
	if stock in available_stocks:
		pass
	else:
		pass

	today = datetime.date.today()
	month_age = today - datetime.timedelta(days=30)
	data = get_data(stock,start_date=month_age,end_date=today)
	data['date'] = pd.to_datetime(data.index)
	details = get_quote_table(stock)
	context = {
		'data1' : {
			'Label' : list(data['date'].dt.strftime('%m/%d/%Y')),
			'Values' : list(data['close'])
		},
		'data2' : {
			'Stock':stock,
			'Open':float(details['Open']),
			'Close':float(details['Previous Close']),
			'Price':round(float(details['Quote Price']),3),
			'Market':details['Market Cap'],
			'Volume':details['Volume'],
		},
		'room_name':'track'
	} 

	# send data to group
	channel_layer = get_channel_layer()
	loop = asyncio.new_event_loop()

	asyncio.set_event_loop(loop)
	loop.run_until_complete(channel_layer.group_send('stock_track', {
		'type' : 'send_stock_update',
		'message': context,
	}))

	return 'Done'
