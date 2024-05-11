from django.urls import path
from . import views

app_name = 'nft'

urlpatterns = [

    path('', views.nft_list, name='nft_list'),
    path('<slug:slug>', views.nft_detail, name='nft_detail'),
]
