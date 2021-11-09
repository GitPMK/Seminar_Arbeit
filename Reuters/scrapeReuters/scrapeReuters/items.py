# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class ScrapereutersItem(scrapy.Item):
    link = scrapy.Field()
    author = scrapy.Field()
    datum = scrapy.Field()
    text = scrapy.Field()
