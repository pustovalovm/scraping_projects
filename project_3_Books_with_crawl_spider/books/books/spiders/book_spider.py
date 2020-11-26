import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpiderSpider(CrawlSpider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='http://books.toscrape.com/', headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths=r'//h3/a'),
            callback='parse_item',
            follow=True,
            process_request='set_user_agent'),
        Rule(LinkExtractor(
            restrict_xpaths=r"//li[@class = 'next']/a"),
            process_request='set_user_agent')
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        rating = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        item = {
            'name': response.xpath("//h1/text()").get(),
            'price': response.xpath("//p[@class = 'price_color']/text()").get(),
            'rating': rating[response.xpath("//div[@class='col-sm-6 product_main']/p[contains(@class, 'star-rating')]/@class").get().split()[1]],
            'image': response.xpath("//div[@class='item active']/img/@src").get(),
        }

        yield item
