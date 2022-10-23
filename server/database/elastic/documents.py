from elasticsearch_dsl import Date, Document, InnerDoc, Integer, Keyword, Object, Text, analyzer, token_filter
from elasticsearch_dsl.connections import connections


search_synonym = token_filter(
    "search_synonym",
    type="synonym",
    ignore_case="true",
    synonyms=[
        "пончо,накидка",  # TODO
    ]
)
ru_stemmer = token_filter(
    "ru_stemmer",
    type="stemmer",
    language="russian"
)
eng_stemmer = token_filter(
    "eng_stemmer",
    type="stemmer",
    language="english"
)
ru_stopwords = token_filter(
    "ru_stopwords",
    type="stop",
    stopwords=['а', 'без', 'более', 'бы', 'был', 'была', 'были', 'было', 'быть', 'в', 'вам', 'вас', 'весь', 'во', 'вот', 'все', 'всего', 'всех', 'вы', 'где', 'да', 'даже', 'для', 'до', 'его', 'ее', 'если', 'есть', 'еще', 'же', 'за', 'здесь', 'и', 'из', 'или', 'им', 'их', 'к', 'как', 'ко', 'когда', 'кто', 'ли', 'либо', 'мне', 'может', 'мы', 'на', 'надо', 'наш', 'не', 'него', 'нее', 'нет', 'ни', 'них', 'но', 'ну', 'о', 'об', 'однако', 'он', 'она', 'они', 'оно', 'от', 'очень', 'по', 'под', 'при', 'с', 'со', 'так', 'также', 'такой', 'там', 'те', 'тем', 'то', 'того', 'тоже', 'той', 'только', 'том', 'ты', 'у', 'уже', 'хотя', 'чего', 'чей', 'чем', 'что', 'чтобы', 'чье', 'чья', 'эта', 'эти', 'это', 'я', 'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for', 'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or', 'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they', 'this', 'to', 'was', 'will', 'with'],
)
gram_analyzer = token_filter(
    "gram_analyzer",
    type="ngram",
    min_gram=4,
    max_gram=4,
    token_chars=[
        "letter",
    ],
)
russian_analyzer = analyzer(
    'russian_analyzer',
    type="custom",
    tokenizer="standard",
    filter=[
        "lowercase",
        gram_analyzer,
        ru_stemmer,
        eng_stemmer,
        ru_stopwords
    ]
)
product_search = analyzer(
    'product_search',
    type="custom",
    tokenizer="standard",
    filter=[
        "lowercase",
        ru_stemmer,
        eng_stemmer,
        ru_stopwords
    ]
)


class Product(Document):
    id = Integer()
    name = Text(analyzer=russian_analyzer)
    word_cloud = Text(analyzer=product_search)

    class Index:
        name = 'product'
        settings = {
            "number_of_shards": 5,
            "analysis": {
                "analyzer": {
                    "default": russian_analyzer
                },
            }
        }


def init_indices():
    Product.init()
