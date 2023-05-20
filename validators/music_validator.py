import os

def validate_music_config(music_config):
    # Check if required fields are present
    required_fields = ['format', 'directory', 'query_type', 'queries']

    for field in required_fields:
        if field not in music_config:
            raise ValueError(f"Missing required field: {field} in source.yml - Music")
    
    # Validate values inside required fields
    supported_formats = ['mp3', 'wav', 'flac']
    if music_config['format'] not in supported_formats:
        raise ValueError("Invalid format specified in Music - source.yml")
    
    directory_path = music_config['directory']
    if os.path.isdir(directory_path):
        raise ValueError("Invalid directory path specified in Music - source.yml")
    
    supported_query_types = ['query', 'url', 'playlist', 'channel_url']
    if music_config['query_type'] not in supported_query_types:
        raise ValueError("Invalid query_type specified in Music - source.yml")
    
    queries_file = music_config['queries']
    if os.path.getsize(queries_file) == 0:
        raise ValueError("music.txt file is empty - no queries to search for / download")
    
    # if all checks pass, return True
    return True