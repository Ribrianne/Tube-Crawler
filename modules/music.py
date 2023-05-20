def download_music(music_config):
    format = music_config['format']
    queries_file = music_config['queries']
    query_type = music_config['query_type']
    download_directory = music_config['directory']

    # Read the queries from the file
    with open(queries_file, 'r') as file:
        queries = file.read().splitlines()