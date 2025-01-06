import os
import pandas
from pymongo import MongoClient

class MongoConnection:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._client = None
            cls._instance._db = None
            cls._instance._collection = None
        return cls._instance
    

    def __init__(self, host='localhost', port=27017, database='test', collection='data'):
        if self._client is None:
            self.host = os.getenv("MONGO_HOST", host)
            self.port = os.getenv("MONGO_PORT", port)
            self.database_name = os.getenv("MONGO_DATABASE", database)
            self.collection = os.getenv("MONGO_COLLECTION", collection)
            self._connect()

    def _connect(self):
        self._client = MongoClient(self.host, int(self.port))
        self._db = self._client[self.database_name]
        self._collection = self._db[self.collection]

    def save_dataframe(self, df):
        data = df.to_dict(orient='records')
        try:
            self._collection.insert_many(data)
        except:
            print('Não foi possível salvar na collection')

    def close_connection(self):
        if self._client:
            self._client.close()
            print('Conexão com o Mongo Encerrada!')