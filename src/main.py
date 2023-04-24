import glob
import os
import sortFilesByEvent
import fileObject

files = []

folderPath = "./../pictures"

os.chdir(folderPath)
fileTypes = []
for file in glob.glob("*.*"):
    files.append(file)

file_Object = []

for file in files:
    file_Object.append(fileObject.File(file, os.path.getctime(folderPath + '/' + file)))

file_sorter = sortFilesByEvent.SortFiles(file_Object)

sorted_files = file_sorter.sortByDataType()
jpeg = sorted_files[0]
raw = sorted_files[1]
print("Sort By JPEG/RAW")
print("---")
print("JPEG")
for file in jpeg:
    print("- " + file.fileName)
print("RAW")
for file in raw:
    print("- " + file.fileName)

print("\n")
print("Sort By Timestamp")
print("---")
sorted_files_by_timestamp = file_sorter.sortByTimeStamp()
for file in sorted_files_by_timestamp:
    print("- " + file.fileName)