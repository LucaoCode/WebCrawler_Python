import requests
import scrapy
from datetime import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


class CrawlvagasSpider(scrapy.Spider):
    name = "CrawlVagas"
    allowed_domains = ["www.trabalhaes.com.br"]
    start_urls = ["https://www.trabalhaes.com.br/vagas-em-vitoria-es/"]

    def parse(self, response):  
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        CaminhoRelatorio = f"../../../Relatorio/vagas-{now}.csv"
        # Cria um arquivo chamado vagas.txt
        with open(CaminhoRelatorio, "w", encoding="utf-8") as file:
            file.write("Vaga;Data;Link\n")
            for vaga in response.css('.list-item'):
                vaga_info = {
                    'link': vaga.css('.list-item-title a::attr(href)').get(),
                    'vaga': vaga.css('.list-item-title a::text').get(),
                    'data': vaga.css('.list-item-time::text').get()
                }
                # como será escrito o arquivo
                file.write(f"{vaga_info['vaga']};{vaga_info['data']};{vaga_info['link']}\n")
# inicializa o Scrap com o comando: scrapy crawl CrawlVagas

        # Após gerar o arquivo, enviá-lo por e-mail
        self.enviar_email(CaminhoRelatorio)

    def enviar_email(self, arquivo_anexo):
        # Informações do e-mail
        remetente = "x@gmail.com"
        destinatario = "x@ucl.br"
        senha = "x"

        # Configuração da mensagem e corpo do email
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = "Relatório de Vagas"
        body = "Segue em anexo o relatório de vagas extraído do site TrabalhaES ."
        msg.attach(MIMEText(body, 'plain'))

        # Anexar o arquivo
        attachment = open(arquivo_anexo, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(arquivo_anexo)}")
        msg.attach(part)

        # Conectar ao servidor SMTP e enviar o e-mail
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(remetente, senha)
            texto = msg.as_string()
            server.sendmail(remetente, destinatario, texto)
            server.quit()
            print(f"Relatório enviado com sucesso para {destinatario}")
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {str(e)}")