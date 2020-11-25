# Project 1 - Fist steps.
The very basic scraping of 2 internet-stores.
1) 'cigabuy' folder contains scraper for 'https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html' and following pages.
2) 'glasses' folder contains scraper for 'https://www.glassesshop.com/bestsellers/' and following pages.


To start the scraper go to the appropriate folder 'glasses' or 'cigabuy' and run in terminal
```
scrapy crawl <spider_name> -o <output_file.extension>
```
where:
* <spider_name> is 'special_offers' for cigabuy and 'glass_spider' for glasses 
* <output_file.extension> - location and name of output file, extension can be .csv or .json.

# Проект 1 - Первые шаги.
Очень простое получение данных с 2 интернет-магазинов. 
1) Папка 'cigabuy' содержит скрепер для страницы 'https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html' и последующих.
2) Папка 'glasses' содержит скрепер для страницы 'https://www.glassesshop.com/bestsellers/' и последующих.
3) 
Чтобы запустить скрейпер необходимо перейти в соответствующую папку  'glasses' или 'cigabuy' и запустить в консоли
```
scrapy crawl <spider_name> -o <output_file.extension>
```
где:
* <spider_name> это название скрепера 'special_offers' для cigabuy и 'glass_spider' для glasses 
* <output_file.extension> - полный путь и имя файла выходных данных, расширение может быть .csv или .json.
