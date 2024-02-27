import argparse
import sqlite3
from os import getenv, listdir, path
from dotenv import dotenv_values
from warnings import warn

from .dbhandler import ViMusicDBHandler


def main():

    vimusic_dbs = [f for f in listdir() if path.isfile(f) and '.db' in f]

    parser = argparse.ArgumentParser(description="Convert ViMusic Playlists to Other Platforms (Currently supports "
                                                 "ViMusic to Spotify)")

    parser.add_argument('database', type=str, choices=vimusic_dbs, help='The ViMusic Database file to read.')
    parser.add_argument('platform', type=str, choices=['spotify'], help="The platform to convert to: ['spotify'].")
    parser.add_argument('--dotenv', action='store_true', help='ENV FILE')

    args = parser.parse_args()

    match args.platform:
        case "spotify":
            from .spotify import SpotifyConverter

            if args.dotenv:
                secrets = dotenv_values('.env')
                spotipy_creds = {
                    "redirect_uri": secrets['SPOTIPY_REDIRECT_URI'],
                    "client_id": secrets['SPOTIPY_CLIENT_ID'],
                    "client_secret": secrets['SPOTIPY_CLIENT_SECRET'],
                }
            else:
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
