# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CyzWork1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #名称
    name = scrapy.Field()
    #具体网址
    link = scrapy.Field()
    #出版社
    publisher =scrapy.Field()
    #作者
    author = scrapy.Field()
    #时间
    time = scrapy.Field()
    #推荐力度
    recommend = scrapy.Field()
    #价格
    price = scrapy.Field()