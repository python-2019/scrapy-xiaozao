# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaozaoItem(scrapy.Item):
    """
        小灶 校招实习 抓取实体
    """
    # 职位
    post = scrapy.Field()
    # 企业
    conpany = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 发布时间
    date = scrapy.Field()
    # 小灶点评
    comment = scrapy.Field()
    # logo
    logo = scrapy.Field()
    # 详情链接
    href = scrapy.Field()
    # 基础职位信息
    base_post_info = scrapy.Field()
    # 详细职位信息
    post_info = scrapy.Field()
    # 工作地址
    addr = scrapy.Field()

