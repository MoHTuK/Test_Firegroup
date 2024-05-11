from django.contrib import admin
from .models import NFT_obj, NFT_price


# Register your models here.
@admin.register(NFT_obj)
class NFTAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'count']
    list_filter = ['name', 'created']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NFT_price)
class NFTPriceAdmin(admin.ModelAdmin):
    list_display = ['nft', 'price', 'date']
    list_filter = ['date']
