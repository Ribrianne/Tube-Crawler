# TubeCrawler - Archived Repository

**Note: This repository has been archived and is no longer actively maintained. Feel free to fork and modify the codebase as needed.**

TubeCrawler is a Python-based media and video content scraper that allows users to download music, podcasts, videos, tutorials, movies, and series from various sources like YouTube. It provides a convenient way to organize and download media content based on user-defined criteria.

## Requirements

### Music Download

- The program accepts a text file containing the titles of the songs to download.
- Users can specify the desired format (e.g., MP3, FLAC) for the downloaded music files.
- The program searches for the provided song titles on YouTube and downloads the corresponding music files.

### Podcast Download

- The program supports downloading podcasts from YouTube or other specified sources.
- Users can specify the source and provide the podcast title or any relevant identifier.
- Downloaded podcast episodes are saved in a suitable format (e.g., MP3) for offline listening.

### Media Type Selection

- The program reads a text file containing a single line with the format "type: <media_type>".
- Users can specify the desired media type (e.g., Music, Podcast, Video, Tutorial, Movie, Series) in the "type" section.
- Based on the specified type, the program executes corresponding functions and downloads the relevant content.

### Subscription

- The program allows users to define a list of YouTube channels to subscribe to.
- Users provide the channel names or identifiers in a text file.
- The program automatically downloads the most recent video uploaded by each subscribed channel.

### Function Modularity

- The program has modular functions for different media types to ensure flexibility and easy maintenance.
- Each media type (e.g., Music, Podcast, Video) has separate functions for searching, downloading, and saving the content.

## Additional Considerations

- The program provides a user-friendly command-line interface for interaction.
- Error handling mechanisms are in place to handle cases like invalid input, network errors, or unavailable content.
- The downloaded media files are organized in a structured manner (e.g., by media type or category) for easy access and management.
- Existing Python libraries or APIs are leveraged for interacting with YouTube or other media sources.

## License

This project is licensed under the MIT License. You are free to modify, distribute, and use the codebase as permitted by the license.

---

For historical reference, the original codebase for TubeCrawler can still be accessed in this archived repository. However, no further updates or maintenance will be provided. Feel free to explore and use the existing codebase to suit your needs.
