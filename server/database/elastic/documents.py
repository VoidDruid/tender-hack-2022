from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, InnerDoc, Object
from elasticsearch_dsl.connections import connections


class Product(Document):
    id = Integer()
    name = Text()
    category = Text()
    code = Text()
    properties = Object()

    class Index:
        name = 'product'
        settings = {
            "number_of_shards": 1,
        }


def init_indices():
    Product.init()
