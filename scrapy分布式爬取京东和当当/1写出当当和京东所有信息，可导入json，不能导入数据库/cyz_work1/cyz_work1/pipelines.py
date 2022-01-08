# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import json

class CyzWork1Pipeline:
    def __init__(self):
        self.file = codecs.open("../cyz_work1/data.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        name = item["name"][0]
        link = item["link"][0]
        publisher = item["publisher"][0]
        # print(item["author"])
        if len(item["author"]) == 1:
            author = item["author"][0]
        else:
            tp = ""
            for i in item["author"]:
                tp = tp + i + " "
            author = tp
        # print(author)
        price = item["price"][0]
        oneitemm = {"name": name, "link": link, "publisher": publisher, "author": author, "price": price}
        ii = json.dumps(oneitemm, ensure_ascii=False)
        linee = ii + '\n'
        self.file.write(linee)

        return item
