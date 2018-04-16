import pytest
from product import dependencies
from product.model import Product


def test_storage_create_successful(): 
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
                "final_gross_price": "1149",
                "final_net_price": "1003",
                "url": "/handwerkzeug/fortis-faeustel-mit-eschen-stiel-SP11968",
                "manufacturer": "Fortis",
            }

    storage = dependencies.Storage()
    product = Product(payload)
    assert storage.create(product) == product


def test_storage_create_fail_missing_value():
    model = { "name": "Fäustel DIN6475 2000g Eschenstiel FORTIS"}

    with pytest.raises(AttributeError): 
        storage = dependencies.Storage()
        storage.create(model)