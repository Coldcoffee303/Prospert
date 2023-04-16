from django.urls import path
from . import views
urlpatterns = [
    path('',views.stocks_Homepage,name='stocks'),
    path('getStock/',views.get_stock,name='getStock'),
]