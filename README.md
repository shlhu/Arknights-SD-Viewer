# Arknights SD Viewer (Sparen Fork)

This is SparenofIría's fork of the Arknights SD Viewer repo. The main purpose of this fork is to provide animations for projects such as ArknightsDNH. There is no expectation of parity with the original repository. Parity additions will remain on the main gh-pages branch while all other changes will go in the sparen-dev branch.

Original Repo: https://github.com/alg-wiki/Arknights-SD-Viewer

Original Live Website: https://arknights.nuke.moe

## Getting New Assets
Latest Arknights CN APK: https://ak.hypergryph.com/downloads/android_lastest

1. Download CN APK (NA/JP APK will not work since they do not have assets in the APK); rename .apk to .zip
2. Navigate to `assets/AB/Android/charpack` for chibi sprites
3. Asset Studio GUI - Load it, export it in the same directory as the .ab files. Export Options should have grouping done by `type name` to be compatible with the Python scripts used for processing.
4. Run sort.py inside a directory called `charpack` with the Texture2D and TextAsset outputs from Asset Studio

Caveats:

- CN APK still does not include skins
- sort.py should only ever be run on the full dataset once, since pretty much all the data in the JSON (e.g. class, rarity) needs to be repopulated from scratch. For adding new characters once the existing portion is established, you can still run sort.py, but it is best to add newly added characters to the top of charData.js or enemyData.js manually.

Portraits:

- Portraits are located at `assets/AB/Android/spritepack` at ui_char_avatar_h1_0.ab, ui_char_avatar_h1_elite_0.ab, and ui_char_avatar_h1_skins_0.ab. These require masks to be applied manually. Note that portraits are 180x180, but the masks and atlases ARE NOT 180x180 for whatever reason. This means that you can either pair the atlas and mask and then crop out the portrait you want by analyzing which edge pixels have been repeated while cross referencing the raw portrait data, or you can crop out the mask after cross referencing and then apply it. The former is less mentally taxing and is therefore recommended.

## SOP - Adding a new Character
- Process the charpack chibi sprite and add the front, back, and base png, skel, and atlas files
- Given the name of the character, add them with their information manually into charData.js
- Process the portraits and add their E1 and E2 portraits (or skin, if applicable)
- Perform the same for their summons, if any

## Python Scripts
The original repository contains three top level python scripts - alpha.py, enemy.py, and sort.py. These were not documented in the original repository. This section documents their usage.

For processing character data, sort.py is used, while for enemy data, enemy.py is used. Regardless, image data needs to go through alpha.py (to apply masks).

### alpha.py
This script applies alpha masks onto the output of sort.py, generating transparent images.

### enemy.py
This script is used on the raw Asset Studio ENEMY exports to neatly organize them, as well as create the enemyData file.

### sort.py
This script is used on the raw Asset Studio CHARACTER exports to process all sprite assets and neatly organize them, as well as create the charData file. The original script assumes the following:

- Extraction was done in-place with the extracted Texture2D and TextAsset directories in the *same directory as the .ab* originals. The filename of the .ab files, excluding the .ab portions cut off using `[:-3]`, are the IDs used for filepaths everywhere else in the system. 

The new script assumes the following, in addition:

- front, back, and base directories have been prepared
- You have a way to remove the .prefab extension from all skel and atlas files

### scraper.py
This script was written in order to scrape the existing character data files from https://media.nuke.moe so that everything could be referenced locally. 

It is run as follows:

`python3 scraper.py targetchar enemyflag<Y/N> nodormflag<Y/N> nobackflag<Y/N> `

`targetchar` is the skin name for the character. `enemyflag` should be set to 'Y' iff the script is being run for an enemy rather than an operator. `nodormflag` should be set to 'Y' if there is no dorm animation (e.g. Weedy's cannon), and `nobackflag` should be set to 'Y' if there is no dorm or back flag (e.g. W's mines). All flags are optional, but the names are required in order for the script to work at all.

### texmapalpha.py
This script applies a mask onto an image. It is primarily used for portrait extraction

## Notes
- Commit Messages are used in the Changelog feature, which hooks into GitHub directly. Commit Messages should therefore be up to standard.
