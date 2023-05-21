from yt_dlp import YoutubeDL

from handlers.status_handler import print_status

def yt_download_handler(config, download_urls):
    download_format = config['format']
    download_directory = config['directory']

    download_options = {
        'format': download_format,
        'outtmpl': f'{download_directory}/%(title)s.%(ext)s'
    }
    with YoutubeDL(download_options) as ytdlp:
        ytdlp.download(download_urls)

    print(download_urls)