# texmapalpha.py
# Given an image and its mask, applies the mask and outputs to "processed.png"
# Usage: python3 texmapalpha.py path1 path2

import os
import re
import math
import shutil
import sys

from PIL import Image

base = Image.open(sys.argv[1])
mask = Image.open(sys.argv[2])
mask = mask.convert("L")
base.putalpha(mask)
base.save("processed.png")

