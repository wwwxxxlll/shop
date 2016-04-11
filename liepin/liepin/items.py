# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class LiepinItem(Item):
    """存储提取信息数据结构"""  
    article_name = Field()  #提取名称
    article_url = Field()   #提取地址
    article_xinzi = Field() #提取薪资
    article_time = Field()  #提取时间