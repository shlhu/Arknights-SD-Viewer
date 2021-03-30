# scaper.py
# The base repository uses https://media.nuke.moe/arknights/ to store all of the character portraits, skeletons, atlases, and images
# This Python script scrapes all of them.
# Note that caracters have front, back, and base variants
# Usage: python3 scraper.py targetchar enemyflag<Y/N> nodormflag<Y/N> nobackflag<Y/N> 
# e.g. python3 scraper.py amiya char_002_amiya

import urllib.request
import shutil
import os
import sys

ORIGSOURCE = "https://media.nuke.moe/arknights/"

charname = sys.argv[1]

options = ["front", "back", "base"]
if (len(sys.argv) > 2 and sys.argv[2]) == "Y": # Switch to enemy mode
	options = ["enemy"]
elif (len(sys.argv) > 3 and sys.argv[3] == "Y"): # No Dorm option
	if (len(sys.argv) > 4 and sys.argv[4] == "Y"): # No Back or Dorm option
		options = ["front"]
	options = ["front", "back"]
elif (len(sys.argv) > 4 and sys.argv[4] == "Y"): # No Back option
	if (len(sys.argv) > 3 and sys.argv[3] == "Y"): # No Back or Dorm option
		options = ["front"]
	options = ["front", "base"]

filetypes = ["skel", "atlas", "png"]

for option in options:
	buildflag = ""
	if option == "base":
		buildflag = "build_" # Base assets are prefixed with build_
	for ft in filetypes:
		remoteURL = ORIGSOURCE + "sd/" + option + "/" + buildflag + charname + "." + ft
		localPath = "./assets/sd/" + option + "/" + buildflag + charname + "." + ft
		os.makedirs(os.path.dirname(localPath), exist_ok=True) # Generate the local path if it does not yet exist
		print(remoteURL)
		req = urllib.request.Request(remoteURL, headers={'User-Agent': 'Mozilla/5.0'}) # Pretend we're a legitimate browser to bypass HTTPS
		with urllib.request.urlopen(req) as response, open(localPath, 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
