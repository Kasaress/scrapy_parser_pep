import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        for link in response.css(
            "section#numerical-index tbody tr td a::attr(href)"
        ).getall():
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css("h1.page-title::text").get().split(" – ")
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            "number": number.split(" ")[1],
            "name": name,
            "status": status,
        }
        yield PepParseItem(data)
