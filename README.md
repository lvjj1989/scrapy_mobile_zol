# scrapy_mobile_zol

1.基于scrapy爬虫，获取中关村最新热门手机数据
2.无价格数据时默认价格字段为0，下次爬取时出现对应价格数据，会更新数据
3.支持增量爬取，更加爬取链接去重
4.数据爬取落地MySQL

建表sql：
    ```

        SET FOREIGN_KEY_CHECKS = 0;

        DROP TABLE IF EXISTS  `spider_moble_zol`;

        CREATE TABLE `spider_moble_zol` (
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `phone_name` varchar(32) DEFAULT '' COMMENT '手机名称',
          `phone_price` float DEFAULT NULL COMMENT '参考价格',
          `phone_info_url` varchar(512) DEFAULT NULL COMMENT '手机爬取链接',
          `phone_parameter_url` varchar(512) DEFAULT '' COMMENT '参数详情链接',
          `phone_x` int(11) DEFAULT '0' COMMENT '分辨率宽',
          `phone_y` int(11) DEFAULT '0' COMMENT '分辨率高',
          `phone_system` varchar(32) DEFAULT '' COMMENT '系统\n',
          `phone_size` varchar(32) DEFAULT '' COMMENT '主屏尺寸',
          `phone_info` varchar(512) DEFAULT '' COMMENT '手机基本信息',
          `phone_brand` varchar(32) DEFAULT '' COMMENT '手机品牌',
          `create_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB AUTO_INCREMENT=901 DEFAULT CHARSET=utf8;

        SET FOREIGN_KEY_CHECKS = 1;

    ```
执行命令：`scrapy runspider scrapy_mobile_zol/spiders/mobile_zol_spider.py`