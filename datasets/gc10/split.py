import random
import glob
import os
import shutil


def copyfiles(fil, root_dir):
    basename = os.path.basename(fil)
    filename = os.path.splitext(basename)[0]

    # copy image
    src = fil
    dest = os.path.join(root_dir, image_dir, f"{filename}.jpg")
    shutil.copyfile(src, dest)

    # copy annotations
    src = os.path.join(label_dir, f"{filename}.txt")
    dest = os.path.join(root_dir, label_dir, f"{filename}.txt")
    if os.path.exists(src):
        shutil.copyfile(src, dest)


label_dir = "labels/"
image_dir = "images/"
lower_limit = 0
files = glob.glob(os.path.join(image_dir, '*.jpg'))

random.shuffle(files)

output = "output/"
folders = {"train": 0.8, "val": 0.1, "test": 0.1}
check_sum = sum([folders[x] for x in folders])

assert check_sum == 1.0, "Split proportion is not equal to 1.0"

oplabel_dir = os.path.join(output, label_dir)
opimage_dir = os.path.join(output, image_dir)

if(os.path.exists(output)):
    shutil.rmtree(output)

os.mkdir(output)
os.mkdir(oplabel_dir)
os.mkdir(opimage_dir)

for folder in folders:
    temp_label_dir = os.path.join(oplabel_dir, folder)
    os.mkdir(temp_label_dir)
    temp_image_dir = os.path.join(opimage_dir, folder)
    os.mkdir(temp_image_dir)

    limit = round(len(files) * folders[folder])
    for fil in files[lower_limit:lower_limit + limit]:        
        # Replace 'folder' with subfolder name in destination paths
        basename = os.path.basename(fil)
        filename = os.path.splitext(basename)[0]
        src = os.path.join(label_dir, f"{filename}.txt")
        dest = os.path.join(output, label_dir, folder, f"{filename}.txt")
        if os.path.exists(src):
            shutil.copyfile(src, dest)
        src = os.path.join(image_dir, f"{filename}.jpg")
        dest = os.path.join(output, image_dir, folder, f"{filename}.jpg")
        if os.path.exists(src):
            shutil.copyfile(src, dest)
