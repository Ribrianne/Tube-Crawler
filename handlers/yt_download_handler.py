import yaml
from yt_dlp import YoutubeDL
from handlers.status_handler import print_status
from modules.music import music

def yt_download_handler(config, download_urls):
    download_options = create_download_options(config, download_urls)
    
    with YoutubeDL(download_options) as ytdlp:
        ytdlp.download(download_urls)

def create_download_options(config, download_urls):
    download_format = config['format']
    query_type = config['query_type']
    download_directory = config['directory']

    print_status(f"Downloading {query_type} - Total {len(download_urls)} Queries")

    download_options = {
        'outtmpl': f'{download_directory}/{music.write_music_file_outtmpl()}',
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