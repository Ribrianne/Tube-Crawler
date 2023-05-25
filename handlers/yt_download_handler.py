import yaml
from yt_dlp import YoutubeDL
from handlers.status_handler import print_status
from utils import utils

def yt_download_handler(config, download_urls, create_download_options):
    query_type = config['query_type']
    download_format = config['format']
    download_directory = config['directory']
    download_history_txt_path = f"{download_directory}/.download_history.txt"
        
    utils.update_download_history(download_format, download_directory, download_history_txt_path)

    print_status(f"Downloading {query_type} - Total {len(download_urls)} Queries")

    for url in download_urls:
        download_options = create_download_options()
        with YoutubeDL(download_options) as ytdlp:
            ytdlp.download(url)