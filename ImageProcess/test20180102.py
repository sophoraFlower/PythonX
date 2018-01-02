# coding=utf-8

import os
import sys
from PIL import Image

# IPFile = os.path.dirname(os.path.abspath(__file__))
# im = Image.open(IPFile + '\\test.png')
# print(im.format, im.size, im.mode)
# im.show()

for infile in sys.argv[1:]:
    print(infile)
    f, e = os.path.splitext(infile)
    outfile = f + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('Cannot convert', infile)

