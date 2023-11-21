# This script goes through the initial folder with all the files and 
# sorts them in different folders with their respective names.

import os
import shutil
from tqdm import tqdm  # Import the tqdm module

file_dir = "/path/to/your/folder"
output_dir = "/path/to/output/folder"
unique_prefixes = set()

# Step 1: Get unique first 4 letters from file names
for filename in os.listdir(file_dir):
    if os.path.isfile(os.path.join(file_dir, filename)):
        unique_prefixes.add(filename[:25])                       # Taking upto 25 characters

# Step 2: Create folders
for prefix in unique_prefixes:
    folder_path = os.path.join(output_dir, prefix)
    os.makedirs(folder_path, exist_ok=True)

# Step 3: Copy files to respective folders
for filename in tqdm(os.listdir(file_dir), desc="Copying files", unit="file"):
    if os.path.isfile(os.path.join(file_dir, filename)):
        prefix = filename[:25]                                    # Taking upto 25 charcters
        source_path = os.path.join(file_dir, filename)
        destination_path = os.path.join(output_dir, prefix, filename)
        shutil.copyfile(source_path, destination_path)

print("Files have been sorted and copied to respective folders.")

# Seeing if the number of files in each folder exceedes the desired amount.

def count_files_in_folders(root_dir):
    folders_with_more_than_six_files = []

    for folder_name, subfolders, filenames in os.walk(root_dir):
        num_files = len(filenames)

        if num_files > 6:
            folders_with_more_than_six_files.append(folder_name)

    if not folders_with_more_than_six_files:
        print("No folders with more than 6 files found.")
    else:
        print("Folders with more than 6 files:")
        for folder in folders_with_more_than_six_files:
            print(folder)

root_directory = "/path/to/your/directory"
count_files_in_folders(root_directory)