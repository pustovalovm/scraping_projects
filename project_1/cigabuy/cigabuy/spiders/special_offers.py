import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html', callback=self.parse,
                             headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'})

    def parse(self, response):
        for product in response.xpath("//div[@class='p_box_wrapper']"):
            yield {
                'title': product.xpath(".//div/a[@class='p_box_title']/text()").get(),
                'url': product.xpath(".//div/a[@class='p_box_title']/@href").get(),
                'discounted_price': product.xpath(".//div/div[@class='p_box_price cf']/span[1]/text()").get(),
                'original_price': product.xpath(".//div/div[@class='p_box_price cf']/span[2]/text()").get()
            }
        next_page_url = response.xpath("//a[@class = 'nextPage']/@href").get()

        if next_page_url:
            yield scrapy.Request(url=next_page_url,
                                 callback=self.parse,
                                 headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'})
