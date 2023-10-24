from dataset import search, tokenize_text, agg_search


def get_all():
    query = {
        'match_all': {}
    }
    return search(query)


def search_by_lyrics(search_term):
    query = {
        'match': {
            'Lyrics': search_term
        }
    }
    return search(query)


def search_by_lyricist(search_term):
    query = {
        'match': {
            'Lyricist': search_term
        }
    }
    return search(query)


def search_metaphor(search_term):
    query = {
        'match': {
            'Metaphor': search_term
        }
    }
    return search(query)


def search_by_source(search_term):
    query = {
        'match': {
            'Source': {
                'query': search_term,
                'analyzer': 'plain_with_synonyms'
            }
        }
    }
    return search(query)


def search_by_target(search_term):
    query = {
        'match': {
            'Target': {
                'query': search_term,
                'analyzer': 'plain_with_synonyms'
            }
        }
    }
    return search(query)


def search_by_any(search_term):
    query = {
        'multi_match': {
            'query': search_term,
            'type': "most_fields",
            "fields": ["Lyrics", "Lyricist", "Metaphor", "Meaning", "Source", "Target", "Resourse", "Gender"]
        }
    }
    return search(query)


def search_by_date_range(start, end):
    query = {
        "range": {
            "Year": {
                "gte": start,
                "lte": end
            }
        }
    }
    return search(query)

def filter_to_maps():
    aggs_query = {
        "product": {
            "terms": {"field": "Gender"}
        }
    }
    search_request = {
        "size": 0,  # Set the size to 0 to only get aggregation results
        "aggs": aggs_query
    }

    return agg_search(search_request)


def bucket_search(search_term):
    data = filter_to_maps()
    max_key_length = max(len(item['key']) for item in data)

    # Print the formatted values
    for item in data:
        print(f"{item['key']} : {item['doc_count']:{max_key_length}}")

    return



def multi_search(search_term: str, mode: int):
    if mode == 0:

        return get_all()
    elif mode == 1:
        return search_by_lyrics(search_term)
    elif mode == 2:
        return search_by_lyricist(search_term)
    elif mode == 3:
        return search_metaphor(search_term)
    elif mode == 4:
        return search_by_source(search_term)
    elif mode == 5:
        return search_by_target(search_term)
    elif mode == 6:
        return search_by_any(search_term)
    elif mode == 7:
        lst = search_term.split("-")
        return search_by_date_range(lst[0], lst[1])
    elif mode == 8:
        bucket_search(search_term)
    else:
        raise RuntimeError('Invalid search mode')

