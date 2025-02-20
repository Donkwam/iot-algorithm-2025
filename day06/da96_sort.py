import os

# 폴더의 하위 폴더의 개수 추출
fnameAry = []
folderName = 'C:/Windows/System32'
for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

print(len(fnameAry))