#!/usr/bin/python
from PIL import Image
import os, sys

path = os.getcwd()
dirs = os.listdir( path )
for  item in dirs:
    file,ext=os.path.splitext(item)
    if(ext==".jpg"):
        image=Image.open(item)
        image.resize((200,200),Image.NEAREST)
        image.save(file+"_resize.jpg")



"""
dılo sürücü <berxudar@gmail.com>
termianlden resimlerin bulunduğu klasörde python3 resize.py vermen yeterlidir

"""
