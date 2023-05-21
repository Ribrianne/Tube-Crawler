import yaml
from yt_dlp import YoutubeDL
from handlers.status_handler import print_status
from modules.music import music

def yt_download_handler(config, download_urls):
    query_type = config['query_type']
    print_status(f"Downloading {query_type} - Total {len(download_urls)} Queries")

    for url in download_urls:
        download_options = create_download_options(config)
        with YoutubeDL(download_options) as ytdlp:
            #TODO: unique identifier I made is working perfectly
            # Now need to create a way to check duplicates in filenames / youtube-link
            # before I create an unique identifier, otherwise everything can be messed up
            # ytdlp.download(url)
            print("ok")

def create_download_options(config):
    download_format = config['format']
    download_directory = config['directory']


    download_options = {
        'outtmpl': music.write_music_file_outtmpl(download_directory),
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