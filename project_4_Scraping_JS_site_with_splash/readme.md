# Project 4 - Scraping JS site with Splash.
This script parses quotes from a JavaScript-based website https://quotes.toscrape.com/js/ \
It renders the website with Splash running in Docker container connected to the port 8050.
Automatically follows the next page.

To start the scraper first the Splash is to be installed (as I use Linux I have it running in Docker container, see https://splash.readthedocs.io/en/stable/install.html).\
Then go to the appropriate folder and run in terminal
```
scrapy crawl quotes_js -o <output_file.extension>
```
where:
* <output_file.extension> - location and name of output file, extension can be .csv or .json.
   
# Проект 4 - Парсинг сайта на JS с использованием Splash.
Этот скрипт парсит цитаты с тренировочного сайта, основанного на JavaScript https://quotes.toscrape.com/js/ \
Скрипт рендерит сайт в Splash, который запущен в контейнере Docker и подключен на порт 8050.
Скрипт умеет переходить на следующую страницу с цитатами, когда текущая разобрана до конца.
Чтобы запустить скрейпер сначала необходимо установить и настроить Splash (поскольку я использую Linux, то мне проще всего эт было сделать в Docker, см. https://splash.readthedocs.io/en/stable/install.html).\
Затем необходимо перейти в папку скрипта и в консоли запустить команду
```
scrapy crawl quotes_js -o <output_file.extension>
```
где:
* <output_file.extension> - полный путь и имя файла выходных данных, расширение может быть .csv или .json.