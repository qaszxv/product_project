from product.model import Product


def test_can_create_product(): 
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

    product = Product(  name = payload['name'],
                        staple_name = payload['staple_name'],
                        description = payload['description'],
                        preview_image = payload['preview_image'],
                        categories = payload['categories'],
                        final_gross_price = payload['final_gross_price'],
                        final_net_price = payload['final_net_price'],
                        url = payload['url'],
                        manufacturer = payload['manufacturer'])

    product.save()
    assert product.name == "Fäustel DIN6475 2000g Eschenstiel FORTIS"   