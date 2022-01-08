import scrapy
from cyz_work1.items import CyzWork1Item
from scrapy import Request
import requests
import json


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['book.jd.com']
    start_urls = ['https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-1#comfort']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            item = CyzWork1Item()
            item["name"] = li.xpath('./div[@class="p-detail"]/a/text()').extract()
            item["author"] = li.xpath('./div[@class="p-detail"]/dl[1]/dd/a/text()').extract()
            item["publisher"] = li.xpath('./div[@class="p-detail"]/dl[2]/dd/a/text()').extract()
            item["link"] = li.xpath('./div[@class="p-detail"]/a/@href').extract()
            #ajax爬取价格
            SkuId = item["link"][0].replace("//item.jd.com/","").replace(".html","")
            json_price = requests.get("https://p.3.cn/prices/mgets?skuIds=J_"+SkuId).text
            data = json.loads(json_price.replace('[', '').replace(']', ''))
            price = data["op"]
            item["price"] = []
            item["price"].append(price)
            yield item

        for i in range(2,6):
            url = "https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-{}#comfort".format(str(i))
            yield Request(url,callback=self.parse)
