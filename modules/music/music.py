from handlers.status_handler import print_status
import os, re
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
    video_id = "%(id)s"

    template = f"{directory}/[{unique_id}] [{title}] [{video_id}].{ext}"

    return template

def create_next_unique_id(directory):
    existing_ids = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.mp3'):
            result = extract_mp3_file_info(file_name)
            unique_id = result[0]
            existing_ids.append(unique_id)

    next_id = max(existing_ids) + 1 if existing_ids else 0

    return next_id

def extract_mp3_file_info(file_name):
    pattern = r'\[(.*?)\]'  # Matches text inside square brackets
    matches = re.findall(pattern, file_name)

    if len(matches) == 3:
        unique_id = int(matches[0])
        title = matches[1]
        video_id = matches[2]
        return [unique_id, title, video_id]
    else:
        return None