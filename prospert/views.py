from django.shortcuts import render
from newsapi import NewsApiClient
from yahoo_fin.stock_info import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os
# Create your views here.

def HomePage(request):
	#Currencies=get_currencies().head()
	TopGainers=get_day_gainers().head(10)
	TopLosers=get_day_losers().head(10)
	MostActive=get_day_most_active().head(10)


	TopGainers.rename(columns = {'Price (Intraday)':'Price','% Change':'Change_PCT'}, inplace = True)
	TopLosers.rename(columns = {'Price (Intraday)':'Price','% Change':'Change_PCT'}, inplace = True)
	MostActive.rename(columns = {'Price (Intraday)':'Price','% Change':'Change_PCT','Market Cap': 'Market'}, inplace = True)
	#Currencies.rename(columns = {'Last Price':'Price','% Change':'Change_PCT'}, inplace = True)

	table1 = TopGainers.set_index('Name').T.to_dict('dict')
	table2 = TopLosers.set_index('Name').T.to_dict('dict')
	table3 = MostActive.set_index('Name').T.to_dict('dict')
	#table4 = Currencies.set_index('Name').T.to_dict('dict')
	context = {
		'table1' : table1,
		'table2' : table2,
		'table3' : table3,
		#'table4' : table4
	}
	return render(request,'homePage.html',context)

@login_required(login_url='Login')
def feedPage(request):
	apikey = os.environ.get("SECRET")
	print(type(apikey))
	feedApi = NewsApiClient(apikey)
	headlines = feedApi.get_top_headlines(category='business',country='in')
	articles = headlines['articles']
	context = {'articles':articles}
	return render(request, 'feedPage.html',context)
