import pymongo


class CovidapiPipeline(object):
    def __init__(self):
        # creating connection with mongoDB
        self.connection = pymongo.MongoClient(
            'localhost',
            27017  # port
        )
        self.db = self.connection['coviddata']  # creating a database
        self.collection = self.db['covid_stats']  # creating a table within db

    def process_item(self, item, spider):
        self.collection.insert(dict(item))  # MnogoDb stores data using a dictionary to avoid collisions.
        self.connection.__init__()
        return item

    def get_data(self, country):
        hasData = True
        country = country.lower()
        if hasData:
            return self.collection.find_one({"country": country})
        else:
            return country + " Does not exist in our records"
