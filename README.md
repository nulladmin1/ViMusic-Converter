# ViMusic-Converter
ViMusic-Converter is a Python script converting ViMusic playlists to Spotify Playlists.

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

* **Go to https://developer.spotify.com/dashboard and create an app with a redirect URI (default: https://localhost:8888/callback)**
* **Copy the client ID and execute: where `<client ID>` is replaced by the copied client ID**
```
echo 'SPOTIPY_CLIENT_ID = "<client ID>"
```
* **Copy the client secret and execute: where `<client secret>` is replaced by the copied client secret**
```
echo 'SPOTIPY_CLIENT_SECRET = "<client secret>"
```
* **Copy the redirect URI and execute: where `<redirect URI>` is replaced by the copied redirect URI**
```
echo 'SPOTIPY_REDIRECT_URI = "<redirect URI>"
```
* **Backup your ViMusic and copy the `.db` file to the current directory**
* **Create a Spotify Playlist and copy it's code from the URL (the code is `<code>` in `https://spotify.com/playlist/<code>`). Keep the code ready for later use.**
* **Run the program and follow the directed steps. When it says to paste the playlist URL, paste the code that was copied earlier**
* ```
  python main.py
  ```
