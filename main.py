import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

client_id = "753950aa9d774c55bc0394bdfa71f77d"
client_secret = "a7324f74b2dc4cb39dbaa3cf2d0d34d4"

# Scopes required for playlist modification
scope = 'playlist-modify-public playlist-modify-private'

# Authenticate with Spotify using Client Credentials flow
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

redirect_uri = 'http://example.com'  # Set this in your Spotify Developer Dashboard

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

token_info = sp_oauth.get_cached_token()

if not token_info:
    auth_url = sp_oauth.get_authorize_url()
    print(f"Please visit this URL to authorize access: {auth_url}")
    response = input('Enter the URL you were redirected to: ')
    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_cached_token()

sp = spotipy.Spotify(auth=token_info['access_token'])

# Example: Create a new playlist
playlist_name = 'My Test Playlist'
user_id = 'mayurpatel78645'  # Replace with your Spotify user ID

# Create the playlist
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist['id']

# Example: Search for a track by name
track_name = 'Shape of You'  # Example track name
results = sp.search(q=track_name, limit=1, type='track')

# Add the first track found to the new playlist
if results['tracks']['items']:
    track_uri = results['tracks']['items'][0]['uri']
    sp.playlist_add_items(playlist_id, [track_uri])
    print(f"Track '{track_name}' added to playlist '{playlist_name}' successfully.")
else:
    print(f"No track found with name '{track_name}'")

bollywood_url = "https://www.bbc.co.uk/asiannetwork/vote/top-songs/"
hollywood_url = "https://www.billboard.com/charts/hot-100/2016-07-02/"
urls = [bollywood_url, hollywood_url]


def scrape(url):
    request = requests.get(url)
    response = request.text
    soup = BeautifulSoup(response, "html.parser")
    if "billboard" in url:
        titles = [song.getText().strip() for song in soup.select("h3") if ":" not in song.getText()][3:103]
    else:
        titles = [song.getText() for song in soup.select(".intro") if "-" in song.getText()][1:]
    return titles


def create_txt_file(file_name, url):
    bollywood_titles = scrape(url)
    with open(f"{file_name}.txt", "w") as file:
        for title in bollywood_titles:
            file.write(f"{title}\n")


# for url in urls:
#     create_txt_file("hollywood" if "billboard" in url else "bollywood", url)
