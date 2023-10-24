# Before Start the Application
* Install required dependencies using pip (Python 3.11 used)
* Update the host, username, password credentials in `dataset/elasticsearch_client.py` file.
* Run the `dataset/create_index.py` file to create the index and upload data to elasticsearch.

# Start the Application
* Run the code in `main.py` .
* Search modes will be popup and follow the instructions.

# Search modes
* ``0 - Get all metaphors``
* ``1 - Search metaphors by Lyrics Phrase``
* ``2 - Search metaphors by Lyricist``
* ``3 - Search metaphors``
* ``4 - Search metaphors by source  (synonyms supported)``
* ``5 - Search metaphors by target (synonyms supported)``
* ``6 - Search metaphors by year``
* ``7 - Search metaphors by resource``
* ``8 - Search metaphors by any keyword``
* ``9 - Search metaphors by year range (Enter with this format :  <start_year>-<end_year>)``
* ``10 - Get metaphors count with Gender``
* ``11 - Get metaphors count with Year range (Enter with this format :  <start_year>-<end_year>)``