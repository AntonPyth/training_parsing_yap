import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        all_authors = response.css('a[href^="/author/"]')
        for author_link in all_authors:
            yield response.follow(author_link, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        name = response.css('h3.author-title::text').get().strip()
        birth_date = response.css('span.author-born-date::text').get().strip()
        birth_place = response.css('span.author-born-location::text').get().strip()
        description = response.css('div.author-description::text').get().strip()
        yield {
            'name': name,
            'birth_date': birth_date,
            'birth_place': birth_place,
            'description': description,
        }
