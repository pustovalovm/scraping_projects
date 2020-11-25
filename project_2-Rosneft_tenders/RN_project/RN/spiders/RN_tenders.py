import scrapy


class RnTendersSpider(scrapy.Spider):
    name = 'RN_tenders'
    allowed_domains = ['zakupki.rosneft.ru']
    start_urls = ['http://zakupki.rosneft.ru/zakupki/']

    def parse(self, response):
        rows = response.xpath(
            "//table[contains(@class,'views-table')]/tbody/tr")
        for tr in rows:
            id_num = tr.xpath(".//td[1]/text()").get().strip()
            tender_id = tr.xpath(".//td[2]/a/text()").get().strip()
            tender_link = tr.xpath(".//td[2]/a/@href").get()
            legal_entity = tr.xpath(".//td[3]/text()").get().strip()
            tender_title = tr.xpath(".//td[4]/a/text()").get().strip()
            purchase_stage = tr.xpath(".//td[5]/text()").get().strip()
            published_date = tr.xpath(".//td[6]/text()").get().strip()
            submission_deadline = tr.xpath(".//td[7]/span/text()").get().strip()
            purchase_class = tr.xpath(".//td[8]/text()").get().strip()
            yield response.follow(url=tender_link, callback=self.parse_tender,
                                  meta={'id_num': id_num,
                                        'tender_id': tender_id,
                                        'tender_link': tender_link,
                                        'legal_entity': legal_entity,
                                        'tender_title': tender_title,
                                        'purchase_stage': purchase_stage,
                                        'published_date': published_date,
                                        'submission_deadline': submission_deadline,
                                        'purchase_class': purchase_class
                                        })
        next_url = response.xpath(
            ".//a[contains(@title, 'На следующую страницу')]/@href").get()
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_tender(self, response):
        tender_table = response.xpath(
            "//table[@class = 'tender-table']")[0].xpath(".//tbody/tr")
        tektorg_link = 'Not specified'
        for tr in tender_table:
            if tr.xpath(".//td[contains(text(), 'Сведения о начальной')]"):
                initial_max_price = tr.xpath(".//td[2]/div/text()").get().strip()
            if tr.xpath(".//td[contains(text(), 'Ссылка')]"):
                tektorg_link = tr.xpath(".//td[2]/div/a/@href").get()
        yield {'id_num': response.request.meta['id_num'],
               'tender_id': response.request.meta['tender_id'],
               'tender_link': response.request.meta['tender_link'],
               'legal_entity': response.request.meta['legal_entity'],
               'tender_title': response.request.meta['tender_title'],
               'purchase_stage': response.request.meta['purchase_stage'],
               'published_date': response.request.meta['published_date'],
               'submission_deadline': response.request.meta['submission_deadline'],
               'purchase_class': response.request.meta['purchase_class'],
               'initial_max_price': initial_max_price,
               'tektorg_link': tektorg_link
               }
