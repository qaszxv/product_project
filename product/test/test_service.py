import pytest
from nameko.events import event_handler
from nameko.standalone.events import event_dispatcher
from nameko.testing.services import entrypoint_waiter
from marshmallow.exceptions import ValidationError

from product.service import ProductService


def test_handle_create_product_success(container_factory, rabbit_config): 
    payload = { "name": "Fäustel DIN6475 2000g Eschenstiel FORTIS",
                "staple_name": "Fortis Fäustel, mit Eschen-Stiel",
                "description": "Fäustel DIN 6475<br><br>Stahlgeschmiedet, Kopf schwarz lackiert, Bahnen poliert, doppelt geschweifter Eschenstiel mit ozeanblau lackiertem Handende. SP11968 SP11968",
                "preview_image": "faeustel-din6475-2000g-eschenstiel-fortis-21049292-0-JlHR5nOi-l.jpg",
                "categories": [
                  "Fäustel",
                  "Handwerkzeug",
                  "Hammer",
                  "Fäustel"
                ],
                "final_gross_price": 1149,
                "final_net_price": 1003,
                "url": "/handwerkzeug/fortis-faeustel-mit-eschen-stiel-SP11968",
                "manufacturer": "Fortis",
            }

    container = container_factory(ProductService, rabbit_config)
    container.start()

    dispatch = event_dispatcher(rabbit_config)

    with entrypoint_waiter(container, 'create') as result:
        dispatch("sent_service", "sent_payload", payload)

    product = result.get()
    assert product['name'] == "Fäustel DIN6475 2000g Eschenstiel FORTIS"


def test_handle_create_product_fail(container_factory, rabbit_config): 
    container = container_factory(ProductService, rabbit_config)
    container.start()

    dispatch = event_dispatcher(rabbit_config)
    payload = { "name": "Fäustel DIN6475 2000g Eschenstiel FORTIS"}

    with pytest.raises(ValidationError) as exc_info:
        with entrypoint_waiter(container, 'create') as result:
            dispatch("sent_service", "sent_payload", payload)
        product = result.get()



