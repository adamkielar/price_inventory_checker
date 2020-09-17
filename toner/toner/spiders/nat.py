import scrapy


class NatSpider(scrapy.Spider):
    name = 'nat'
    start_urls = ['https://www.x2p.pl/pl/list/tonery-oryginalne']

    def parse(self, response):
        items = response.css("div.ins-v-product-thumbnail.list")
        for item in items:
            sku = item.css("div.symbol").css("strong::text").get()
            price1 = item.css("div.price-net").css("span.price::text").get()
            price2 = item.css("div.price-net").css("span.decimal::text").get()
            stock = item.css("div.availability-text").css("div.d-inline-flex").css("span.text::text").get()
            yield {
                'sku': sku,
                'price': price1+price2,
                'stock': stock
            }
