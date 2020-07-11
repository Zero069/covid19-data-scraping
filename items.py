import scrapy
from scrapy.loader.processors import MapCompose


class ScrapData(scrapy.Spider):
    name = "scrape table"
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        last_element_number = "215"  # Number assigned to country in table
        table = response.xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[3]')
        columns = table.xpath("//tr")

        for row in columns:
            country = row.xpath("td[2]//text()").extract_first()

            if last_element_number == row.xpath("td[1]//text()").extract_first():
                break

            if "\n" == country:  # Skips elements with a null country value = no country
                continue

            else:
                yield {
                    "Country": row.xpath("td[2]//text()").extract_first(),
                    "Total Cases": row.xpath("td[3]//text()").extract_first(),
                    "Total Deaths": row.xpath("td[5]//text()").extract_first(),
                    "Total Recovered": row.xpath("td[7]//text()").extract_first(),
                    "Active Cases": row.xpath("td[9]//text()").extract_first()
                }


