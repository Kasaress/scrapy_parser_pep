import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN


class PepSpider(scrapy.Spider):
    """Парсер PEP."""

    name = "pep"
    allowed_domains = [PEP_DOMAIN]
    start_urls = [f"https://{domain}/" for domain in allowed_domains]

    def parse(self, response):
        """Находит ссылки на странице PEP, для каждой
        вызывает обработчик.
        """
        for link in response.css(
            "section#numerical-index tbody tr td a::attr(href)"
        ).getall():
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Собирает информацию со страницы PEP."""
        number, name = response.css("h1.page-title::text").get().split(" – ")
        data = {
            "number": number.split(" ")[1],
            "name": name,
            "status": response.css(
                'dt:contains("Status") + dd abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
