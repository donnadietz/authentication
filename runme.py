#Spring 2018
#HW C1
#Place this file in a folder with one of the .pyc files
#provided for this lesson.
#Run this file. Do what it says.

import os
import re

def findFileNames():
    L=[]
    cp=os.listdir(".")
    p=re.compile('auth[\w]*')
    for i in range(len(cp)):
        names=p.findall(cp[i])
        if not(names in L) and len(names)>0:
            L.append(names)
    return L

L=findFileNames()
for i in range(len(L)):
    try:
        exec("import "+L[i][0]+" as a")
        a.main()
    except:
        pass
