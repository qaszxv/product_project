from elasticsearch_dsl import DocType, Integer, Text


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