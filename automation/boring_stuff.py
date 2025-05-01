import os
import shutil

# explore file system
print(f"Current working Directory {os.getcwd()}")

print("Listing files and folders")

for item in os.listdir():
    print(f"- {item}")

# create folders and files
folder_name = "backup_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")
else:
    print("Folder already exists")

# with open("sample_file.txt", "w") as file:
#     file.write("Hello Python! Automate this!")

# move file to the backup folder
# shutil.move("sample_file.txt", f"{folder_name}/sample_file.txt")

# copy file back
# shutil.copy(f"{folder_name}/sample_file.txt", "sample_file_copy.txt")

# rename file
# os.rename("sample_file_copy.txt", "copied_file.txt")

# delete file
# os.remove("copied_file.txt")

# delete folder
# shutil.rmtree(folder_name)
