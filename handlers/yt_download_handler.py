import yaml, yt_dlp
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
        with yt_dlp.YoutubeDL(download_options) as ydl:
            try:
                ydl.download(url)
            except yt_dlp.utils.DownloadError as e:
                error_message = str(e)
                if "Video unavailable" in error_message:
                    print_status("Video Unavilable, Skipping Download", "warning", delay=3)
                else:
                    raise e