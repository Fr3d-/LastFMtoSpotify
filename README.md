LastFMtoSpotify
====

Import a Last.fm users recently played songs into spotify.

Installation
---------
**Ubuntu**

    sudo apt-get install python3.4
    sudo apt-get install python3-requests
    wget https://github.com/Fr3d-/LastFMtoSpotify/raw/master/LastFMtoSpotify.py
    sudo chmod +x LastFMtoSpotify.py
    sudo mv LastFMtoSpotify.py /usr/bin/
    
Syntax
---------
    Usage: LastFMtoSpotify.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -u USERNAME, --user=USERNAME
                            Username of the user to import recently listened
                            tracks.
      -a API_KEY, --api-key=API_KEY
                            LastFM API key that will be used to fetch data from
                            LastFM.
      -p NUMPAGES, --pages=NUMPAGES
                            Maximum number of pages to fetch.

**Example**

    LastFMtoSpotify.py -u example -a xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Requirements
---------
* Python 3.4
* Requests 2.2.1