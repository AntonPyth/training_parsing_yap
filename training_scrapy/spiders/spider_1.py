import scrapy


class QuotesSpider(scrapy.Spider):
    # Имя паука должно быть уникальным в рамках одного проекта.
    name = 'quotes'
    # Список стартовых ссылок, с которых паук начнёт парсить данные.
    # Нам понадобится только одна стартовая ссылка:
    start_urls = ['http://quotes.toscrape.com/',]

    def parse(self, response):
        for qoute in response.css('div.quote'):
            yield {
                'text': qoute.css('span.text::text').get(),
                'author': qoute.css('small.author::text').get(),
                'tags': qoute.css('a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
