import sqlite3


connection = sqlite3.connect('COVID19_DATA.db')
curr = connection.cursor()

curr.execute("CREATE TABLE COVID19(country text, "
             "total_cases integer,"
             "total_cured integer)")


curr.execute("INSERT INTO COVID19 VALUES('Pakistan', 0, 200)")
connection.commit()











