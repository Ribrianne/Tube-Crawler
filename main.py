import yaml
from modules import music, podcasts

# read the source.yml file
with open('./sources/source.yml', 'r') as file:
    config = yaml.safe_load(file)

# Extract the media_type field from configuration file
media_type = config['media_type']

# Call the appropriate function based on the media_type
if media_type == 'Music':
    music.download_music(config['Music'])
elif media_type == 'Podcasts':
    podcasts.download_podcasts(config['Podcasts'])