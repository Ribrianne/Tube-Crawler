def validate_music_config(music_config):
    # Check if required fields are present
    required_fields = ['format', 'directory', 'query_type', 'queries']

    for field in required_fields:
        if field not in music_config:
            raise ValueError(f"Missing required field in source.yml - Music: {field}")
    
    # Validate values inside required fields
    supported_formats = ['mp3', 'wav', 'flac']
    if music_config['format'] not in supported_formats:
        raise ValueError("Invalid format specified in Music - source.yml")
    
    supported_query_types = ['query', 'url', 'playlist', 'channel_url']
    if music_config['query_type'] not in supported_query_types:
        raise ValueError("Invalid query_type specified in Music - source.yml")
    
    # if all checks pass, return True
    return True