import scrapy

#PRUEBA4
class ItemsamazonSpider(scrapy.Spider):
    item_name = 'Scrapy Field'
    item_price = 'Scrapy Field'

    
    def parse(self, response):
        pass
