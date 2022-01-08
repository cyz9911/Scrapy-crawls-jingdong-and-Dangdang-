import scrapy
from cyz_work1.items import JingDongBookItem
from scrapy import Request
#https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-1
#https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-2
#https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-5

class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['book.jd.com']
    start_urls = ['https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-1']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            item = JingDongBookItem()
            item["name"] = li.xpath('./div[@class="p-detail"]/a/text()').extract()
            item["author"] = li.xpath('./div[@class="p-detail"]/dl[1]/dd/a/text()').extract()

            # item["author"] = ""
            # xx = li.xpath('./div[@class="p-detail"]/dl[1]/dd/a/text()').extract()
            # for i in xx:
            #     item["author"] = item["author"] + i + " "

            item["publisher"] = li.xpath('./div[@class="p-detail"]/dl[2]/dd/a/text()').extract()
            item["price"] = li.xpath('./div[@class="p-detail"]/dl[4]/dd/em/text()').extract()
            item["link"] = li.xpath('./div[@class="p-detail"]/a/@href').extract()
            yield item

        for i in range(2,6):
            url = "https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-" + str(i)
            yield Request(url,callback=self.parse)
