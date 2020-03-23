# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ScrapyMobileZolPipeline(object):
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='lvjj',
            password='a1478520B',
            db='mysql_lvjj',
            charset='utf8'
        )
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
        insert into spider_moble_zol(
        phone_name,
        phone_price,
        phone_info_url,
        phone_parameter_url,
        phone_x,
        phone_y,
        phone_size,
        phone_info,
        phone_brand) 
        VALUES("{}","{}","{}","{}",{},{},{},"{}","{}")

        """.format(item['phone_name'],
                   item['phone_price'],
                   item['phone_info_url'],
                   item['phone_parameter_url'],
                   item['phone_x'],
                   item['phone_y'],
                   item['phone_size'],
                   item['phone_info'],
                   item['phone_brand'])
        # 执行插入数据到数据库操作
        # print(insert_sql)
        self.cursor.execute(insert_sql)
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()


        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()