from search import multi_search
from ui import get_search_results_table


def take_inputs():
    mode = int(input('Enter search mode: '))

    if mode == 0 or mode == 10 or mode == -1:
        search_term = "kk"
    else:
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
    file_path = 'welcome.txt'  # Replace with the path to your file
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    modes_text = open('search_modes.txt', 'r').read()

    while True:
        print(modes_text)
        mode, search_term = take_inputs()
        if mode < 0:
            file_path_1 = 'thank.txt'  # Replace with the path to your file
            try:
                with open(file_path_1, 'r') as file:
                    file_contents = file.read()
                    print(file_contents)
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
            modes_text = open('search_modes.txt', 'r').read()
            break

        results = multi_search(search_term, mode)
        if mode != 10 and mode != 11:
            total_matches, table_rows = transform_results(results)
            print(' **************** Total Matches - ' + str(total_matches) + ' ****************')
            results_table = get_search_results_table(table_rows)
            results_table.mainloop()


main()
