import yaml
from modules.music import music
from validators import music_validator
from handlers.status_handler import print_status

print_status("Reading source.yml file")

# read the source.yml file
with open('./sources/source.yml', 'r') as file:
    config = yaml.safe_load(file)
    music_config = config['Music']

# Extract the media_type field from configuration file
media_type = config['media_type']

# Call the appropriate function based on the media_type
match media_type:
    case 'Music':
        print_status(f"Detected Media Type: {media_type}")

        music_validator.validate_music_config(music_config)
        music.download_music(music_config)
    case _:
        raise NotImplementedError(f"Downloading {media_type} is not implemented yet!")
    
print_status("Tube Crawler has crawled its way to the end!")