import scrapy


class CovidItem(scrapy.item):
    country = scrapy.Field()
    total_cases = scrapy.Field()
    deaths = scrapy.Field()
    recovered = scrapy.Field()
    active_cases = scrapy.Field()

