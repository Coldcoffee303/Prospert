from django.shortcuts import render
from newsapi import NewsApiClient
import os
# Create your views here.

def feedPage(request):
	apikey=os.environ.get('NEWSAPI')
	print(type(apikey))
	feedApi = NewsApiClient(api_key=apikey)
	headlines = feedApi.get_top_headlines(category='business',country='in')
	articles = headlines['articles']
	context = {'articles':articles}
	return render(request, 'feedPage.html',context)  