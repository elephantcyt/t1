import os

dirlist=os.listdir(".")

fileL=open("namelist.txt","a")
for fname in dirlist:
    print("%s" % fname)
    fileL.write("%s\n" % fname)


fileL.close()    
                
