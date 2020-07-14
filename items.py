from scrapy.item import Field


class CovidItem:

    def __init__(self):
        self.dict = {
            "country": Field(),
            "total_cases": Field(),
            "deaths": Field(),
            "recovered": Field(),
            "active_cases": Field()
        }

    def get_info(self):
        return self.dict
