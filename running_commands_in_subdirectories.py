import os
import subprocess

# Define the command to execute
#command = 'extract_trajectory extract_traj_dcd --replica 0 trajectory0.dcd'
#command ="ls"
command = ""        # Write the command inside quotes
# Function to execute the command in a directory
def execute_command_in_directory(directory):
    try:
        # Change to the specified directory
        os.chdir(directory)
        
        # Execute the command in the current directory
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f"Error in directory '{directory}': {str(e)}")

# Specify the root directory where you want to start
root_directory = '/home/sdutta46/Desktop/MSA_set2'

# Iterate over subdirectories in the root directory
for subdir in os.listdir(root_directory):
    # Create the full path of the subdirectory
    subdir_path = os.path.join(root_directory, subdir)
    
    # Check if the item in the root directory is a directory and not a file
    if os.path.isdir(subdir_path):
        # Execute the command in the subdirectory
        execute_command_in_directory(subdir_path)
