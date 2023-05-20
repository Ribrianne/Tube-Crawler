import yaml
from modules import music
from validators import music_validator

# read the source.yml file
with open('./sources/source.yml', 'r') as file:
    config = yaml.safe_load(file)
    music_config = config['Music']

# Extract the media_type field from configuration file
media_type = config['media_type']

# Call the appropriate function based on the media_type
if media_type == 'Music':
    music_validator.validate_music_config(music_config)
    music.download_music(music_config)

## Add more later
#elif media_type == 'Podcasts':
    #podcasts.download_podcasts(config['Podcasts'])