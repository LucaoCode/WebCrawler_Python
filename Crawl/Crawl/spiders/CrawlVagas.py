import requests
import scrapy


class CrawlvagasSpider(scrapy.Spider):
    name = "CrawlVagas"
    allowed_domains = ["www.trabalhaes.com.br"]
    start_urls = ["https://www.trabalhaes.com.br/vagas-em-vitoria-es/"]

    def parse(self, response):
        for a in response.css('ol.cl-static-search-results a::attr(href)').getall():
            yield {'link': a}
