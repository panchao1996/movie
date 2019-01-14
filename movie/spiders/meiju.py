# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'     # 爬虫名。一个项目下可能有多个爬虫，并且每个爬虫有优先级、并发等设置：scrapy crawl [spider_name]
    allowed_domains = ['meijutt.com']    #  为了防止爬虫自动爬取到其他网站，设置限制，每一次请求前都会检查请求得网址是否属于这个域名下，是的话才允许请求。注意：爬取日志爬取网址后响应总为None，检查allowed_domain书写是否正确。值是一级域名
    start_urls = ['http://meijutt.com/new100.html']  # 第一个请求得url，整个程序逻辑得入口。得到得response返回给 self.parse（self，response=response）

    def parse(self, response):

        # print(response.status_conde,response.content,response.text)
        # 非框架下写法   dom = lxml.etree.HTML(response.text);dom.xpath('')
        #scrapy框架下正则写法  Selector(response.text).xpath('').extract()

        movie_list = response.xpath('//ul[@class="top-list  fn-clear" ]/li')  #[<Selector data=li>对象，<li>对象]
        # /h5/text()
        for movie in movie_list:
            # movie.xpath('./h5/text()').extract()[0]    # .表示在字标签基础上继续解析
            # movie.xpath('./h5/text()').extract_first()   # xpath()返回[Selector(),Selector()]   ，功能强，可以在Selector对象上进行第二次xpath解析
            # xpath().extract()返回['据集名1'，'据集名2']
            #xpath（）.extract_first()   返回'据集名1'
            name = movie.xpath('./h5/a/text()').extract_first()    #
            # print(movie,name)  # 建议debug而不是print，不然因为并发会重复打印多次信息。

            item = MovieItem()
            # item.name= name
            item['name']= name
            yield item   # 相当于同步脚本方法中得return


