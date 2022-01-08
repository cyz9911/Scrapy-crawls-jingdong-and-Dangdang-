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
        self.header = {
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control":"max-age=0",
            "sec-fetch-dest":"document",
            "sec-fetch-mode":"navigate",
            "sec-fetch-site":"none",
            "sec-fetch-user":"?1",
            "upgrade-insecure-requests":"1",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
        }

        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            item = CyzWork1Item()
            item["name"] = li.xpath('./div[@class="p-detail"]/a/text()').extract()
            item["author"] = li.xpath('./div[@class="p-detail"]/dl[1]/dd/a/text()').extract()
            item["publisher"] = li.xpath('./div[@class="p-detail"]/dl[2]/dd/a/text()').extract()
            item["link"] = li.xpath('./div[@class="p-detail"]/a/@href').extract()
            #ajax爬取价格
            SkuId = item["link"][0].replace("//item.jd.com/","").replace(".html","")
            json_price = requests.get("https://p.3.cn/prices/mgets?skuIds=J_"+SkuId,headers=self.header).text
            data = json.loads(json_price.replace('[', '').replace(']', ''))
            # print(item["link"][0])
            # print(SkuId)
            # print(data)
            # print("")

            price = data["op"]
            item["price"] = []
            item["price"].append(price)
            # yield scrapy.Request("https:"+item["link"][0],callback=self.parse_isbn,dont_filter=True,headers=self.header,
            #                      meta={'name':item["name"],'author':item["author"],'publisher':item["publisher"],'link':item["link"],'price':item["price"]})
            yield scrapy.Request("https:" + item["link"][0], callback=self.parse_isbn, dont_filter=True,
                                 headers=self.header,meta={'item':item})

        for i in range(2,6):
            url = "https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10003-{}#comfort".format(str(i))
            yield Request(url,callback=self.parse)

    def parse_isbn(self,response):
        item = response.meta['item']
        # print(item)
        # print(response.text)
        # print(response)
        # print("111")
        # item["isbn"] = response.xpath('//ul[@id="parameter2"]/li/text()').extract()
        item["isbn"] = response.xpath('//*[@id="parameter2"]/li[2]/text()').extract()
        # print(item["isbn"])
        yield item

        # yield scrapy.Request("https:"+item["link"][0],callback=self.parse_isbn,meta={'item':item},dont_filter=True)