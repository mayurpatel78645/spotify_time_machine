import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


class SpotifyAPI:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.sp = None

    def authenticate_client_credentials_flow(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id,
                                                              client_secret=self.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def authenticate_authorization_code_flow(self):
        sp_oauth = SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret,
                                redirect_uri=self.redirect_uri, scope=self.scope)
        token_info = sp_oauth.get_cached_token()
        if not token_info:
            auth_url = sp_oauth.get_authorize_url()
            print(f"Please visit this URL to authorize access: {auth_url}")
            response = input('Enter the URL you were redirected to: ')
            code = sp_oauth.parse_response_code(response)
            token_info = sp_oauth.get_access_token(code)
        self.sp = spotipy.Spotify(auth=token_info['access_token'])

    def create_playlist(self, user_id, playlist_name, public=False):
        playlist = self.sp.user_playlist_create(user=user_id, name=playlist_name, public=public)
        return playlist['id']

    def search_track(self, track_name, limit=1):
        results = self.sp.search(q=track_name, limit=limit, type='track')
        return results['tracks']['items']

    def add_track_to_playlist(self, playlist_id, track_uri):
        self.sp.playlist_add_items(playlist_id, [track_uri])
        print(f"Track '{track_uri}' added to playlist '{playlist_id}' successfully.")
