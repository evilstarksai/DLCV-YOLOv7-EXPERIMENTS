import os

# directory paths
dir1 = "images"
dir2 = "lable"

# get list of files in directories
dir1_files = set(os.path.splitext(f)[0] for f in os.listdir(dir1))
dir2_files = set(os.path.splitext(f)[0] for f in os.listdir(dir2))


# get set difference to find missing files
missing_files = dir1_files - dir2_files

# print missing files
print("Missing files in directory 2:")
for file in missing_files:
    print(file)

# delete extra files in directory 1
print("Deleting extra files in directory 1...")
for file in os.listdir(dir1):
    base_name, extension = os.path.splitext(file)
    if base_name not in dir2_files:
        os.remove(os.path.join(dir1, file))
        print(f"Deleted {file}")
print("Done!")
