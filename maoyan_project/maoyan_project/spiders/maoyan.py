import scrapy
import time
import random


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=0']
    url='https://maoyan.com/board/4?offset='
    page=10
    def parse(self, response):
        # . class 名字为board-wrapper 中的 dd 标签
        movies = response.css('.board-wrapper dd')
        # 虽然加了 cookie  如果弹出了滑块验证码 就睡眠一下，再请求
        if (len(movies) == 0):
            print(response.url)
            time.sleep(random.randint(30, 60))
            request = scrapy.Request(url=response.url, callback=self.parse)
        else:
            for movie in movies:
                item = {}
                #  . class 名字 ::文本
                item["movie_name"] = movie.css('.name a::text').extract_first()
                item["movie_star"] = movie.css('.star::text').extract_first().strip()
                item['movie_time'] = movie.css('.releasetime::text').extract_first().strip()
                big_score = movie.css('.integer::text').extract_first().strip()
                small_score = movie.css('.fraction::text').extract_first().strip()
                item['movie_sore'] = big_score + small_score
                yield item
        time.sleep(random.randint(0, 10))
        self.page+=10
        if (self.page<=90):
            yield scrapy.Request(url=self.url +str(self.page), callback=self.parse)