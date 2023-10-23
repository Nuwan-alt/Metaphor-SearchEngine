from dataset import search, tokenize_text


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

# def filter_to_maps():
#     aggs = {
#
#     }

# def bucket_search():



def multi_search(search_term: str, mode: int):
    if mode == 0:

        res = get_all()
    elif mode == 1:
        res = search_by_lyrics(search_term)
    elif mode == 2:
        res = search_by_lyricist(search_term)
    elif mode == 3:
        res = search_metaphor(search_term)
    elif mode == 4:
        res = search_by_source(search_term)
    elif mode == 5:
        res = search_by_target(search_term)
    elif mode == 6:
        res = search_by_any(search_term)
    elif mode == 7:
        lst = search_term.split("-")
        res = search_by_date_range(lst[0], lst[1])
    else:
        raise RuntimeError('Invalid search mode')

    return res
