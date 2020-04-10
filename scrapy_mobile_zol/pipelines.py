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
            password='123456',
            db='mysql_lvjj',
            charset='utf8'
        )

        # 创建游标
        self.cursor = self.conn.cursor()

    # def data_insert(self, phone_name, phone_price, phone_info_url, phone_parameter_url, phone_x, phone_y, phone_size, phone_info, phone_brand):
    def data_insert(self, **kwargs):
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
                """.format(kwargs['phone_name'],
                           kwargs['phone_price'],
                           kwargs['phone_info_url'],
                           kwargs['phone_parameter_url'],
                           kwargs['phone_x'],
                           kwargs['phone_y'],
                           kwargs['phone_size'],
                           kwargs['phone_info'],
                           kwargs['phone_brand'])
        # 执行插入数据到数据库操作
        # print(insert_sql)
        self.cursor.execute(insert_sql)
        # 提交，不进行提交无法保存到数据库
        self.conn.commit()

    def data_select(self, phone_info_url):
        select_sql = "SELECT * FROM spider_moble_zol WHERE phone_info_url = '{}' and phone_price > 0".format(phone_info_url)
        self.cursor.execute(select_sql)
        res = self.cursor.fetchone()
        # print("res = ", res)
        return res

    def data_update_price(self, phone_info_url, phone_price):
        select_sql = "SELECT * FROM spider_moble_zol WHERE phone_info_url = '{}' and phone_price = 0".format(
            phone_info_url)
        self.cursor.execute(select_sql)
        res = self.cursor.fetchone()
        # print("res = ", res)
        if res:
            uplate_sql = "UPDATE spider_moble_zol SET phone_price={} WHERE phone_info_url = '{}' and phone_price = 0".format(phone_price, phone_info_url)

            # print(uplate_sql)
            self.cursor.execute(uplate_sql)
            self.conn.commit()
            return True
        else:
            return False

    def process_item(self, item, spider):

        # print(dict(item))
        res_data_select = self.data_select(item['phone_info_url'])
        if self.data_update_price(phone_info_url=item['phone_info_url'], phone_price=item['phone_price']):
            print('更新价格')
        else:
            if not res_data_select:
                print("增量数据")
                # print(res_data_select)
                # 增量数据
                # self.data_insert(phone_name=item['phone_name'], phone_price=item['phone_price'],
                #                  phone_info_url=item['phone_info_url'], phone_parameter_url=item['phone_parameter_url'],
                #                  phone_x=item['phone_x'], phone_y=item['phone_y'], phone_size=item['phone_size'],
                #                  phone_info=item['phone_info'], phone_brand=item['phone_brand'])
                self.data_insert(dict(item))
        # self.cursor.execute(insert_sql)
        # # 提交，不进行提交无法保存到数据库
        # self.conn.commit()

        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()