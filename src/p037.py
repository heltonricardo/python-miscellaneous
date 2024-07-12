import os
import shutil


parent = os.path.join("parent")
if not os.path.exists(parent):
    os.makedirs(parent)  # or
os.makedirs(parent, exist_ok=True)

# Creating folders and files:
for i in range(3):
    subdir = os.path.join(parent, str(i))
    os.makedirs(subdir, exist_ok=True)
    for j in range(2):
        sub_subdir = os.path.join(subdir, str(j))
        os.makedirs(sub_subdir, exist_ok=True)
        file_dir = os.path.join(sub_subdir, "file.txt")
        with open(file_dir, "w") as file:
            file.write("content")

# Listing recursively:
for root, dirs, files in os.walk(parent):
    print("Root: ", root)
    print("Dirs: ", dirs)
    print("Files:", files)
    print()

# Copying recursively:
shutil.copytree(parent, os.path.join("new_parent"))
