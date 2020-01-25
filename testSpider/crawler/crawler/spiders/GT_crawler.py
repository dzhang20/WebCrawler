# -*- coding: utf-8 -*-
import scrapy


class GtCrawlerSpider(scrapy.Spider):
    name = 'GT_crawler'
    allowed_domains = ['gatech.edu']
    start_urls = ['https://gatech.edu/']

    def parse(self, response):
        pass
