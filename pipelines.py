import sqlite3


class CovidapiPipeline:

    def process_item(self, item, spider):
        return item

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("covid_stats.db")
        self.curr = self.conn.cursor()

    # def create_table(self):

        


