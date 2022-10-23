from elasticsearch_dsl.connections import connections


def main():
    import database.elastic

    print(connections.get_connection().cluster.health())
