# Arknights SD Viewer (Sparen Fork)

This is SparenofIría's fork of the Arknights SD Viewer repo. The main purpose of this fork is to provide animations for projects such as ArknightsDNH. There is no expectation of parity with the original repository. Parity additions will remain on the main gh-pages branch while all other changes will go in the sparen-dev branch.

Original Repo: https://github.com/alg-wiki/Arknights-SD-Viewer

Original Live Website: https://arknights.nuke.moe

## Getting New Assets
Latest Arknights CN APK: https://ak.hypergryph.com/downloads/android_lastest

1. Download CN APK (NA/JP APK will not work since they do not have assets in the APK); rename .apk to .zip
2. Navigate to `assets/AB/Android/charpack` for chibi sprites
3. Asset Studio GUI - Load it, export it
4. Run sort.py inside a directory called `charpack` with the Texture2D and TextAsset outputs from Asset Studio

## Python Scripts
The original repository contains three top level python scripts - alpha.py, enemy.py, and sort.py. These were not documented in the original repository. This section documents their usage.

### alpha.py

TODO

### enemy.py

TODO

### sort.py
This script is used on the raw Asset Studio exports to process all sprite assets and neatly organize them, as well as create the charData file.

### scraper.py
This script was written in order to scrape the existing character data files from https://media.nuke.moe so that everything could be referenced locally. 

It is run as follows:

`python3 scraper.py operatorinternalname targetchar enemyflag<Y/N> nodormflag<Y/N> nobackflag<Y/N> `

`operatorinternalname` is the internal name of the operator, and is the first level key in charData for the character. It is used solely to group skins for an operator together. `targetchar` is the skin name for the character. `enemyflag` should be set to 'Y' iff the script is being run for an enemy rather than an operator. `nodormflag` should be set to 'Y' if there is no dorm animation (e.g. Weedy's cannon), and `nobackflag` should be set to 'Y' if there is no dorm or back flag (e.g. W's mines). All flags are optional, but the names are required in order for the script to work at all.

## Notes
- Commit Messages are used in the Changelog feature, which hooks into GitHub directly. Commit Messages should therefore be up to standard.
