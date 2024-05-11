import json
from django.shortcuts import render, get_object_or_404
from .models import NFT_obj, NFT_price


# Create your views here.
def nft_list(request):
    nfts = NFT_obj.objects.all()
    return render(request, 'post/list.html', {'nfts': nfts})


def nft_detail(request, slug):
    nft = get_object_or_404(NFT_obj, slug=slug)
    nft_prices = NFT_price.objects.filter(nft=nft)
    last_price = nft_prices.last()

    dates = [price.date.strftime("%Y-%m-%d") for price in nft_prices]
    prices = [str(price.price) for price in nft_prices]

    return render(request, 'post/detail.html', {'nft': nft, 'nft_prices': nft_prices, 'last_price': last_price,
                                                'dates': json.dumps(dates), 'prices': json.dumps(prices)})
