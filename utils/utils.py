import os, re, yt_dlp, pprint
from handlers.status_handler import print_status

# Generates a template for the output file name based on the given directory and file format.
# Returns: str: The generated template for the output file name.
# Example:
#    If directory = '/path/to/directory' and file_format = 'mp3', the template would be:
#    '/path/to/directory/[unique_id] [title] [video_id].mp3'
def write_file_outtmpl(directory, file_format):
    unique_id = create_next_unique_id(directory, file_format)
    unique_id = "{" + str(unique_id) + "}"
    title = "{%(title)s}"
    ext = "%(ext)s"
    video_id = "{%(id)s}"

    template = f"{directory}/{unique_id} {title} {video_id}.{ext}"
    
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
    pattern = r'\{(.*?)\}' # Matches text inside square brackets
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
    
# update .download_history.txt file from
# looking through video id of file names
# adding them in .download_history.txt
# renaming every file if unique_id got messed up!
def update_download_history(file_extension, download_directory, download_history_txt_path):
    print_status("Updating Download History")

    if not os.path.isfile(download_history_txt_path):
        # right now, if i delete the download history txt
        # the program will think there's no history because
        # of this condition, i need to do something about this
        # when I get back TODO:
        print_status("No Previous Download History Found!")
    else:
        video_ids = []
        for file_name in os.listdir(download_directory):
            if file_name.endswith(file_extension):
                result = extract_file_info(file_name)
                video_id = result["video_id"]
                video_ids.append(f"youtube {video_id}")

        number_of_download_history = len(open(download_history_txt_path, "r").readlines())
        print_status(f"Total video_ids: {len(video_ids)}, Number Of Download History: {number_of_download_history}", "warning")
        
        if len(video_ids) != number_of_download_history:
            print_status(f"Some {file_extension} files were deleted.", "warning")
            print_status("Or, you modified .download_history.txt.", "warning")

            print_status(f"Updating Unique IDs From {file_extension} files")
            fix_unique_ids(download_directory, file_extension)

            
            with open(download_history_txt_path, "w") as file:
                for video_id in video_ids:
                    file.write(video_id + "\n")
                print_status(f"Updated Download History!", "warning")
        else:
            print_status("Files are Untouched. Nothing Changed in Download Histories!")


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
            print_status(f"ID No. [{current_id}] is not Sorted!", "warning")

            title = result["title"]
            video_id = result["video_id"]
            
            title = "{" + title + "}"
            video_id = "{" + video_id + "}"
            str_expected_id = "{" + str(expected_id) + "}"
            new_file_name = f"{directory}/{str_expected_id} {title} {video_id}.{file_extension}"
            os.rename(os.path.join(directory, file), os.path.join(directory, new_file_name))

        expected_id += 1

# Extract Urls from a YouTube Playlist using yt-dlp
def extract_youtube_playlist_urls(playlist_urls):
    # Configuration opitons for yt-dlp
    extract_options = {
        "dump_single_json": True,
        "extract_flat": True,
        "flat_playlist": True,
        "ignore_errors": True,
    }

    with yt_dlp.YoutubeDL(extract_options) as ydl:
            extracted_urls = []
            try:
                # Extract Playlist Information
                for playlist_url in playlist_urls:
                    result = ydl.extract_info(playlist_url, download=False)
                    
                    # Extract the URLs from the playlist entries
                    extracted_urls_from_playlist = [entry["url"] for entry in result["entries"]]
                    extracted_urls.extend(extracted_urls_from_playlist)
                    

            except yt_dlp.utils.DownloadError:
                raise ValueError("Error: Unable to extract playlist URLs")
            
            return extracted_urls
    
# Searches YouTube for videos based on the provided query and returns a list of video URLs.
#     Args:
#         query (str): The search query to look for on YouTube.
#         max_results (int, optional): The maximum number of results to fetch. Defaults to 5.
#     Returns:
#         list: A list of video URLs matching the search query.
def search_youtube(search_queries, max_results=1):
    extracted_urls = []

    search_options = {
        "quiet": True,
        "extract_flat": True,
        "dump_single_json": True,
        "max_downloads": max_results,
        "match_filter": yt_dlp.utils.match_filter_func("is_video")
    }

    with yt_dlp.YoutubeDL(search_options) as ydl:
        for search_query in search_queries:
            search_results = ydl.extract_info(f"ytsearch{max_results}:{search_query}", download=False)
            videos = search_results.get("entries", [])

            if videos:
                for video in videos:
                    title = video["title"]
                    duration_seconds = format_duration(video["duration"])
                    view_count = format_view_count(int(video["view_count"]))

                    print_status(f"Title: {title} Duration: {duration_seconds} View Count: {view_count}",
                                  color="cyan", delay=0)
                    extracted_urls.append(video["url"])
            else:
                raise ValueError(f"No Videos Found For {search_query}")
    
    return extracted_urls

# Formats the given view count into a more human-readable format.
def format_view_count(view_count):
    if view_count < 1000:
        return str(view_count)  # Return as is if less than 1000

    # Use a list of suffixes to represent large numbers (e.g., 1M for 1 million)
    suffixes = ['', 'K', 'M', 'B', 'T']
    suffix_index = 0

    # Divide the view count by 1000 until it becomes less than 1000
    while view_count >= 1000:
        view_count /= 1000.0
        suffix_index += 1

    # Format the view count with a maximum of two decimal places
    formatted_count = '{:.2f}'.format(view_count)

    # Concatenate the formatted count with the appropriate suffix
    return f'{formatted_count}{suffixes[suffix_index]}'

# Formats the given duration in seconds into a more human-readable format.
def format_duration(duration):
    seconds = int(duration) % 60
    minutes = int(duration / 60) % 60
    hours = int(duration / 3600) % 24
    days = int(duration / 86400)

    formatted_duration = ""
    if days > 0:
        formatted_duration += f"{days}d "
    if hours > 0:
        formatted_duration += f"{hours}h "
    if minutes > 0:
        formatted_duration += f"{minutes}m "
    if seconds > 0:
        formatted_duration += f"{seconds}s"

    return formatted_duration.strip()
