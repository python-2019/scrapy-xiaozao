#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy

import scrapy

# 这里是正确的 应该以spider上级目录为根目录
from xiaozao.items import XiaozaoItem

class xiaozaoScrapy(scrapy.Spider):
    """
        小灶实习 爬虫
    """
    name = 'shixixiaozao'
    allowed_domains = ["xiaozao.org"]
    host = "https://shixi.xiaozao.org"
    start_urls = (
        host,
    )

    def parse(self, response):
        # 职位div list
        div_list = response.xpath("//div[@class='ant-card-body']")
        # 遍历拉取信息
        for div in div_list:
            item = XiaozaoItem()
            item['post'] = div.xpath("./div/a/dl/dt/text()").extract_first()
            item['conpany'] = div.xpath("./div/a/dl/dd[1]/text()").extract_first()
            # 这里存在换行符需过滤
            item['city'] = div.xpath("./div/a/dl/dd[2]/text()").extract_first()
            # 这里存在换行符需过滤
            item['date'] = div.xpath("./div/a/dl/dd[3]/text()").extract_first()
            item['comment'] = div.xpath("./div[@class='comment']/a/span/text()").extract_first()
            item['logo'] = div.xpath("./a/img/@src").extract_first()
            # 详情地址
            item['href'] = self.host + div.xpath("./a/@href").extract_first()
            # 不爬取详情的话 yield item
            # yield item
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)})
        #  翻页
        next_page = response.xpath("//li[@class=' ant-pagination-next']/a/@href").extract_first()
        if next_page is not None:
            next_page_url = self.host + next_page
            print(next_page_url)
            yield scrapy.Request(
                next_page_url,
                callback=self.parse
            )

    def parse_detail(self, response):
        """
        处理详情页
       """
        item = response.meta['item']
        div_list_base_post_info= response.xpath("//div[@style='margin-right:25px;']")
        base_list = []
        for base_post_info in div_list_base_post_info:
            base_item = base_post_info.xpath("./span/text()").extract_first()
            base_list.append(base_item)
        item['base_post_info'] = base_list
        item['post_info'] = response.xpath("//div[@class='ant-card content ant-card-bordered']/div/div/div/text()").extract_first()
        item['addr'] = response.xpath("//div[@style='color:#666666;flex:1;white-space:pre-line;word-wrap:break-word;']/text()").extract_first()
        yield item
