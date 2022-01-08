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
        # 代码移植时注意改写
        self.file = codecs.open("../cyz_work1/data.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):
        # print("name:"+str(len(item["name"])))
        # print("link:"+str(len(item["link"])))
        # print("publisher:"+str(len(item["publisher"])))
        # print("author:"+str(len(item["author"])))
        # print("time:"+str(len(item["time"])))
        # print("recommend:"+str(len(item["recommend"])))
        # print("price:"+str(len(item["price"])))

        for j in range(len(item["name"])):
            name = item["name"][j]
            # print(name)
            link = item["link"][j]
            # print(link)
            publisher = item["publisher"][j]
            # print(publisher)
            author = item["author"][j]
            # print(author)
            time = item["time"][j]
            # print(time)
            recommend = item["recommend"][j]
            # print(recommend)
            price = item["price"][j]
            # print(price)

            oneitem = {"name":name,"link":link,"publisher":publisher,"author":author,"time":time,"recommend":recommend,"price":price}
            i = json.dumps(oneitem,ensure_ascii=False)
            line = i + '\n'
            # print(line)
            self.file.write(line)

        return item
