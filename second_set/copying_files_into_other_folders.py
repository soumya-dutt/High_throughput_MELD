# This file copies the files needed to run meld and copies them to every folder.

import shutil
import os
from tqdm import tqdm  # Import the tqdm library

def copy_files_to_multiple_directories(source_dir, file_names, parent_target_dir):
    subdirectories = [item for item in os.listdir(parent_target_dir) if os.path.isdir(os.path.join(parent_target_dir, item))]
    
    for subdirectory in subdirectories:
        target_dir = os.path.join(parent_target_dir, subdirectory)
        for file_name in tqdm(file_names, desc=f"Copying to {subdirectory}", unit="file"):
            source_path = os.path.join(source_dir, file_name)
            target_path = os.path.join(target_dir, file_name)
            
            if os.path.exists(source_path):
                try:
                    shutil.copy(source_path, target_path)
                    tqdm.write(f"File '{file_name}' copied to '{target_path}'.")
                except Exception as e:
                    tqdm.write(f"Error copying '{file_name}' to '{target_path}': {e}")
            else:
                tqdm.write(f"Source file '{file_name}' not found in '{source_dir}'.")

# Source directory containing files to be copied
source_directory = "/home/sdutta46/Desktop/Scripts"

# List of file names to be copied
files_to_copy = ["system_setup.py","bias_old.py","md.sh"]            # Here mention the files that are needed to be copied.
# Here a comma separated list of files can also be given. 
# For example files_to_copy = ["1d_rmsd_and_clustering.py" , "run_scripts.py" , "anyscript.py"] 

# Parent target directory containing all the subdirectories
parent_target_directory = "/home/sdutta46/Desktop/MSA_set2"

copy_files_to_multiple_directories(source_directory, files_to_copy, parent_target_directory)