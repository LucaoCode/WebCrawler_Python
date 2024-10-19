@echo off
call "C:\Users\LUCAS LIMA\Desktop\env\Scripts\activate.bat"
cd "C:\Users\LUCAS LIMA\Workspace\WebCrawler_Python\Crawl\Crawl\spiders"
python -m scrapy crawl CrawlVagas
pause


