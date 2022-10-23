from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from loguru import logger

from settings import elastic_settings

client = Elasticsearch(elastic_settings.URI, timeout=30)

connections.create_connection(hosts=[elastic_settings.URI])


default_settings = {"number_of_shards": 1, "number_of_replicas": 0}

default_config = {"mappings": {"dynamic": True}}


def create_index(es: Elasticsearch, index_name: str, index_config=None, settings=None):
    if index_config is None:
        index_config = default_config
    if settings is None:
        settings = default_settings

    config = {"settings": settings, **index_config}

    try:
        if not es.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es.indices.create(index=index_name, ignore=400, body=config)
    except Exception:
        logger.exception("Could not create index")
        return False
    return True
