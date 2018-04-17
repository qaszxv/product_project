import pytest
from elasticsearch_dsl.connections import connections
from mock import Mock

from product import dependencies
from product.model import Product


@pytest.fixture
def escon(): 
    return connections.create_connection(hosts=['localhost'], timeout=20)

@pytest.fixture
def storage(config):
    provider = dependencies.Storage()
    provider.container = Mock(config=config)
    provider.setup()
    return provider.get_dependency({})

@pytest.mark.order1
def test_storage_create_successful(storage, product): 
    storage.create(product)
    assert Product.get(using=escon(), id=product.meta.id) == product

@pytest.mark.order2
def test_storage_update_successful(storage): 
    storage.update(product_id=1, name='New Name', staple_name='New Stapple Name')
    product = Product.get(using=escon(), id=1, ignore = 404)
    assert product.name == "New Name"
    assert product.staple_name == "New Stapple Name"
    assert product.preview_image == "faeustel-din6475-2000g-eschenstiel-fortis-21049292-0-JlHR5nOi-l.jpg"
    assert product.categories == [  "Fäustel",
                                    "Handwerkzeug",
                                    "Hammer",
                                    "Fäustel"]
    assert product.manufacturer == "Fortis"
    assert product.final_gross_price == 1149

@pytest.mark.order3
def test_storage_get_successful(storage): 
    test_product = storage.get(product_id=1)
    product = Product.get(using=escon(), id=1, ignore = 404)
    assert test_product.name == product.name

@pytest.mark.order4
def test_storage_get_fail_on_not_found(storage): 
    with pytest.raises(storage.NotFound) as exc:
        storage.get(2)
    assert 'Product ID 2 does not exist' == exc.value.args[0]
    
@pytest.mark.order5
def test_storage_delete_successful(storage, product):
    storage.delete(product)
    p = Product.get(using=escon(), id=product.meta.id, ignore = 404)
    assert p is None