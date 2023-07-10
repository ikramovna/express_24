from elasticsearch_dsl import Document, Text


class ProductIndex(Document):
    name = Text()
    short_description = Text()
    long_description = Text()

    class Index:
        name = 'product_index'

    def save(self, **kwargs):
        return super(ProductIndex, self).save(**kwargs)
