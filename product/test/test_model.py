# from elasticsearch import Elasticsearch
# from elasticsearch_dsl import connections
# from elasticsearch_dsl import Search
# import pytest

# from product.model import Product


# @pytest.fixture
# def escon(): 
#     return connections.create_connection(hosts=['localhost'], timeout=20)

# @pytest.fixture
# def product(): 
#     payload = { "id": 1,
#                 "name": "Fäustel DIN6475 2000g Eschenstiel FORTIS",
#                 "staple_name": "Fortis Fäustel, mit Eschen-Stiel",
#                 "description": "Fäustel DIN 6475<br><br>Stahlgeschmiedet, Kopf schwarz lackiert, Bahnen poliert, doppelt geschweifter Eschenstiel mit ozeanblau lackiertem Handende. SP11968 SP11968",
#                 "preview_image": "faeustel-din6475-2000g-eschenstiel-fortis-21049292-0-JlHR5nOi-l.jpg",
#                 "categories": [
#                   "Fäustel",
#                   "Handwerkzeug",
#                   "Hammer",
#                   "Fäustel"
#                 ],
#                 "final_gross_price": "1149",
#                 "final_net_price": "1003",
#                 "url": "/handwerkzeug/fortis-faeustel-mit-eschen-stiel-SP11968",
#                 "manufacturer": "Fortis",
#             }

#     return Product( meta={'id': 1}, 
#                     name = payload['name'],
#                     staple_name = payload['staple_name'],
#                     description = payload['description'],
#                     preview_image = payload['preview_image'],   
#                     categories = payload['categories'],
#                     final_gross_price = payload['final_gross_price'],
#                     final_net_price = payload['final_net_price'],
#                     url = payload['url'],
#                     manufacturer = payload['manufacturer'])

# def test_can_create_product(): 
#     test_product = product()
#     assert test_product.save(using=escon()) == True



