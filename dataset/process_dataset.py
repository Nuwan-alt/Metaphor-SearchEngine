from elasticsearch_client import bulk_insert_documents, create_metaphor_index
import json

def main():
    json_file_path = "data.json"
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        metaphor_documents = json.load(json_file)

    print(len(metaphor_documents), 'metaphor documents found.')

    create_metaphor_index()
    print(bulk_insert_documents(metaphor_documents))
