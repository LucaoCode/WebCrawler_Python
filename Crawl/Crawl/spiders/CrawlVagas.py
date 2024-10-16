import requests
import scrapy
from datetime import datetime


class CrawlvagasSpider(scrapy.Spider):
    name = "CrawlVagas"
    allowed_domains = ["www.trabalhaes.com.br"]
    start_urls = ["https://www.trabalhaes.com.br/vagas-em-vitoria-es/"]

    def parse(self, response):
        # Cria um arquivo chamado vagas.txt
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        CaminhoRelatorio = f"../../../Relatorio/vagas-{now}.csv"
        
        with open(CaminhoRelatorio, "w", encoding="utf-8") as file:
            file.write("Vaga;Data;Link\n")
            for vaga in response.css('.list-item'):
                vaga_info = {
                    'link': vaga.css('.list-item-title a::attr(href)').get(),
                    'vaga': vaga.css('.list-item-title a::text').get(),
                    'data': vaga.css('.list-item-time::text').get()
                }
                # como será escrito o arquivo
                file.write(f"{vaga_info['vaga']};{vaga_info['data']};{vaga_info['link']}\n")# como será escrito o arquivo
# inicializa o Scrap com o comando: scrapy crawl CrawlVagas

