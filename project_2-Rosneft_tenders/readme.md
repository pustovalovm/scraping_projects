# Project 2 - Rosneft tenders.
This script parses tender information from Rosneft registry located at http://zakupki.rosneft.ru/zakupki/\
It parses main info from the tender table such as ID, title, link to tender's page, published date and submission deadline. Also it visits tender's page and parses initial minimum price for it. There is some more data is available there which can be parsed (documents' contacts, etc.). When all the tenders are parsed from the table on the page the scraper continues to the next one.


To start the scraper go to the appropriate folder and run in terminal
```
scrapy crawl RN_tenders -o <output_file.extension>
```
where:
* <output_file.extension> - location and name of output file, extension can be .csv or .json.

The way forward is:
* Filtering tenders by legal entities and keywords.
* Extracting more data like contacts and docs.
* Running the script on some remote virtual machine on schedule (i.e. with cron) and sending the updates daily to e-mail or Telegram.
   
# Проект 2 - Парсинг тендеров Роснефти.
Этот скрипт парсит данные об активных закупках Роснефти с сайта закупок http://zakupki.rosneft.ru/zakupki/\
Скрипт забирает основные данные из общей таблицы закупок, такие как ID, название, ссылка на страницу закупки, дата публикации и дата подачи. Также для каждой закупки с её страницы забирается начальная максимальная цена. На этой странице есть дополнительная информация, такая как список лотов, контакты, документация и т.д.
Скрипт умеет переходить на следующую страницу, когда текущая разобрана до конца.
Чтобы запустить скрейпер необходимо перейти в соответствующую папку и запустить в консоли
```
scrapy crawl RN_tenders -o <output_file.extension>
```
где:
* <output_file.extension> - полный путь и имя файла выходных данных, расширение может быть .csv или .json.

Дальнейшее развитие:
* Фильтрация закупок по юрлицам и ключевым словам.
* Извлечение большего количества данных со страницы тендера.
* Запуск на удалённой виртуальной машине скрипта по расписанию (например при помощи cron) и ежедневная отправка обновлений на почту или в Telegram.