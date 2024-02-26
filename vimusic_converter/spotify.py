import spotipy


class SpotifyConverter:
    def __init__(self, spotipy_creds: dict, verbose=False):
        self.spotipy_instance = spotipy.Spotify(
            auth_manager=spotipy.oauth2.SpotifyOAuth(
                scope="playlist-modify-private playlist-modify-public",
                redirect_uri=spotipy_creds['redirect_uri'],
                client_id=spotipy_creds['client_id'],
                client_secret=spotipy_creds['client_secret'],
            )
        )
        self.verbose = verbose

    def vimusic_to_spotify_playlist(self, playlist_uri: str, songs: list):
        songs_uri = []
        song_names = [s[1] for s in songs]
        for song in song_names:
            result = self.spotipy_instance.search(q=f"track:{song}", type="track", limit=1)
            for result_track in result['tracks']['items']:
                songs_uri.append(result_track['uri'])
        print(songs_uri)
        self.spotipy_instance.playlist_add_items(playlist_id=playlist_uri, items=songs_uri)
