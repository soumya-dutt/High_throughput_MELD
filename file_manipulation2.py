# This script makes another directory with the same folders and copies only one file
# from the previous sorted folders to these newly created sub folders in the new directory. 

import os
import shutil
from tqdm import tqdm

main_directory = "/home/sdutta46/Desktop/tristan_sorted"
destination_directory = "/home/sdutta46/Desktop/MSA_sorted"

existing_folders = [folder for folder in os.listdir(main_directory) if os.path.isdir(os.path.join(main_directory, folder))]

os.makedirs(destination_directory, exist_ok=True)

for folder in tqdm(existing_folders, desc="Processing Folders", unit="folder"):
    folder_path = os.path.join(main_directory, folder)
    folder_files = os.listdir(folder_path)
    if folder_files:
        first_file_name = folder_files[0]
        
        new_folder_path = os.path.join(destination_directory, folder)
        os.makedirs(new_folder_path, exist_ok=True)
        
        source_file_path = os.path.join(folder_path, first_file_name)
        destination_file_path = os.path.join(new_folder_path, first_file_name)
        
        shutil.copy(source_file_path, destination_file_path)

print('job done!!')