from dotenv import load_dotenv
from os import getenv, listdir, path
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sqlite3
from warnings import warn

load_dotenv()


def get_list(data: list, list_type: str) -> str:
    if len(data) < 1:
        if list_type == "db":
            raise FileNotFoundError(".db file not found.")
        else:
            raise sqlite3.OperationalError("Playlist not found. ")
    elif len(data) > 1:
        while True:
            print(f"Which {list_type} to select? ")
            for k, v in enumerate(data):
                if list_type == "db":
                    print(f"{k + 1}. {v}")
                else:
                    print(f"{k + 1}. {v[1]}")
            x = input(f"Which {list_type} to select? ")
            try:
                return data[(int(x) - 1)]
            except ValueError:
                warn("Not a number; please try again.")
            except IndexError:
                warn("Not an option; please try again")
    else:
        return data[0]


def get_songs():
    cur.execute("SELECT * FROM Playlist")
    playlists = cur.fetchall()

    playlist = get_list(playlists, "playlist")

    # cur.execute("SELECT * FROM SongPlaylistMap WHERE playlistid = ?", (playlist[0],))
    cur.execute("SELECT * FROM Song INNER JOIN SongPlaylistMap ON Song.id = SongPlaylistMap.songId WHERE "
                "SongPlaylistMap.playlistid = ?", (playlist[0],))
    return playlist, cur.fetchall()


vimusic_dbs = [f for f in listdir() if path.isfile(f) and '.db' in f]
db = get_list(vimusic_dbs, "db")

conn = sqlite3.connect(db)
cur = conn.cursor()

songs = get_songs()

song_names = [x[1] for x in songs[1]]
pl = songs[0][1]

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public",
        redirect_uri=getenv('SPOTIPY_REDIRECT_URI'),
        client_id=getenv('SPOTIPY_CLIENT_ID'),
        client_secret=getenv('SPOTIPY_CLIENT_SECRET'),
    )
)

pl_uri = input(
    'Go to Spotify, create a new playlist, and copy & paste playlist playlist URL Code here (the code is the part of '
    'the playlist url that comes after "/playlist/":')
songs_uri = []
for s in song_names:
    results = sp.search(q=f'track:{s}', type='track', limit=1)
    for track in results['tracks']['items']:
        print(f"Adding \033[1;96m'{track['name']}'\033[0m to playlist \033[1;96m'{pl}'\033[0m...")
        songs_uri.append(track['uri'])
print(songs_uri)
sp.playlist_add_items(playlist_id=pl_uri, items=songs_uri)
