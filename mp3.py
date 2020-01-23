#Stigmatas and AFThunder, 2019

from mutagen.easyid3 import EasyID3
import mutagen
import os

print("input directory for processing: ")
path = input()
os.chdir(path)

file_list = filter((lambda x: '.mp3' in x), os.listdir(path))

for i in file_list:
    print("file: "+i)
    try:
        current = EasyID3(i)
        newname = current["artist"][0] + ".mp3"
        newname.replace(" ", "_")
        del current
        print("renaming "+i+" to "+newname)
        os.rename(i, newname)
    except:
        print("...that file didn't work for some reason.")
