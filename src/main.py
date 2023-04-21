import sortFilesByEvent
import fileObject

files = ['test.jpeg', 'test.jpg', 'test.raw']
file_Object = []

for file in files:
    file_Object.append(fileObject.File(file, 12))

file_sorter = sortFilesByEvent.SortFiles(file_Object)

sorted_files = file_sorter.sortBydataType()
jpeg = sorted_files[0]
raw = sorted_files[1]
for file in jpeg:
    print(file.fileName)
for file in raw:
    print(file.fileName)
