#!/usr/bin/python  
# -*- coding:utf-8 -*-  
  
# from scrapy.contrib.spiders import  CrawlSpider,Rule  
  
from scrapy.spider import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from liepin.items import LiepinItem 
  
class liepinspiders(Spider):  
    """爬虫liepinSpider"""  
    name = "liepin1"  
    #减慢爬取速度 为1s  
    download_delay = 1  
    allowed_domains = ["bj.liepin.com"]  
    start_urls = [  
        #第一篇文章地址  
        "http://bj.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&key=python"  
    ]   
    def parse(self, response):  
        sel = Selector(response)  
        #获得猎聘网url和名称，薪资  ,发布时间
        jobs = sel.xpath('//div[@class="job-info"]')
        for job in jobs:     
            article_name = job.xpath('h3/a/span/text()').extract()
            article_url = job.xpath('h3/a/@href').extract()  
            article_xinzi = job.xpath('p[@class="condition clearfix"]/span').xpath('string(.)').extract()
            article_time = job.xpath('p[@class="time-info clearfix"]').xpath('string(.)').extract()
            item = LiepinItem() 
            item['article_name'] = article_name
            item['article_url'] = article_url 
            item['article_xinzi'] = article_xinzi
            item['article_time'] = article_time   
            yield item  
        #获取下一篇文章内容
        urls = sel.xpath('//div[@class="pagerbar"]/a/@href').extract()  
        for url in urls:  
            print url  
            url = "http://bj.liepin.com" + url  
            print url  
            yield Request(url, callback=self.parse)  
            
            
            
            