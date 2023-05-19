TubeCrawler is a Python-based media and video content scraper that allows users to download music, podcasts, videos, tutorials, movies, and series from various sources like YouTube. It provides a convenient way to organize and download media content based on user-defined criteria.

### Requirements:

1. **Music Download:**
   - The program should accept a text file containing the titles of the songs to download.
   - Users should be able to specify the desired format (e.g., MP3, FLAC) for the downloaded music files.
   - The program should search for the provided song titles on YouTube and download the corresponding music files.

2. **Podcast Download:**
   - The program should support downloading podcasts from YouTube or other specified sources.
   - Users should be able to specify the source and provide the podcast title or any relevant identifier.
   - Downloaded podcast episodes should be saved in a suitable format (e.g., MP3) for offline listening.

3. **Media Type Selection:**
   - The program should read a text file containing a single line with the format "type: <media_type>".
   - Users can specify the desired media type (e.g., Music, Podcast, Video, Tutorial, Movie, Series) in the "type" section.
   - Based on the specified type, the program should execute corresponding functions and download the relevant content.

4. **Subscription:**
   - The program should allow users to define a list of YouTube channels to subscribe to.
   - Users should provide the channel names or identifiers in a text file.
   - The program should automatically download the most recent video uploaded by each subscribed channel.

5. **Function Modularity:**
   - The program should have modular functions for different media types to ensure flexibility and easy maintenance.
   - Each media type (e.g., Music, Podcast, Video) should have separate functions for searching, downloading, and saving the content.

### Additional Considerations:

- The program should provide a user-friendly command-line interface for interaction.
- Error handling mechanisms should be in place to handle cases like invalid input, network errors, or unavailable content.
- The downloaded media files should be organized in a structured manner (e.g., by media type or category) for easy access and management.
- It is recommended to leverage existing Python libraries or APIs for interacting with YouTube or other media sources.