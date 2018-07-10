# -*- coding: UTF-8 -*-
import scrapy

class Book9Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()   #小说名字
    chapter_name = scrapy.Field()   #小说章节名字
    chapter_content = scrapy.Field()    #小说章节内容