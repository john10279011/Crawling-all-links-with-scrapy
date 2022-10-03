import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class sipwhiskey(CrawlSpider):
    name = 'whisky'
    start_urls = ['https://sipwhiskey.com/']
    
    rules = (
        Rule(LinkExtractor(allow='collections',deny='products')),
        Rule(LinkExtractor(allow='products'),callback = 'yield_item')
    )
        
    def yield_item(self,response):
        yield{
            'name': response.css('h1.title::text').get(),
            'price':response.css('span.price.theme-money::text').get().replace('$',''),
            'brand':response.css('div.vendor a::text').get()
        }