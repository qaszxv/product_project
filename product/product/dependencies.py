from elasticsearch_dsl import DocType, Integer, Text
from elasticsearch_dsl.connections import connections


ELASTICSEARCH_URI_KEY = 'localhost'


class Product(DocType): 
    name = Text()
    staple_name = Text()
    description = Text()
    preview_image = Text()
    categories = Text()
    final_gross_price = Integer()
    final_net_price = Integer()
    url = Text()
    manufacturer = Text()

    class Meta:
        index = 'product'
    
    def save(self, ** kwargs):
        return super(Product, self).save(** kwargs)


class Storage: 
    connections.create_connection(hosts=[ELASTICSEARCH_URI_KEY])

    def create(self, payload): 
        product = Product(name = payload['name'], staple_name = payload['staple_name'])
        product.description = payload['description']
        product.preview_image = payload['preview_image']
        product.categories = payload['categories']
        product.final_gross_price = payload['final_gross_price']
        product.final_net_price = payload['final_net_price']
        product.url = payload['url']
        product.manufacturer = payload['manufacturer']
        product.save()
        
        return product.name