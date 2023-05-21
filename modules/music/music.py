from handlers.status_handler import print_status
from handlers.yt_download_handler import yt_download_handler

def download_music(music_config):
    print_status("Reading configurations: format, queries, query_type, directory")

    queries_file = music_config['queries']
    query_type = music_config['query_type']

    print_status(f"Reading queries from {queries_file}")

    # Read the queries from the file
    with open(queries_file, 'r') as file:
        queries = file.read().splitlines()
        
        match query_type:
            case 'url':
                yt_download_handler(music_config, queries)
            case _:
                #TODO:
                raise NotImplementedError(f"Downloading Music from {query_type} is not implemented yet!")
            
def write_music_file_outtmpl():
    return "[0] [%(title)s].%(ext)s"