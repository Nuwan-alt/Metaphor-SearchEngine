import json
from elasticsearch import Elasticsearch, helpers

def elasticsearch_config():
    return {
        'host': 'CS-4642:YXAtc291dGhlYXN0LTEuYXdzLmZvdW5kLmlvJGZkODg5MWQzZWQxYzRjMmZhYzMyZWRhMDhhNmJlMWE3JDA3NDA1OTNmZmJiMDRhMjQ4ZjRhYzBlOGMxYmMwNWNk',
        'username': 'elastic',
        'password': 'xbqraUMgQGj8lYoaqL61Mz5P',
        'index_name': 'metaphors'
    }

def get_client() -> Elasticsearch:
    c = elasticsearch_config()
    return Elasticsearch(cloud_id=c['host'],
                         basic_auth=(c['username'], c['password']))

def delete_metaphor_index():
    c = elasticsearch_config()
    client = get_client()
    print(client.indices.delete(index=c['index_name'], ignore_unavailable=True))


def create_metaphor_index():
    c = elasticsearch_config()
    index_name = c['index_name']
    with open('elasticsearch/metaphors_index_config.json', mode='r', encoding='utf_8') as json_file:
        config = json.load(json_file)

    client = get_client()
    print(client.indices.delete(index=index_name, ignore_unavailable=True))
    print(client.indices.create(index=index_name, settings=config['settings'], mappings=config['mappings']))

def tokenize_text(text, analyzer='plain'):
    c = elasticsearch_config()

    client = get_client()
    res = client.indices.analyze(index=c['index_name'], analyzer=analyzer, text=text)
    return res['tokens'], ' '.join([t['token'] for t in res['tokens']])


def bulk_insert_documents(docs):
    client = get_client()
    c = elasticsearch_config()
    return helpers.bulk(client=client,actions=docs, index=c['index_name'])

def search(query, size=100):

    client = get_client()
    c = elasticsearch_config()

    res = client.search(index=c['index_name'], query=query, size=size)

    if res['timed_out']:
        raise RuntimeError('Search request timed out.')
    return res['hits']

def agg_search(search_request):
    client = get_client()
    c = elasticsearch_config()
    result = client.search(index=c['index_name'], body=search_request)
    aggregation_results = result['aggregations']['product']['buckets']

    return aggregation_results