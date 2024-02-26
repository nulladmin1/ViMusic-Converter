# ViMusic-Converter
ViMusic-Converter is a Python script converting ViMusic playlists to playlists in other platforms. (Currently only supports Spotify)

## Installation

* **`Clone` and `cd` into directory**
```
git clone https://github.com/nulladmin1/ViMusic-Converter.git
cd ViMusic-Converter/
```
* **Create `virtualenv` environment**
```
python -m virtualenv venv
```
* **Activate `virtualenv` environment**
  * **Windows:** `./venv/bin/activate`
  * **Mac/Linux:** `source venv/bin/activate`
* **Install required modules**
```
pip -r requirements.txt
```
## Usage
Backup your ViMusic and copy the `.db` file to the current directory, and run:
```
python main.py <ViMusic .db file> <platform> <extra_args>
```
### For Spotify

* **Go to https://developer.spotify.com/dashboard and create an app with a redirect URI (default: https://localhost:8888/callback)**
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
python main.py <ViMusic .db file> spotify
```
