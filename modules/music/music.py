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
        
        print_status(f"Extracting urls from Query Type: {query_type}")
        match query_type:
            case "url":
                yt_download_handler(music_config, queries, create_download_options)
                
            case "playlist":
                playlist_urls = utils.extract_youtube_playlist_urls(playlist_urls=queries)
                yt_download_handler(music_config, playlist_urls, create_download_options)

            case "query":
                urls_from_queries = utils.search_youtube(search_queries=queries)

                prompt_message = "Press ENTER to continue or any other key to stop: "
                if input(f"\n {prompt_message} \n"):
                    print_status("Interuppted By User.")
                    raise SystemExit

                yt_download_handler(music_config, urls_from_queries, create_download_options)

            case "channel_url":
                urls_from_channel = utils.extract_youtube_channel_urls(channel_urls=queries)
                yt_download_handler(music_config, urls_from_channel, create_download_options)

            case _:
                raise ValueError(f"Wrong Query Type: {query_type}")