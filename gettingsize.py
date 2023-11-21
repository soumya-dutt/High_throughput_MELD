import os

# Function to calculate the size of a file and print it along with the directory name
def calculate_file_size(directory):
    file_path = os.path.join(directory, "trajectory0.dcd")
    
    # Check if the file exists in the directory
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        file_size_mb = file_size/(1024 ** 2)                # Convert bytes to gigabytes
        
        if file_size_mb <= 900 :
            print(f"Directory: {directory},  Size of trajectory0.dcd: {file_size_mb} mb")

# Function to search for 'trajectory0.dcd' files in subdirectories
def search_for_files(root_directory):
    for root, dirs, files in os.walk(root_directory):
        # Process only the immediate subdirectories, not nested ones
        if root == root_directory:
            for directory in dirs:
                calculate_file_size(os.path.join(root, directory))

# Replace 'your_root_directory' with the path to your top-level directory
your_root_directory = '/scratch/sdutta46/MSA_sorted'

search_for_files(your_root_directory)

