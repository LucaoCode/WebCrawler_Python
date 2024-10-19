# 🕸Projeto Web Crawler - Vagas de Emprego no ES

Este projeto realiza o web scraping do site TrabalhaES para extrair vagas de emprego disponíveis na cidade de Vitória, ES. O resultado é salvo em um arquivo CSV e enviado por e-mail automaticamente.

## 🏗 Funcionalidades

- Extração de vagas de emprego do site *www.trabalhaes.com.br*
- Armazenamento de dados em arquivo CSV
- Envio automático do arquivo gerado por e-mail
- Executa rotinas periódicas

## 🫡 Apresentação do Projeto

**Video em Breve**

## 🕷 Tecnologias utilizadas

- **Python 3**
- **Scrapy** - Biblioteca de scraping para realizar a extração de dados.
- **Requests** - Para fazer requisições HTTP
- **smtplib** - Para envio de e-mails via protocolo SMTP.
- **email.mime** - Para estruturação e envio do e-mail com anexo.
- **Agendador de Tarefas do Windows** - Para agendamento de execuções automáticas do script.

## 🤖 Requisitos

1. Python 3.9 ou superior instalado.
2. Instalar as bibliotecas necessárias no terminal:
```python
pip install scrapy requests
```
3. Acesso a uma conta de e-mail com senha de app configurada para envio via SMTP (usado para enviar o relatório).

## 👾Como Executar

### 1. Rodar o scrapy

- Para iniciar o processo de scraping, execute o comando no terminal:
```python
scrapy crawl CrawlVagas
```
sso iniciará o crawler que extrairá as vagas e criará um arquivo CSV com o relatório na pasta *Relatorio*.

### 2. Envio do relatótio para o E-mail

- No código Python, ajuste os campos de *remetente*, *destinatario* e *senha* de acordo com suas credenciais de e-mail.

- Após a extração das vagas, o script automaticamente enviará o relatório gerado para o destinatário configurado no código.

- Certifique-se de usar uma senha de aplicativo do Gmail, configurada via painel de segurança.

### 3. Exemplo de arquivo CSV gerado

O arquivo gerado terá o seguinte formato:
```python
Vaga;Data;Link
Desenvolvedor Python;2024-10-10;https://www.trabalhaes.com.br/vaga/12345
Analista de Dados;2024-10-11;https://www.trabalhaes.com.br/vaga/12346
```
### 4. Automação com Crontab (Linux/Mac)

- Para rodar o script automaticamente em um intervalo de tempo, adicione uma tarefa no Crontab. Exemplo para rodar diariamente às 9h:
```bash
0 9 * * * cd /caminho/para/o/projeto && scrapy crawl CrawlVagas
```
### 5. Automação no Windows (Agendador de tarefas)

- Para rodar automaticamente no Windows, use o Agendador de Tarefas. Crie uma tarefa para executar o arquivo *rodar.bat* configurado para iniciar o Scrapy.

## 🤩 Responsáveis pelo projeto

[Lucas Lima Campos](https://www.linkedin.com/in/lucaslimacampos/)