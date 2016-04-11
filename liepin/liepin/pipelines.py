# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class LiepinPipeline(object):
    def __init__(self):  
        self.wb = Workbook()
        self.ws = self.wb.active
        # 设置表头
        self.ws.append(['职位名称', '网址', '薪资','发布时间'])
    def process_item(self, item, spider):
        c1 = ''.join(item['article_name']).strip()
        c2 = ''.join(item['article_url'])
        c3 = ''.join(item['article_xinzi']).strip()
        c4 = ''.join(item['article_time']).strip()
        
        line = [ c1, c2, c3, c4 ] 
        self.ws.append(line)
        self.wb.save('liepin.xlsx') #保存格式xlsx表格
        return item
