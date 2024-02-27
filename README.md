# ViMusic-Converter
ViMusic-Converter is a Python script converting ViMusic playlists to playlists in other platforms. (Currently only supports Spotify)

## Installation

```
pip install vimusic-converter
```

## Usage
Backup your ViMusic and copy the `.db` file to the current directory.
```
python main.py <vimusic .db file> <platform> <extra_args>
```
### For Spotify

* **Go to https://developer.spotify.com/dashboard and create an app with a redirect URI (default: https://localhost:8888/callback)**

#### Using .env file for secrets
* **Copy the client ID and execute: where `<client ID>` is replaced by the copied client ID**
```
echo 'SPOTIPY_CLIENT_ID = "<client ID>"' >> .env
```
* **Copy the client secret and execute: where `<client secret>` is replaced by the copied client secret**
```
echo 'SPOTIPY_CLIENT_SECRET = "<client secret>"' >> .env
```
* **Copy the redirect URI and execute: where `<redirect URI>` is replaced by the copied redirect URI**
```
echo 'SPOTIPY_REDIRECT_URI = "<redirect URI>"' >> .env
```
* **Create a Spotify Playlist and copy it's code from the URL (the code is `<code>` in `https://spotify.com/playlist/<code>`). Execute: where `<playlist_code>` is replaced by the copied code**
```
echo 'SPOTIPY_PLAYLIST_URI = "<playlist_code>"' >> .env
```
* **Run program:**
```
python main.py <vimusic .db file> spotify --dotenv
```


#### Using environment variables for secrets
* **Copy the client ID and execute: where `<client ID>` is replaced by the copied client ID**
```
export 'SPOTIPY_CLIENT_ID = "<client ID>"'
```
* **Copy the client secret and execute: where `<client secret>` is replaced by the copied client secret**
```
export 'SPOTIPY_CLIENT_SECRET = "<client secret>"'
```
* **Copy the redirect URI and execute: where `<redirect URI>` is replaced by the copied redirect URI**
```
export 'SPOTIPY_REDIRECT_URI = "<redirect URI>"'
```
* **Create a Spotify Playlist and copy it's code from the URL (the code is `<code>` in `https://spotify.com/playlist/<code>`). Execute: where `<playlist_code>` is replaced by the copied code**
```
export 'SPOTIPY_PLAYLIST_URI = "<playlist_code>"'
```
* **Run program:**
```
python main.py <vimusic .db file> spotify
```
