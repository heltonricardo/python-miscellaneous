import os
from p035 import format_size, format_date


print("X" * 1000)
# Windows: cls | Unix/Linux/MacOS: clear
os.system("cls" if os.name == "nt" else "clear")

path = os.path.join("dir1", "dir2", "file.txt")
print(" 1)", path)

splitted = os.path.split(path)
print(" 2)", splitted)

directory, file = splitted
print(" 3)", directory)
print(" 4)", file)

file_name, extension = os.path.splitext(file)
print(" 5)", file_name)
print(" 6)", extension)

print(" 7)", os.path.abspath("."))

print("-" * 40)
for item in os.listdir("."):
    print(" 8)", item)

print("-" * 40)
for item in os.listdir("."):
    print(" 9)", item)
    if not os.path.isdir(item):
        continue
    for intern_item in os.listdir(item):
        print("    -", intern_item)


print("-" * 40)
for item in os.listdir("."):
    print("10)", item)
    print("    perms: ", os.stat(item).st_mode)
    print("    size:  ", format_size(os.path.getsize(item)))
    print("    access:", format_date(os.path.getatime(item)))
    print("    create:", format_date(os.path.getctime(item)))
    print("    modify:", format_date(os.path.getmtime(item)))
