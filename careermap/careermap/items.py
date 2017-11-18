# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CareermapItem(scrapy.Item):
    # define the fields for your item here like:
    
    #URL
    #https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&q=jserpAll

    #姓名
    name = scrapy.Field()
    #职位
    current_position = scrapy.Field()
    #当前所在城市
    current_city = scrapy.Field()
    #Profile URL
    profile_URL = scrapy.Field()
    
    
    #pass
