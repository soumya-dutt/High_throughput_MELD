# This script runs the bias script and the system setup script in the folders

import os
import subprocess
from tqdm import tqdm

# Path to the parent directory containing subdirectories
parent_directory = '/home/sdutta46/Desktop/MSA_set2'

# Function to execute a Python script in a given directory
def execute_script_in_directory(directory, script_name):
    script_path = os.path.join(directory, script_name)
    if os.path.exists(script_path):
        subprocess.run(['python', script_path], cwd=directory)

# List to store directories where bias1.dat was not generated
missing_bias_directories = []

# Traverse through subdirectories and execute 'bias_old.py' script
for root, dirs, files in tqdm(os.walk(parent_directory), desc='Running bias_old.py'):
    for dir in dirs:
        subdirectory = os.path.join(root, dir)
        execute_script_in_directory(subdirectory, 'bias_old.py')
        if not os.path.exists(os.path.join(subdirectory, 'bias1.dat')):
            missing_bias_directories.append(subdirectory)

# Report directories where 'bias1.dat' was not generated
if missing_bias_directories:
    print("The following directories did not generate 'bias1.dat':")
    for missing_dir in missing_bias_directories:
        print(missing_dir)
else:
    print("All directories generated 'bias1.dat'.")

# Execute 'system_setup.py' script in directories with 'bias1.dat'
for root, dirs, files in tqdm(os.walk(parent_directory), desc='Running system_setup.py'):
    for dir in dirs:
        subdirectory = os.path.join(root, dir)
        if os.path.exists(os.path.join(subdirectory, 'bias1.dat')):
            execute_script_in_directory(subdirectory, 'system_setup.py')