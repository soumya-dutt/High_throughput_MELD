import os
import subprocess
from tqdm import tqdm

# Specify the main directory path
main_directory = '/home/sdutta46/Desktop/msa_test'

# Command template with a placeholder for input file name
command_template = "pdb4amber -i {} -o 1stframe.pdb"

# Get a list of immediate subdirectories in the main directory
subdirectories = [d for d in os.listdir(main_directory) if os.path.isdir(os.path.join(main_directory, d))]

# Create a tqdm progress bar
progress_bar = tqdm(subdirectories, desc="Processing Subdirectories", unit="subdirectory")

# Iterate through the subdirectories and run the command
for subdir in progress_bar:
    # Create the full path to the subdirectory
    subdirectory_path = os.path.join(main_directory, subdir)
    
    # Find all .pdb files in the subdirectory
    pdb_files = [f for f in os.listdir(subdirectory_path) if f.endswith(".pdb")]
    
    if pdb_files:
        # Use the first found .pdb file as the input file
        input_file = os.path.join(subdirectory_path, pdb_files[0])
        
        # Create the full command by replacing the placeholder with the input file name
        full_command = command_template.format(input_file)
        
        # Change the current working directory to the subdirectory
        os.chdir(subdirectory_path)
        
        # Run the command in the current subdirectory
        subprocess.call(full_command, shell=True)
        
        # Change back to the main directory
        os.chdir(main_directory)