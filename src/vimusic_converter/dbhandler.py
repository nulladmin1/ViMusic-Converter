import sqlite3


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
