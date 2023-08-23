# coding:utf-8
import os
from PIL import Image


path = r'/home/whn/ly/AROD-RS/data/UCAS-AOD/VOC2007/JPEGImages/'
for file in os.listdir(path):
    if file.endswith('.png'):
        filename = os.path.join(path, file)
        new_name = path +'/' + file[:-4] + '.jpg'
        img = Image.open(filename)
        img = img.convert('RGB') # OSError: cannot write mode RGBA as JPEG 时用
        img.save(new_name)
        #del img
        #os.remove(filename)
        pass

