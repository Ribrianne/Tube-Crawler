from handlers.status_handler import print_status
import os
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
            
def write_music_file_outtmpl(directory):
    unique_id = create_next_unique_id(directory)
    title = "%(title)s"
    ext = "%(ext)s"

    template = f"{directory}/[{unique_id}] [{title}].{ext}"

    return template

def create_next_unique_id(directory):
    existing_ids = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.mp3'):
            start_index = file_name.find('[') + 1  # Finding the index of the opening bracket
            end_index = file_name.find(']')  # Finding the index of the closing bracket
            unique_id = int(file_name[start_index:end_index])
            existing_ids.append(unique_id)

    next_id = max(existing_ids) + 1 if existing_ids else 0

    return next_id