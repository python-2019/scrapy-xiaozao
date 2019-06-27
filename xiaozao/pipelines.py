# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

import xlsxwriter
from scrapy.conf import settings


class XiaozaoPipeline(object):

    def open_spider(self, spider):
        file_path = settings.get("FILE_PATH") + "小灶实习.csv"
        self.file = open(file_path, 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        headers = ['职位', '企业', '城市', '工作地点', '发布时间', '小灶点评', 'logo', '基础职位信息', '详细职位信息', '详情链接']
        self.csv_writer.writerow(headers)

    def process_item(self, item, spider):
        post = item['post']
        company = item['company']
        city = item['city']
        addr = item['addr']
        date = item['date']
        comment = item['comment']
        logo = item['logo']
        base_post_info = item['base_post_info']
        post_info = item['post_info']
        href = item['href']
        row = [post, company, city, addr, date, comment, logo, base_post_info, post_info, href]
        self.csv_writer.writerow(row)
        print(row)
        return item

    def close_spider(self, spider):
        self.file.flush()


class XiaozaoExcelPipeline(object):

    col = "A"
    row_num = 1

    def open_spider(self, spider):
        file_path = settings.get("FILE_PATH") + '小灶实习.xlsx'
        workbook = xlsxwriter.Workbook(file_path)
        headers = ['职位', '企业', '城市', '工作地点', '发布时间', '小灶点评', 'logo', '基础职位信息', '详细职位信息', '详情链接']
        # 插入头部
        workbook.write_row("A1", headers)

    def process_item(self, item, spider):
        post = item['post']
        company = item['company']
        city = item['city']
        addr = item['addr']
        date = item['date']
        comment = item['comment']
        logo = item['logo']
        base_post_info = item['base_post_info']
        post_info = item['post_info']
        href = item['href']
        row = [post, company, city, addr, date, comment, logo, base_post_info, post_info, href]
        self.row_num = self.row_num+1
        col_row = self.col+str(self.row_num)
        self.workbook.write_row(col_row, row)
        print(row)
        return item

    def close_spider(self, spider):
        self.workbook.closed()
