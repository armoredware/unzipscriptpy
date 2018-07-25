from pyunpack import Archive
import os
import random


path="/root/Desktop/zip/arc"
os.chdir(path)
#rand = random.random()
count = 0
x = 2

while(x != 0):
	for files in next(os.walk(path))[2]:
               try:
		    if files.endswith(".zip") or files.endswith(".gz") or files.endswith(".tar"):
			#arr.append(path + "/" + files)
			count = count + 1
                        print files, count
                        if files.endswith(".zip"):
                            packed = files+str(count)+".zip"
			    os.rename(files,packed)
                        if files.endswith(".gz"):
                            packed = files+str(count)+".gz"
			    os.rename(files,packed)
                        if files.endswith(".tar"):
                            packed = files+str(count)+".tar"
			    os.rename(files,packed)
			#unpack
			Archive(packed).extractall('/root/Desktop/zip/arc')
                        print packed
                        os.rename(packed,packed+".txt")
                        packed = ""
                        files = ""
                        break
			#renames container
			#os.remove(packed)
		    else:
			pass
	       except:
		    pass


