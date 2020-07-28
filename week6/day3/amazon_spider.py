import scrapy
from ..items import ItemsamazonSpider
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
#PRUEBA4
class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.es/Tommy-Hilfiger-UM0UM00054-Camiseta-Hombre/dp/B01MYD0T1F/ref=sr_1_1?dchild=1&pf_rd_p=58224bec-cac9-4dd2-a42a-61b1db609c2d&pf_rd_r=VZQ1JTQXFVRZ9E9VSKX4&qid=1595364419&s=apparel&sr=1-1']

    def parse(self, response):
        items = ItemsamazonSpider()

        item_name = response.css(['productTitle::text']).extract()
        item_price = response.css('priceblock_ourprice , title , imgTagWrapperId').css('::text').extract()
        pass
