# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import json
import pymysql
import re
from scrapy.exceptions import DropItem

isbn_list = []

class CyzWork1Pipeline:
    def __init__(self):
        # self.ids_seen = set()

        self.connect = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='chen0000',db='scraping',charset='utf8')
        self.cursor = self.connect.cursor()
        self.cursor.execute("USE scraping")
        sql = """CREATE TABLE Bestseller(id BIGINT(7) NOT NULL AUTO_INCREMENT,cname VARCHAR(200),clink VARCHAR(200),cpublisher VARCHAR(200),cauthor VARCHAR(200),cprice VARCHAR(200),PRIMARY KEY(id))"""
        #数据表未存在
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        #数据表已存在
        except pymysql.err.OperationalError:
            pass

    def process_item(self, item, spider):

        isbn = re.sub("\D","",item["isbn"][0])
        if isbn in isbn_list:
            pass
        else:
            isbn_list.append(isbn)

            name = item["name"][0].replace(" ","")
            link = item["link"][0]
            publisher = item["publisher"][0]
            if len(item["author"]) == 1:
                author = item["author"][0]
            else:
                tp = ""
                for i in item["author"]:
                    tp = tp + i + " "
                author = tp
            price = item["price"][0].replace('¥','')
            self.cursor.execute("INSERT INTO Bestseller(cname,clink,cpublisher,cauthor,cprice) VALUES (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(name,link,publisher,author,price))
            self.connect.commit()
        print(len(isbn_list))
        print(isbn_list)
        print("\n")
        return item
