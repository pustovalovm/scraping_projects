# Project 3 - Books crawl spider.
This script parses books information from a scraping training website http://books.toscrape.com \
It extracts all the links to the book pages, visits the pages and scrapes basic book info such as name, image of bookcover url, price and rating.
Automatically follows the next page.

To start the scraper go to the appropriate folder and run in terminal
```
scrapy crawl book_spider -o <output_file.extension>
```
where:
* <output_file.extension> - location and name of output file, extension can be .csv or .json.

The way forward is:
* Make Rosneft scraper work like this. Much simpler and clearer way.
   
# Проект 3 - Парсинг сайта с книгами с использованием краулера.
Этот скрипт парсит данные книгах с тренировочного сайта http://books.toscrape.com\
Скрипт извлекает ссылки на страницы книг с главной страницы, переходит по ним и извлекает основную информацию, такую как название, ссылка на изображение обложки книги, цену и рейтинг.
Скрипт умеет переходить на следующую страницу со ссылками, когда текущая разобрана до конца.
Чтобы запустить скрейпер необходимо перейти в соответствующую папку и запустить в консоли
```
scrapy crawl book_spider -o <output_file.extension>
```
где:
* <output_file.extension> - полный путь и имя файла выходных данных, расширение может быть .csv или .json.

Дальнейшее развитие:
* Переписать скрейпер Роснефти по принципу краулера, так проще и логичнее.