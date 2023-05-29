import pprint
from handlers.status_handler import print_status
from handlers.yt_download_handler import yt_download_handler
from utils import utils

def download_music(music_config):
    print_status("Reading configurations: format, queries, query_type, directory")

    queries_file = music_config['queries']
    query_type = music_config['query_type']
    download_format = music_config['format']
    download_directory = music_config['directory']

    print_status(f"Creating Download Options For {query_type}")

    def create_download_options():
        download_options = {
        'format': 'bestaudio/best',
        'outtmpl': utils.write_file_outtmpl(download_directory, download_format),
        'download_archive': f"{download_directory}/.download_history.txt",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': download_format,
            'preferredquality': '320',
        }],
        }
        return download_options

    print_status(f"Reading queries from {queries_file}")

    # Read the queries from the file
    with open(queries_file, 'r') as file:
        queries = file.read().splitlines()
        
        match query_type:
            case 'url':
                yt_download_handler(music_config, queries, create_download_options)
            case 'playlist':
                print_status("Extracting Url From Playlists")
                playlist_urls = utils.extract_youtube_playlist_urls(queries)
                yt_download_handler(music_config, playlist_urls, create_download_options)
            case _:
                #TODO:
                raise NotImplementedError(f"Downloading Music from {query_type} is not implemented yet!")