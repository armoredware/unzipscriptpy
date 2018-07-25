import os
import rando
import subprocess

path="/root/Desktop/zip/arc"
os.chdir(path)
#rand = random.random()
count = 0
x = 2

while(x != 0):
	for files in next(os.walk(path))[2]:
               try:
		    if files.endswith(".zip") or files.endswith(".gz") or files.endswith(".tar"):
			count = count + 1
                        p = subprocess.Popen(["atools", files], stdout=subprocess.PIPE)
                        print p.communicate()
                        print archive
                        print count
                        os.chdir(path+"/flag")
		    else:
			pass
	       except:
		    pass


