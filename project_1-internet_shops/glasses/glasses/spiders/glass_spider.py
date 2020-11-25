import scrapy


class GlassSpiderSpider(scrapy.Spider):
    name = 'glass_spider'
    allowed_domains = ['www.glassesshop.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.glassesshop.com/bestsellers/',
                             callback=self.parse,
                             headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'})

    def parse(self, response):
        for glasses in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item']"):
            yield {'product_name': glasses.xpath(".//div[@class='p-title']/a/@title").get(),
                   'product_url': glasses.xpath(".//div[@class='p-title']/a/@href").get(),
                   'product_image_link': glasses.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@data-src").get(),
                   'product_price': glasses.xpath(".//div[@class='p-price']/div/span/text()").get()
                   }

        next_url = response.xpath(
            "//a[@class='page-link' and @rel='next']/@href").get()
        if next_url:
            yield scrapy.Request(url=next_url,
                                 callback=self.parse,
                                 headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'})
