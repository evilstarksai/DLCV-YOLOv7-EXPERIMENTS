import os
import random
import shutil

# Source folders
image_folder = "datasets/pipe/images/train2021"
label_folder = "datasets/pipe/labels/train2021"

# Destination folder
random_folder = "datasets/random"

# Create the Random folder if it doesn't exist
if not os.path.exists(random_folder):
    os.mkdir(random_folder)

# Get list of files in the Image folder
image_files = os.listdir(image_folder)

# Shuffle the list of image files
random.shuffle(image_files)

# Calculate the number of files to move (20% of total)
num_files_to_move = int(len(image_files) * 0.2)

# Move the image files to the Random folder
for i in range(num_files_to_move):
    # Get the file name from the shuffled list
    file_name = image_files[i]

    # Get the corresponding label file name
    label_file_name = os.path.splitext(file_name)[0] + ".txt"

    # Move the image file
    shutil.move(os.path.join(image_folder, file_name), os.path.join(random_folder, file_name))

    # Move the label file
    shutil.move(os.path.join(label_folder, label_file_name), os.path.join(random_folder, label_file_name))

print(f"Moved {num_files_to_move} files to the Random folder.")
