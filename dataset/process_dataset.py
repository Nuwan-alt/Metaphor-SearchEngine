from elasticsearch_client import bulk_insert_documents, create_metaphor_index
import json
# from sinling import SinhalaStemmer

# def stem_sinhala_text(text_line: str):
#     stemmer = SinhalaStemmer()
#     text_line = text_line.lstrip().rstrip()
#     words = text_line.split()
#     stemmed_words = [stemmer.stem(i)[0] for i in words]
#     return ' '.join(stemmed_words)

def main():
    json_file_path = "data.json"
    print("==================================")

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        metaphor_documents = json.load(json_file)

    print(len(metaphor_documents), 'metaphor documents found.')

    create_metaphor_index()
    print(bulk_insert_documents(metaphor_documents))
