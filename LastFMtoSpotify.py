import requests
import xml.etree.ElementTree as ET
import json
import sys, os

from optparse import OptionParser

def searchLastFM(user, api_key, tracks, currPage):
	payload = {
		"user": user,
		"api_key": api_key,
		"limit": 50, # 50 elem on each page
		"method": "user.getrecenttracks",
		"page": currPage
	}

	lastFM = "http://ws.audioscrobbler.com/2.0/"

	r = requests.get(lastFM, params=payload)
	#print(r.text)

	root = ET.fromstring(r.text)

	if currPage == 1:
		recentrack = list(root.iter("recenttracks"))[0]
		totalPages = recentrack.attrib["totalPages"]
		print("LastFM profile " + user + " has " + totalPages + " pages in total.")
	print("Reading LastFM page:", currPage)
	for track in root.iter("track"):
		artist = track[0].text
		name = track[1].text

		if not (artist, name) in tracks: # Do not accept duplicates
			tracks.append((artist, name))

def spotifySearchAndGo(tracks):
	spotify = "https://api.spotify.com/v1/search"
	spotifyIDList = []

	for track in tracks:
		artist = track[0]
		name = track[1]

		payload = {
		  "q": name + " artist:" + artist,
		  "type": "track",
		  "limit": 1
		}

		headers = {"Accept": "application/json"}

		r = requests.get(spotify, params=payload, headers=headers)
		#print(r.url)

		data = json.loads(r.text)
		try:
			spotifyIDList.append(data["tracks"]["items"][0]["id"])
		except IndexError:
			print(artist + " - " + name + " wasn't found by spotify.")

	finalString = "spotify:trackset:Playlist:" + ",".join(spotifyIDList)
	print(finalString)
	os.system("xdg-open " + finalString)

def parserOptions():
	parser.add_option("-u", "--user", dest="username", default=None,
		help="Username of the user to import recently listened tracks.")
	parser.add_option("-a", "--api-key", dest="api_key", default=None,
		help="LastFM API key that will be used to fetch data from LastFM.")
	parser.add_option("-p", "--pages", dest="numPages", default=1,
		help="Maximum number of pages to fetch.")

	options, args = parser.parse_args()

	if not options.username:
		sys.exit("Username has to be defined, see --help")
	if not options.api_key:
		sys.exit("LastFM API key has to be defined, seek --help")

	return options.username, options.api_key, options.numPages

if __name__ == "__main__":
	tracks = []
	parser = OptionParser()
	username, api_key, numPages = parserOptions()

	for i in range(1, numPages + 1):
		searchLastFM(username, api_key, tracks, i)

	spotifySearchAndGo(tracks)

