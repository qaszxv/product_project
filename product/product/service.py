from nameko.events import event_handler
from nameko.rpc import rpc

from product import dependencies
from product import schemas


class ProductService: 
    name = "product_service"

    storage = dependencies.Storage()

    @event_handler("sent_service", "sent_payload")
    def create(self, payload): 
        product = schemas.Product(strict=True).load(payload).data
        print(product['categories'])
        self.storage.create(product)

        return product
