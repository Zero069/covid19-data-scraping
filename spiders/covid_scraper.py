# Main Class, web crawling occurs in this class
import scrapy
from covidAPI.items import CovidItem


class ScrapData(scrapy.Spider):
    name = "scrape"  # Name of Spider
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        items = CovidItem().get_info()

        table = response.xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr[3]')

        last_element_number = "215"  # Number assigned to country in table on the website

        columns = table.xpath("//tr")  # Extracting the columns of the desired table.

        for row in columns:
            country = row.xpath("td[2]//text()").extract_first()

            if last_element_number == row.xpath("td[1]//text()").extract_first():
                break

            if "\n" == country:  # Skips elements with a null country value. Null Country = No data
                continue

            else:
                # Adding scraped data into the items list
                items["country"] = row.xpath("td[2]//text()").extract_first()
                items["total_cases"] = row.xpath("td[3]//text()").extract_first()
                items["deaths"] = row.xpath("td[5]//text()").extract_first()
                items["recovered"] = row.xpath("td[7]//text()").extract_first()
                items["active_cases"] = row.xpath("td[9]//text()").extract_first()
                yield items
