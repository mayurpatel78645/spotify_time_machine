from scraper import WebScraper
from spotify_api import SpotifyAPI
from dotenv import load_dotenv
import os
from datetime import datetime


class SpotifyPlaylistCreator:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.spotify_api = SpotifyAPI(client_id, client_secret, redirect_uri, scope)
        self.web_scraper = WebScraper()

    def create_playlist_from_url(self, user_id, playlist_name, url):
        # Authenticate Spotify API
        self.spotify_api.authenticate_authorization_code_flow()

        # Create playlist
        playlist_id = self.spotify_api.create_playlist(user_id, playlist_name, public=False)

        # Scrape titles from URL and add tracks to playlist
        titles = self.web_scraper.scrape(url)
        for title in titles:
            # Search for track
            track_results = self.spotify_api.search_track(title)
            if track_results:
                track_uri = track_results[0]['uri']
                # Add track to playlist
                self.spotify_api.add_track_to_playlist(playlist_id, track_uri)
            else:
                print(f"No track found for '{title}'")


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    spotify_user_id = os.getenv("SPOTIFY_USER_ID")
    spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
    spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
    scope = 'playlist-modify-public playlist-modify-private'

    spotify_playlist_creator = SpotifyPlaylistCreator(spotify_client_id, spotify_client_secret, spotify_redirect_uri,
                                                      scope)

    user_id = spotify_user_id

    get_date = input("Enter a date to create a playlist of top 100 songs of that time (e.g. 2016-07-02): ")


    def is_valid_date(date_string):
        try:
            # Attempt to parse the date string
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False


    while True:
        date_input = input("Enter a date to create a playlist of top 100 songs of that time (e.g. 2016-07-02): ")
        if is_valid_date(date_input):
            break
        else:
            print(f"The date '{date_input}' is not in the correct format (YYYY-MM-DD). Please enter a valid date.")

    playlist_name = f"{date_input} Billboard 100"
    # bollywood_url = "https://www.bbc.co.uk/asiannetwork/vote/top-songs/"
    hollywood_url = f"https://www.billboard.com/charts/hot-100/{date_input}/"
    # Create playlist from Bollywood and Hollywood URLs
    # spotify_playlist_creator.create_playlist_from_url(user_id, "Bollywood 100", bollywood_url)
    spotify_playlist_creator.create_playlist_from_url(user_id, playlist_name, hollywood_url)

