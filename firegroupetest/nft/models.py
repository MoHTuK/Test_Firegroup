from django.db import models
from django.urls import reverse


# Create your models here.

class NFT_obj(models.Model):

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, blank=True)

    image = models.ImageField(upload_to='images/%Y/%m/%d/')

    description = models.TextField(blank=True)
    count = models.IntegerField(default=1)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"NFT : {self.name}"

    def get_absolute_url(self):
        return reverse('nft:nft_detail', args=[self.slug])


class NFT_price(models.Model):

    nft = models.ForeignKey(NFT_obj, related_name='prices', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Price : {self.price} on {self.date}"
