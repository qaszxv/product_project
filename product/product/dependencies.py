from nameko.extensions import DependencyProvider
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search

from product.model import Product
from product.exceptions import NotFound


ELASTICSEARCH_URI = 'localhost:9200'


class StorageWrapper: 
    NotFound = NotFound

    def __init__(self, client): 
        self.client = client

    def create(self, product): 
        product.save(using=self.client)

    def get(self, product_id): 
        try: 
            product = Product.get(using=self.client, id=product_id) 
        except:
            raise NotFound('Product ID {} does not exist'.format(product_id))
        else: 
            return product

    def update(self, product_id, **kwargs): 
        try: 
            product = self.get(product_id)
        except: 
            raise NotFound('Product not found')

        product.update(**kwargs)

    def delete(self, product): 
        search_client = Elasticsearch()
        s = Search(index=product.meta.index).using(search_client).query("match", _id=product.meta.id)
        response = s.delete()

class Storage(): 
    def setup(self): 
        self.client = connections.create_connection(hosts=[ELASTICSEARCH_URI], timeout=20)

    def get_dependency(self, worker_ctx): 
        return StorageWrapper(self.client)