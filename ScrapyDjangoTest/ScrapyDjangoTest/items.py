# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from products.models import Product

class ScrapydjangotestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BrandsItem(DjangoItem):
   django_model = Product
   stock = scrapy.Field() # You can still add extra fields