# -*- coding: UTF-8 -*-
import os
import io
class Book9Pipeline(object):
    def process_item(self, item, spider):
        # item['book_name']
        file_path = os.path.join("D:\\BOOK",item['book_name'][0])
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        # #将各章节写入文件
        chapter_path = os.path.join(file_path,item['chapter_name'] + '.txt')
        print(chapter_path)
        with io.open(chapter_path,'w',encoding='utf-8') as f:
            f.write(item['chapter_content'])

        return item


