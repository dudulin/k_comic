import scrapy
from ..items import KkkspiderItem

from ..middlewares import ip_list


class KkkSpider2(scrapy.Spider):
    # 这个 name 是 scrapy crawl {name}   是项目运行的 key
    name = 'kkk'
    allowed_domains = ['https://www.1kkk.com/']
    start_urls = ['http://https://www.1kkk.com//']
    page_url = r'https://www.1kkk.com/manhua-list-area36-s2-p{}/'

    def parse(self, response):
        lists = response.xpath('//div[@class="mh-item"]')
        for i in lists:
            items = KkkspiderItem()
            items['title'] = i.xpath('.//h2/a/text()').get()

            items['image_urls'] = [i.xpath('./p/@style').get().replace('background-image: url(', '').replace(')', '')]
            print(items, 'ss')
            yield items  # 发送给pipe 管道处理

    def start_requests(self):
        for i in range(1, 3):
            url = self.page_url.format(i)
            yield scrapy.Request(url=url, callback=self.parse)
