# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMobileZolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    phone_name = scrapy.Field()  # 手机名称
    phone_price = scrapy.Field()  # 参考价格
    phone_info_url = scrapy.Field()  # 手机爬取链接
    phone_parameter_url = scrapy.Field()  # 参数详情链接
    phone_x = scrapy.Field()  # 分辨率宽
    phone_y = scrapy.Field()  # 分辨率高
    # phone_system = scrapy.Field()  # 系统
    phone_size = scrapy.Field()  # 主屏尺寸
    phone_info = scrapy.Field()  # 手机基本信息
    phone_brand = scrapy.Field()  # 手机品牌
