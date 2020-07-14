import mysql.connector
import sqlite3



class CovidapiPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = mysql.connector.connect(host="localhost",
                                                  user="root",
                                                  passwd="BedDoorHairStairs3",
                                                  database="covid_stats")
        self.cursor = self.connection.cursor()

    def create_table(self):
        # self.cursor.execute("DROP TABLE IF EXISTS covid_data")
        self.cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

        self.cursor.execute("DROP TABLE IF EXISTS covid_data")

        self.cursor.execute("CREATE TABLE covid_data(country text,"
                            "total-cases INTEGER,"
                            "total-deaths INTEGER,"
                            "total-recovered INTEGER,"
                            "active-cases INTEGER)")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.cursor.execute("insert into covid_data values (%s,%s,%s,%s,%s)", (
            item["country"][0],
            item["total_cases"][0],
            item["deaths"][0],
            item["recovered"][0],
            item["active_cases"][0],
        ))
        self.connection.commit()

# connection = sqlite3.connect('covid_data.db')
# curr = connection.cursor()
#
# curr.execute("CREATE TABLE COVID19(country text, "
#              "total_cases integer,"
#              "total_cured integer)")
#
# curr.execute("INSERT INTO COVID19 VALUES('Pakistan', 0, 200)")
# connection.commit()
