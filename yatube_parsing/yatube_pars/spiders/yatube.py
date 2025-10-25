import scrapy


class YatubeSpider(scrapy.Spider):
    name = "yatube"
    allowed_domains = ["158.160.177.221"]
    start_urls = ["http://158.160.177.221/"]

    def parse(self, response):
        for post in response.css('div.card.mb-3.mt-1.shadow-sm'):
            author = post.css('strong.d-block.text-gray-dark::text').get()
            text = ' '.join(post.css('p.card-text::text').getall()).strip()
            date = post.css('time::attr(datetime), .date::text').get()
            yield {
                'author': author,
                'text': text,
                'date': date,
            }
    
    # По CSS-селектору ищем ссылку на следующую страницу.
        next_page = response.css('a.page-link:contains("Следующая")::attr(href)').get()
        if next_page:
        # Если ссылка нашлась, загружаем страницу по ссылке
        # и вызываем метод parse() ещё раз.
            yield response.follow(next_page, callback=self.parse)
