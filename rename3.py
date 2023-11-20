#thay thế phần mở rộng của tên file
import os

folder = r"D:\RenameFilePy\testfile\\"
# Listing the files of a folder
print('Before rename')
files = os.listdir(folder)
print(files)

# rename each file one by one
for file_name in files:
    # construct full file path
    old_name = os.path.join(folder, file_name)

    # Changing the extension from txt to pdf
    new_name = old_name.replace('.txt', '.pdf')
    os.rename(old_name, new_name)

# print new names
print('After rename')
print(os.listdir(folder))
