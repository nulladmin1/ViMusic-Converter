import argparse
from dotenv import load_dotenv
from os import getenv, listdir, path
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
from warnings import warn

load_dotenv()


class ViMusicDBHandler:
    def __init__(self, database_path: str, ):
        self.database_path = database_path
        self.database_conn = sqlite3.connect(database_path)
        self.database_cur = self.database_conn.cursor()

    def get_playlists(self):
        self.database_cur.execute('SELECT * FROM Playlist')
        return self.database_cur.fetchall()

    def get_songs_all(self):
        self.database_cur.execute("SELECT * FROM Song")
        return self.database_cur.fetchall()

    def get_songs_playlist(self, playlist_id: str, ):
        self.database_cur.execute("""SELECT * FROM Song INNER JOIN SongPlaylistMap on Song.id = SongPlaylistMap.songId 
                                  WHERE SongPlaylistMap.playlistId = ?""", (playlist_id,))
        return self.database_cur.fetchall()


class SpotifyConverter:
    def __init__(self, spotipy_creds: dict, verbose=False):
        self.spotipy_instance = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
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


def main():
    vimusic_dbs = [f for f in listdir() if path.isfile(f) and '.db' in f]

    parser = argparse.ArgumentParser(description="Convert ViMusic Playlists to Other Platforms (Currently supports "
                                                 "ViMusic to Spotify)")

    parser.add_argument('database', type=str, choices=vimusic_dbs, help='The ViMusic Database file to read.')
    parser.add_argument('platform', type=str, choices=['spotify'], help="The platform to convert to: ['spotify'].")

    args = parser.parse_args()

    match args.platform:
        case "spotify":
            spotipy_creds = {
                "redirect_uri": getenv('SPOTIPY_REDIRECT_URI'),
                "client_id": getenv('SPOTIPY_CLIENT_ID'),
                "client_secret": getenv('SPOTIPY_CLIENT_SECRET'),
            }

            db_handler = ViMusicDBHandler(args.database)
            playlists = db_handler.get_playlists()
            songs = None
            while True:
                for playlist in playlists:
                    print(f"{playlist[0]}. {playlist[1]}")
                playlist_input = input("Which playlist to select: ")
                try:
                    playlist_r = playlists[int(playlist_input)-1]
                    playlist_id = playlist_r[0]
                    songs = db_handler.get_songs_playlist(playlist_id)
                except ValueError:
                    warn("Not a number; please try again.")
                except IndexError:
                    warn("Not an option; please try again.")
                else:
                    break

            spotify_converter = SpotifyConverter(spotipy_creds)
            spotify_converter.vimusic_to_spotify_playlist(getenv('SPOTIPY_PLAYLIST_URI'), songs)


if __name__ == "__main__":
    main()
