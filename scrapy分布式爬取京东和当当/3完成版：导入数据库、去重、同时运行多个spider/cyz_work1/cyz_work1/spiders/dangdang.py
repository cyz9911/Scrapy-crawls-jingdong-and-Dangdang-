import scrapy
from cyz_work1.items import CyzWork1Item
from scrapy import Request

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')
        for li in li_list:
            item = CyzWork1Item()
            item['name'] = li.xpath('./div[@class="name"]/a/@title').extract()
            item['link'] = li.xpath('./div[@class="name"]/a/@href').extract()
            item['publisher'] = li.xpath('./div[@class="publisher_info"][2]/a/text()').extract()
            # try:
            #     #正常爬取
            #     item['author'] = li.xpath('./div[@class="publisher_info"][1]/a[1]/@title').extract()
            # except IndexError:
            #     #对应图1.7情况，否则这条会爬不到
            #     item['author'] = '无'
            item['author'] = li.xpath('./div[@class="publisher_info"][1]/a[1]/@title').extract()
            item['price'] = li.xpath('./div[@class="price"]/p[1]/span[1]/text()').extract()
            yield item

        for i in range(2,26):
            url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-" + str(i)
            yield Request(url,callback=self.parse)
