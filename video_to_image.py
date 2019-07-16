import cv2
import os
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('E:\Hashplay\shooting videos') if isfile(join('E:\Hashplay\shooting videos', f))]

file_count = 0
folder_count = 1
image_count = 1
path = "E:/python/dataset/guns/"
os.mkdir(path+"1/")
path = path+"1/"
for each_file in onlyfiles:
    vidcap = cv2.VideoCapture('E:\Hashplay\shooting videos\%s' % (each_file))
    def getFrame(sec):
        global file_count
        global folder_count
        global path
        global image_count
        hasFrames,image = vidcap.read()
        if hasFrames:
            if file_count == 500:
                file_count = 0
                folder_count +=1
                path_make = 'E:/python/dataset/guns/%s' % folder_count+'/'
                os.mkdir(path_make)
                path = path_make
            cv2.imwrite(path+"image_"+str(image_count)+"_"+str(folder_count)+".jpg", image)
            file_count +=1
            image_count +=1
        return hasFrames
    sec = 0
    frameRate = 0.5 #//it will capture image in each 0.5 second
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)