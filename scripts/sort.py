import os
import re
import math
import shutil

from PIL import Image
from shutil import copyfile

def clean(file):
	"""
	Return file name with suffixes removed
	"""
	file = re.sub("\s","",file)
	file = re.sub("#\d*","",file)
	file = re.sub("\.txt","",file)
	file = re.sub("\.prefab","",file)
	return file

def organize_assets(source_path, target_path):
	path = source_path
	base = os.path.join(target_path, "base")
	front = os.path.join(target_path, "front")
	back = os.path.join(target_path, "back")
	os.makedirs(base, exist_ok=True)
	os.makedirs(front, exist_ok=True)
	os.makedirs(back, exist_ok=True)
	
	text_asset_path = os.path.join(path, "TextAsset")
	texture_path = os.path.join(path, "Texture2D")


	for file in os.listdir(path):
		id = file[:-3]
		if (re.match("char_\d\d\d_.*", id)):
			for imgfile in os.listdir(texture_path):
				if (re.match(".*"+id+".*", imgfile)):
					#base
					if (imgfile[:5] == "build"):
						copyfile(os.path.join(texture_path, imgfile), os.path.join(base, clean(imgfile)))
			for file2 in os.listdir(text_asset_path):
				if (re.match(".*"+id+".*", file2)):
					if (file2[:5] == "build"):
						copyfile(os.path.join(text_asset_path, file2), os.path.join(base, clean(file2)))

	list1 = []
	list2 = []

	for file in os.listdir(path):
		id = file[:-3]
		if (re.match("char_\d\d\d_.*", id)):
			for imgfile in os.listdir(texture_path):
				x = re.findall("^("+id+")\s?#?[0-9]*\.png$", imgfile)
				if (len(x) != 0):
					if (x[0] not in list1):
						list1.append(x[0])
						print(imgfile)
				x = re.findall("^("+id+"_[a-zA-Z]+[0-9]*)\s?#?[0-9]*\s?#?[0-9]*\.png$", imgfile)
				if (len(x) != 0):
					if (x[0] not in list1):
						list1.append(x[0])
						print(imgfile)
				x = re.findall("^("+id+"\[alpha\])\s?#?[0-9]*\.png$", imgfile)
				if (len(x) != 0):
					if (x[0] not in list1):
						list1.append(x[0])
						print(imgfile)
				x = re.findall("^("+id+"_[a-zA-Z]+[0-9]*)[0-9#\s]*\[alpha\][0-9#\s]*\.png$", imgfile)
				if (len(x) != 0):
					if ((x[0]+"[alpha]") not in list1):
						list1.append(x[0]+"[alpha]")
						print(imgfile)


	print(list1)

	for id in list1:
		print(id)
		count = 0
		for imgfile in os.listdir(texture_path):
			if (re.match(re.escape(id)+"[0-9#\s]*\.png", clean(imgfile))):
				im = Image.open(os.path.join(texture_path, imgfile))
				h,w = im.size
				if (h < 1024):
					list2.append(imgfile)
					count = count + 1
		if (count == 2):
			size1 = os.stat(os.path.join(texture_path, list2[0])).st_size
			size2 = os.stat(os.path.join(texture_path, list2[1])).st_size
			if (size1 > size2):
				copyfile(os.path.join(texture_path, list2[0]), os.path.join(front, clean(list2[0])))
				copyfile(os.path.join(texture_path, list2[1]), os.path.join(back, clean(list2[1])))
			else:
				copyfile(os.path.join(texture_path, list2[1]), os.path.join(front, clean(list2[1])))
				copyfile(os.path.join(texture_path, list2[0]), os.path.join(back, clean(list2[0])))
			list2 = []
			count = 0

		list2 = []
		count = 0
		for binfile in os.listdir(text_asset_path):
			if (re.match(re.escape(id)+"[0-9#\s]*\.skel", clean(binfile))):
				list2.append(binfile)
				count = count + 1
		if (count == 2):
			size1 = os.stat(os.path.join(text_asset_path, list2[0])).st_size
			size2 = os.stat(os.path.join(text_asset_path, list2[1])).st_size
			if (size1 > size2):
				copyfile(os.path.join(text_asset_path, list2[0]), os.path.join(front, clean(list2[0])))
				copyfile(os.path.join(text_asset_path, list2[1]), os.path.join(back, clean(list2[1])))
			else:
				copyfile(os.path.join(text_asset_path, list2[1]), os.path.join(front, clean(list2[1])))
				copyfile(os.path.join(text_asset_path, list2[0]), os.path.join(back, clean(list2[0])))
			list2 = []
			count = 0

		list2 = []
		count = 0
		for binfile in os.listdir(text_asset_path):
			if (re.match(re.escape(id)+"[0-9#\s]*\.atlas", clean(binfile))):
				list2.append(binfile)
				count = count + 1
		if (count == 2):
			size1 = os.stat(os.path.join(text_asset_path, list2[0])).st_size
			size2 = os.stat(os.path.join(text_asset_path, list2[1])).st_size
			if (size1 > size2):
				copyfile(os.path.join(text_asset_path, list2[0]), os.path.join(front, clean(list2[0])))
				copyfile(os.path.join(text_asset_path, list2[1]), os.path.join(back, clean(list2[1])))
			else:
				copyfile(os.path.join(text_asset_path, list2[1]), os.path.join(front, clean(list2[1])))
				copyfile(os.path.join(text_asset_path, list2[0]), os.path.join(back, clean(list2[0])))
			list2 = []
			count = 0
		list2 = []
		count = 0

	filestring = "var charData = {\n"

	for file in os.listdir(path):
		id = file[:-3]
		if (re.match("char_\d\d\d_.*", id)):
			filestring += '\t"'+re.sub("char_\d\d\d_","",id)+'" : {\n'
			filestring += '\t\t"name" : "'+re.sub("char_\d\d\d_","",id)+'",\n'
			filestring += '\t\t"type" : "",\n'
			filestring += '\t\t"group" : "",\n'
			filestring += '\t\t"rarity" : "",\n'		
			filestring += '\t\t"skin" : ['
			for x in list1:
				if (re.match(re.escape(id) + ".*", x)):
					if (x[-7:] != "[alpha]"):
						filestring += '"' + x + '",'
			filestring += ']\n\t},\n'

	filestring += "};"
	print(filestring)
	text_file = open(os.path.join(target_path, "charData.js"), "w")
	text_file.write(filestring)
	text_file.close()

def main():
	source_path = (r"C:\Users\shlhu\Downloads\arknights-hg-1921\assets\AB\Android\charpack")
	target_path = os.path.join(".", "new_data")
	organize_assets(source_path, target_path)

if __name__ == "__main__":
    main()