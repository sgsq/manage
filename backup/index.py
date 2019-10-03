import requests 
import os
import time
def dld(u,n):
    with open(n,"wb") as f:
        f.write(requests.get(u).content)
tb=time.time()
print("Backup")
print(" ")
print("source:SGSQ")
print("sgsq.github.io")
print(" ")
print("Fetching list")
url="https://sgsq.github.io/sources.list"
r=requests.get(url)
a=r.text.split("\n")
# a=['https://codeload.github.com/sgsq/tool/zip/master', 'https://codeload.github.com/sgsq/train/zip/master', 'https://codeload.github.com/sgsq/sgsq.github.io/zip/master']
print("Files to download: ",len(a))
cnt=0
for aa in a:
    cnt=cnt+1
    print("Downloading file ",cnt)
    na=aa.split("/")[-3]+".zip"
    print(aa,na)
    dld(aa,na)
    print("Completed file ",cnt)
    print(" ")
tu=time.time()-tb
print("Backup completed in ",tu)
os.system("pause")
