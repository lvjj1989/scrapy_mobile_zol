# @Time : 2020/3/15 8:34 PM 
# @Author : lvjunjie


import scrapy
from scrapy.exporters import CsvItemExporter
from scrapy_mobile_zol.items import ScrapyMobileZolItem
import copy
import re


class MobileZil(scrapy.Spider):
    name = 'mobile_scrapy'
    # start_urls = ['http://detail.zol.com.cn/cell_phone_index/subcate57_list_2.html',
    # 'http://detail.zol.com.cn/cell_phone_index/subcate57_list_2.html']
    start_urls = []
    for i in range(1, 21):
        start_url = 'http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_{}.html'.format(i)
        start_urls.append(start_url)

    def parse(self, response):
        phone_list = response.xpath('//*[@id="J_PicMode"]/li')
        for phone_item in phone_list:
            stats = {}
            try:
                phone_price = phone_item.xpath('div[1]/span[2]/b[2]/text()').extract()[0]  # 价格
            except:
                phone_price = 0
            stats['phone_price'] = phone_price  # 价格

            try:
                phone_name = phone_item.xpath('h3/a/text()').extract()[0]
                stats['phone_name'] = phone_name.lower()  # 手机名称
            except:
                continue

            try:
                phone_info_url = response.urljoin(phone_item.xpath('a/@href').extract()[0])
                stats['phone_info_url'] = phone_info_url
                # print(response.urljoin(phone_item.xpath('a/@href').extract()[0]))  # 详情链接
            except:
                continue

            # print(stats)

            yield scrapy.Request(url=phone_info_url, meta={"stats": stats}, callback=self.parse_phone_info, dont_filter=True)

    def parse_phone_info(self, response):
        stats = response.meta['stats']
        # 获取手机参数详情链接
        phone_parameter = response.xpath('//*[@id="_j_tag_nav"]/ul/li[2]')
        phone_parameter_url = response.urljoin(phone_parameter.xpath("a/@href").extract()[0])
        # print(phone_parameter_url)
        stats['phone_parameter_url'] = phone_parameter_url

        # 获取手机品牌
        try:
            phone_brand = response.xpath('//*[@id="_j_breadcrumb"]/text()').extract()[0]
        except:
            phone_brand = ''

        stats['phone_brand'] = phone_brand

        # 获取手机所有基本信息
        phone_info_xpaths = response.xpath('//*[@class="product-link"]')
        phone_info = ''
        for phone_info_item in phone_info_xpaths:
            # print(phone_info_item.xpath("text()").extract()[0])
            if phone_info_item.xpath("text()").extract()[0]:
                phone_info = phone_info_item.xpath("text()").extract()[0] + ", " + phone_info

        stats['phone_info'] = phone_info

        # 获取手机尺寸
        phone_size = phone_info_xpaths[-2].xpath("text()").extract()[0]
        # print(phone_size)
        try:
            phone_size = float(re.search('(.+)英寸',phone_size).group(1))
        except:
            phone_size = 0.0
        stats['phone_size'] = phone_size


        # 获取手机分辨率
        phone_resolution = phone_info_xpaths[-1].xpath("text()").extract()[0]
        # print(phone_resolution)
        stats['phone_x'] = int(re.search("(\d+)x(\d+).+", phone_resolution).group(2))
        stats['phone_y'] = int(re.search("(\d+)x(\d+).+", phone_resolution).group(1))
        print(stats)
        yield stats





    # def parse_phone_parameter(self, response):
    #     stats = response.meta['stats']
    #     phone_resolution = response.xpath('//*[@class="box-item-fl"]/text()').extract()[0]
    #     print(phone_resolution)
    #
    #     # phone_x =
    #     # phone_y =
    #     # phone_system =
    #     # phone_size =
    #     #
    #
    #
