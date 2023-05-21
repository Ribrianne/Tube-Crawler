from handlers.status_handler import print_status

def download_music(music_config):
    print_status("Reading configurations: format, queries, query_type, directory")

    format = music_config['format']
    queries_file = music_config['queries']
    query_type = music_config['query_type']
    download_directory = music_config['directory']

    print_status("Reading queries from music.txt")

    # Read the queries from the file
    with open(queries_file, 'r') as file:
        queries = file.read().splitlines()
        
        if query_type == "url":
            print("ok")
            # logic for downloading music from youtube
        else:
            print_status("Sorry, Only url Query Type is Supported For Now!", "warning")
