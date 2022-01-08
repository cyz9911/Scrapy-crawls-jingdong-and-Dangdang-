# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import json
from cyz_work1.items import CyzWork1Item
from cyz_work1.items import JingDongBookItem

class CyzWork1Pipeline:
    def __init__(self):
        # 代码移植时注意改写
        self.file = codecs.open("../cyz_work1/data.json", "wb", encoding="utf-8")

    def process_item(self, item, spider):

        if isinstance(item,CyzWork1Item):
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
        elif isinstance(item,JingDongBookItem):

            # print(item["author"])

            # print("name:"+str(len(item["name"])))
            # print("link:"+str(len(item["link"])))
            # print("publisher:"+str(len(item["publisher"])))
            # print("author:"+str(len(item["author"])))
            # print("price:"+str(len(item["price"])))

            # print(item["name"])
            # print(item["link"])
            # print(item["publisher"])
            # print(item["author"])
            # # print(type(item["author"]))
            # print(item["price"])
            # print("")

            name = item["name"][0]
            # print(name+"\n")
            link = item["link"][0]
            publisher = item["publisher"][0]
            if len(item["author"]) == 1:
                author = item["author"][0]
            else:
                tp = ""
                for i in item["author"]:
                    tp = tp + i + " "
                author = tp

            price = item["price"][0]
            oneitemm = {"name": name, "link": link, "publisher": publisher, "author": author, "price": price}
            # print(oneitemm)

            ii = json.dumps(oneitemm, ensure_ascii=False)
            linee = ii + '\n'
            print(linee)
            self.file.write(linee)


            # for jj in range(len(item["name"])):
            #     name = item["name"][jj]
            #     # print(name)
            #     link = item["link"][jj]
            #     # print(link)
            #     publisher = item["publisher"][jj]
            #     # print(publisher)
            #     author = item["author"][jj]
            #     # print(str(len(author)))
            #     # print(author)
            #     price = item["price"][jj]
            #     # print(price)
            #
            #     oneitemm = {"name":name,"link":link,"publisher":publisher,"author":author,"price":price}
            #     ii = json.dumps(oneitemm,ensure_ascii=False)
            #     linee = ii + '\n'
            #     # print(line)
            #     self.file.write(linee)

        return item
