import yaml
from yt_dlp import YoutubeDL
from handlers.status_handler import print_status
from utils import utils

def yt_download_handler(config, download_urls):
    query_type = config['query_type']
    download_format = config['format']
    download_directory = config['directory']
    download_history_txt_path = f"{download_directory}/download_history.txt"
        
    utils.update_download_history(download_format, download_directory, download_history_txt_path)

    print_status(f"Downloading {query_type} - Total {len(download_urls)} Queries")

    for url in download_urls:
        download_options = create_download_options(download_directory, download_format)
        with YoutubeDL(download_options) as ytdlp:
            ytdlp.download(url)

def create_download_options(download_directory, download_format):


    download_options = {
        'outtmpl': utils.write_file_outtmpl(download_directory, download_format),
        'download_archive': f"{download_directory}/download_history.txt",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': download_format,
            'preferredquality': '320',
        }],
    }
    with open('./sources/source.yml', 'r') as file:
        yml_config = yaml.safe_load(file)
        media_type = yml_config['media_type']

    if media_type == 'Music': download_options['format'] = 'bestaudio/best'
    
    return download_options