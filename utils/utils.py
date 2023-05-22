import os, re

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
            unique_id = result[0]
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
        return [unique_id, title, video_id]
    else:
        raise ValueError(f"file naming is inconsistent: {file_name}")