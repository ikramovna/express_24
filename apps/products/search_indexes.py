from elasticsearch_dsl import Document, Text, Index


class ProductDocument(Document):
    name = Text()
    short_description = Text()
    long_description = Text()

    class Index:
        name = 'my_elasticsearch_index'
