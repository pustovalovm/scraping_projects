import scrapy
from scrapy_splash import SplashRequest

class QuotesJsSpider(scrapy.Spider):
    name = 'quotes_js'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/js/']
    script = '''
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            splash:set_viewport_full()
            return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url='https://quotes.toscrape.com/js/',
                            callback=self.parse,
                            endpoint='execute',
                            args={'lua_source': self.script})

    def parse(self, response):
        for quote in response.xpath("//div[@class = 'quote']"):
            tags = []
            for tag in quote.xpath(".//div/a"):
                tags.append(tag.xpath(".//text()").get())
            yield {
                'text': quote.xpath(".//span[1]/text()").get(),
                'by': quote.xpath(".//span[2]/small/text()").get(),
                'tags': tags
            }
        next_url = response.xpath("//li[@class = 'next']/a/@href").get()
        if next_url:
            req = SplashRequest(url='https://quotes.toscrape.com'+next_url,
                    callback=self.parse,
                    endpoint='execute',
                    args={'lua_source': self.script})
            yield req
