import scrapy
from cyz_work1.items import CyzWork1Item
from scrapy import Request
from bs4 import BeautifulSoup

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1']

    def parse(self, response):
        self.header = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection":"keep-alive",
            "Cookie":"__permanent_id=20200411184106952270082839774622750; MDD_channelId=70000; MDD_fromPlatform=307; dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; permanent_key=202101051107356806153715145a6d65; ddscreen=2; secret_key=aaaa6bd0ad3414148641266412217a80; __visit_id=20210107195951800332727119817802828; __out_refer=; USERNUM=JaXZmCUlyYMYb57/V1jrYQ==; dangdang.com=email=MTczNjUxODAzNDA2NzA1NkBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=4993640252214&customerid=689dzg65D1Xux9nvgBxDdA==&viptype=653t1sRgb1w=&show_name=173%2A%2A%2A%2A0340; ddoy=email=1736518034067056%40ddmobilphone__user.com&nickname=&agree_date=1&validatedflag=0&uname=17365180340&utype=1&.ALFG=on&.ALTM=1610021763; sessionID=pc_d07472c09dc078a8cc9597c88a49203b3335fff87e6cd5d97814e34a185e539f; __dd_token_id=20210107202231652398754307cc4473; login.dangdang.com=.AYH=2021010720223201321669564&.ASPXAUTH=j79V1LEjG/lXjfEtD2lYLIVlzhC3DtLUejLA7s5uhiUq6TZaVgZAsg==; login_dang_code=20210107202243163539314367e7d9d8; __rpm=mix_317715.3208542%2C9371..1610023921634%7C...1610023926384; LOGIN_TIME=1610023927305; __trace_id=20210107205220610208084173279278388",
            "Host":"product.dangdang.com",
            "Referer":"http://product.dangdang.com/",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
            "X-Requested-With":"XMLHttpRequest"
        }

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
            yield scrapy.Request(item["link"][0],callback=self.parse_isbn,dont_filter=True,headers=self.header,
                                 meta={'item':item})

        for i in range(2,26):
            url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-" + str(i)
            yield Request(url,callback=self.parse)

    def parse_isbn(self,response):
        item = response.meta['item']
        # print(response)
        # print(response.text)
        item["isbn"] = response.xpath('//ul[@class="key clearfix"]/li[5]/text()').extract()
        # item["isbn"] = response.xpath('/html/body/div[2]/div[5]/div[1]/div[4]/div[3]/div[1]/ul/li[5]/text()').extract()
        # print(item)
        # print(item["isbn"])
        yield item