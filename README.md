### README.md

---

# Spotify Time Machine

This Python program allows users to create a Spotify playlist featuring the top 100 songs from a specific date. The program uses web scraping to gather song data and the Spotify API to create and populate the playlist.

### Features

- Authenticate with Spotify using OAuth
- Create a new playlist on Spotify
- Search for songs by name
- Add songs to the created playlist
- Scrape top song data from specified URLs

### Requirements

- Python 3.x
- Spotify Developer Account (Client ID, Client Secret, and Redirect URI)
- `requests` library
- `beautifulsoup4` library
- `spotipy` library
- `python-dotenv` library (for managing environment variables)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/spotify-time-machine.git
   cd spotify-time-machine
   ```

2. **Create a `.env` File**

   In the root directory of your project, create a file named `.env` and add your Spotify credentials and user ID:

   ```plaintext
   SPOTIFY_USER_ID=your_spotify_user_id
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SPOTIFY_REDIRECT_URI=http://example.com
   ```

3. **Install Dependencies**

   Install the required Python libraries:

   ```bash
   pip install requests beautifulsoup4 spotipy python-dotenv
   ```

### Usage

1. **Run the Program**

   Execute the Python script `spotify_time_machine.py`:

   ```bash
   python spotify_time_machine.py
   ```

2. **Enter a Date**

   When prompted, enter a date in the format `YYYY-MM-DD` to create a playlist of the top 100 songs from that time.

   ```plaintext
   Enter a date to create a playlist of top 100 songs of that time (e.g. 2016-07-02):
   ```

3. **Playlist Creation**

   The program will authenticate with Spotify, create a new playlist, scrape song data from predefined URLs, search for each song on Spotify, and add them to the playlist.

### Example

```plaintext
Enter a date to create a playlist of top 100 songs of that time (e.g. 2016-07-02): 2016-07-02
Playlist 'Top Songs from 2016-07-02' created successfully.
Track 'Shape of You' added to playlist 'Top Songs from 2016-07-02' successfully.
...
```
