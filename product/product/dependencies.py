from elasticsearch_dsl.connections import connections

from product import model


ELASTICSEARCH_URI_KEY = 'localhost'


class Storage: 
    connections.create_connection(hosts=[ELASTICSEARCH_URI_KEY])

    def create(self, model): 
        model.save()

        return model