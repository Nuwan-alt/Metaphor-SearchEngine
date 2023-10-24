from search import multi_search
from ui import get_search_results_table


def take_inputs():
    mode = int(input('Enter search mode: '))
    search_term = input('Enter search query: ')

    return mode, search_term


def transform_results(results):
    total_matches = results['total']['value']
    documents = [i['_source'] for i in results['hits']]

    table_rows = []
    for doc in documents:
        row = [
            doc['Lyrics'],
            doc['Lyricist'],
            doc['Year'],
            doc['Metaphor'],
            doc['Source'],
            doc['Target'],
            doc['Meaning'],
            doc['Gender'],
            doc['Resourse'],

        ]
        table_rows.append(tuple(row))

    return total_matches, table_rows


def main():
    modes_text = open('search_modes.txt', 'r').read()

    while True:
        print(modes_text)
        mode, search_term = take_inputs()
        if mode < 0:
            break

        results = multi_search(search_term, mode)
        if mode !=8:

            total_matches, table_rows = transform_results(results)
            print('Total Matches -', total_matches)
            results_table = get_search_results_table(table_rows)
            results_table.mainloop()


main()