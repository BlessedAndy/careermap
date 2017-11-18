# -*- coding: utf-8 -*-
import scrapy
from .. import items

class LinkedinSpider(scrapy.Spider):
    #爬虫名，启动爬虫时需要的参数
    name = "linkedin"
    #爬取域范围，可选
    allowed_domains = ["www.linkedin.com"]
    #start_urls = ['https://www.linkedin.com/']
    #https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH
    start_urls = ['https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&q=jserpAll']
    
    #https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&q=jserpAll
    #connections:
    #https://www.linkedin.com/mynetwork/invite-connect/connections/
#https://www.linkedin.com/search/results/index/

    def parse(self, response):
         
        #print(response.body)
        print('卧槽，到底进来没。。。')
        #
        #items = []
        
        #//*[@id="ember2927"]/span[1]/span
        
        #ember2927 > span.name-and-icon > span
        
        #<span class="name actor-name">李文杰</span>
        
        #name actor-name
        #//title[@lang='en']
        
        #URL
        #https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL&q=jserpAll
        #姓名
        #//div[@class='search-result__info pt3 pb4 ph0']/a/h3/span/span[@class='name actor-name']
        #职位
        #//div[@class='search-result__info pt3 pb4 ph0']/p[@class='subline-level-1 Sans-15px-black-85% search-result__truncate']
        #城市
        #//div[@class='search-result__info pt3 pb4 ph0']/p[@class='subline-level-2 Sans-13px-black-55% search-result__truncate']
        #Profile URL without https://www.linkedin.com
        #//div[@class='search-result__info pt3 pb4 ph0']/a/@href
        
        node_list = response.xpath("//div[@class='search-result__info pt3 pb4 ph0']")
        for node in node_list:
            #.extract()将xpath对象转换成Unicode字符串
            name = node.xpath("./a/h3/span/span[@class='name actor-name']/text()").extract()
            
            print('看这里！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
            print(name)
            print('看这里！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
            
            #xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            
            #item.append(item)
            
            #将获取的数据交给pipeline
            yield item
            
        #return items
        #with open("linkedin.html","w") as f:
   #         f.write(response.body)
        #pass
