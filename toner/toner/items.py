import scrapy


class TonerItem(scrapy.Item):
    skus = scrapy.Field()
    price1 = scrapy.Field()
    price2 = scrapy.Field()
    stock = scrapy.Field()
