# thay thế một phần tên file bằng kí tự khác
import glob
import os

path = r"D:\RenameFilePy\testfile\\"
# search text files starting with the word "sales"
pattern = path + "*Document" + "*pdf"

# List of the files that match the pattern
result = glob.glob(pattern)

# Iterating the list with the count
#count = 1
for file_name in result:
    print(file_name)
    old_name = file_name
    file_name_1 = file_name.replace(' Document','Text')
    new_name = file_name_1 + ".pdf"
    os.rename(old_name, new_name)
   # count = count + 1

# printing all revenue txt files
res = glob.glob(path + "revenue" + "*.mp3")
for name in res:
    print(name)