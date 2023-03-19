import scrapy


class PepParseItem(scrapy.Item):
    """Класс для хранения данных PEP."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
