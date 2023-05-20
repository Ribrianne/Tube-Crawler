from handlers.status_handler import print_status
import query_handler, playlist_handler, url_handler, channel_handler

def download_music(music_config):
    print_status("Reading music configurations")

    format = music_config['format']
    queries_file = music_config['queries']
    query_type = music_config['query_type']
    download_directory = music_config['directory']

    print_status("Reading queries from music.txt")

    # Read the queries from the file
    with open(queries_file, 'r') as file:
        queries = file.read().splitlines()
        if query_type == "query": query_handler(queries)
        if query_type == "url": url_handler(queries)
        if query_type == "playlist": playlist_handler(queries)
        if query_type == "channel_url": channel_handler(queries)
