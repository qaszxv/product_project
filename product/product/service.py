from nameko.events import event_handler
from nameko.rpc import rpc

from product import dependencies
from product.model import Product
from product import schemas


class ProductService: 
    name = "product_service"

    storage = dependencies.Storage()

    @event_handler("sent_service", "sent_payload")
    def create(self, payload): 
        payload = schemas.Product(strict=True).load(payload).data
        product = Product(  name = payload['name'],
                            staple_name = payload['staple_name'],
                            description = payload['description'],
                            preview_image = payload['preview_image'],
                            categories = payload['categories'],
                            final_gross_price = payload['final_gross_price'],
                            final_net_price = payload['final_net_price'],
                            url = payload['url'],
                            manufacturer = payload['manufacturer'])
        self.storage.create(product)
        
        return product
