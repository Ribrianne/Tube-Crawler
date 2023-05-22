import os, re
from handlers.status_handler import print_status

# Generates a template for the output file name based on the given directory and file format.
# Returns: str: The generated template for the output file name.
# Example:
#    If directory = '/path/to/directory' and file_format = 'mp3', the template would be:
#    '/path/to/directory/[unique_id] [title] [video_id].mp3'
def write_file_outtmpl(directory, file_format):
    unique_id = create_next_unique_id(directory, file_format)
    title = "%(title)s"
    ext = "%(ext)s"
    video_id = "%(id)s"

    template = f"{directory}/[{unique_id}] [{title}] [{video_id}].{ext}"

    return template

# Generates the next unique ID for a file based on the existing files in the directory.
# Args:
#    directory (str): The directory where the files are located.
#    file_format (str): The file format or extension.
# Returns:
#    int: The next unique ID.
def create_next_unique_id(directory, file_format):
    existing_ids = []
    for file_name in os.listdir(directory):
        if file_name.endswith(f".{file_format}"):
            result = extract_file_info(file_name)
            unique_id = result['unique_id']
            existing_ids.append(unique_id)

    next_id = max(existing_ids) + 1 if existing_ids else 0

    return next_id

# Extracts the file information (unique ID, title, and video ID) from a given file name.
# Args:
#    file_name (str): The name of the file.
# Returns:
#    list: A list containing the unique ID, title, and video ID.
#    Returns None if the file name does not match the expected pattern.
def extract_file_info(file_name):
    pattern = r'\[(.*?)\]'  # Matches text inside square brackets
    matches = re.findall(pattern, file_name)

    if len(matches) == 3:
        unique_id = int(matches[0])
        title = matches[1]
        video_id = matches[2]
        return {
            'unique_id': unique_id,
            'title': title,
            'video_id': video_id
        }
    else:
        raise ValueError(f"file naming is inconsistent: {file_name}")
    
# update download_history.txt file from
# looking through video id of file names
# adding them in download_history.txt
# renaming every file if unique_id got messed up!
def update_download_history(file_extension, download_directory, download_history_txt_path):

    print_status(f"Checking Unique IDs From {file_extension} files", delay=2)

    fix_unique_ids(download_directory, file_extension)

    print_status(f"Updating Download History: {download_history_txt_path}")

    if not os.path.isfile(download_history_txt_path):
        print_status("No Previous Download History Found!")
    else:
        video_ids = []
        for file_name in os.listdir(download_directory):
            if file_name.endswith(file_extension):
                result = extract_file_info(file_name)
                video_id = result["video_id"]
                video_ids.append(f"youtube {video_id}")

        with open(download_history_txt_path, 'w') as file:
            for video_id in video_ids:
                file.write(video_id + "\n")

        print_status(f"Updated Download History!")

# fix unique ids from files in a directory
# by renaming them if nessesary
def fix_unique_ids(directory, file_extension):
    all_files = [file for file in os.listdir(directory) if file.endswith(file_extension)]
    all_files.sort()

    expected_id = 0
    for file in all_files:
        result = extract_file_info(file)
        current_id = result["unique_id"]

        if current_id != expected_id:
            print_status(f"Warning: Unique IDs are not Sorted!", color="warning")

            title = result["title"]
            video_id = result["video_id"]
            new_file_name = f"[{expected_id}] [{title}] [{video_id}].{file_extension}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))

        expected_id += 1