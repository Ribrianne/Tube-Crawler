import yaml
from yt_dlp import YoutubeDL
from handlers.status_handler import print_status
from modules.music import music

def yt_download_handler(config, download_urls):
    # update download_history.txt file from
    # looking through video id of file names
    # adding them in download_history.txt
    # renaming every file using create_next_unique_id()
    #TODO:
#   update_download_history()

    query_type = config['query_type']
    print_status(f"Downloading {query_type} - Total {len(download_urls)} Queries")

    for url in download_urls:
        download_options = create_download_options(config)
        with YoutubeDL(download_options) as ytdlp:
            ytdlp.download(url)

def create_download_options(config):
    download_format = config['format']
    download_directory = config['directory']


    download_options = {
        'outtmpl': music.write_music_file_outtmpl(download_directory),
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