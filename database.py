import sqlite3
import mysql.connector


class MysqlDataBase(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.connection = mysql.connector.connect(host="localhost",
                                                  user="root",
                                                  passwd="BedDoorHairStairs3",
                                                  database="covid_stats")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS covid")
        self.cursor.execute("CREATE TABLE covid(country text,"
                            "total-cases,"
                            "total-deaths,"
                            "total-recovered"
                            "active-cases)")

    def store_db(self, item):
        self.cursor.execute("insert into covid values (%s,%s,%s,%s,%s)", (
            item["country"][0],
            item["author"][0],
            item["tag"][0]
        ))
        self.connection.commit()

# connection = sqlite3.connect('COVID19_DATA.db')
# curr = connection.cursor()
#
# curr.execute("CREATE TABLE COVID19(country text, "
#              "total_cases integer,"
#              "total_cured integer)")
#
# curr.execute("INSERT INTO COVID19 VALUES('Pakistan', 0, 200)")
# connection.commit()
