# -*- coding: UTF-8 -*-
import scrapy
from book9.items import Book9Item
from scrapy.http import Request
import os

class Book9Spider(scrapy.Spider):
    name = "book9"
    allowed_domains = ['quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/list/1_1.html']

    #爬取每本书的URL
    def parse(self, response):
        book_urls = response.xpath('//*[@id="navList"]/section/ul/li/span/a[1]/@href').extract()
        for book_url in book_urls:
            yield Request(book_url,callback=self.parse_read)

    #进入每一本书目录
    def parse_read(self,response):

        read_url = response.xpath('//*[@id="container"]/div[2]/section/div/div[1]/div[2]/a[1]/@href').extract()
        for i in read_url:
            # read_url_path = os.path.join('https:' + i + '#Catalog')
            yield Request(i,callback=self.parse_body)

    def parse_body(self,response):
        body_url= response.xpath('//*[@id="chapter"]/div[3]/div[3]/ul/div[2]/li/a/@href').extract()
        for i in body_url:
            # read_url_path = os.path.join('https:' + i + '#Catalog')
            yield Request(i,callback=self.parse_content)

    #爬取小说名，章节名，内容
    def parse_content(self,response):

        #爬取小说名
        book_name = response.xpath('//*[@id="direct"]/a[3]/text()').extract()
        #爬取章节名
        chapter_name = response.xpath('//*[@id="directs"]/div[1]/h1/strong/text()').extract_first()

        # # #爬取内容并处理
        chapter_content_2 = response.xpath('//*[@class="mainContenr"][1]').extract()
        chapter_content_1 = ''.join(chapter_content_2)
        chapter_content = chapter_content_1.replace('    ', '')
        item = Book9Item()
        item['book_name'] = book_name
        item['chapter_name'] = chapter_name
        item['chapter_content'] = chapter_content

        yield item