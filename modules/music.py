def download_music(music_config):
    format = music_config['format']
    queries_file = music_config['queries']
    query_type = music_config['query_type']
    download_directory = music_config['directory']

    print(f"Format: {format}")
    print(f"Queries File: {queries_file}")
    print(f"Query Type: {query_type}")
    print(f"Download Directory: {download_directory}")

    # Read the queries from the file
    with open(queries_file, 'r') as file:
        queries = file.read().splitlines()