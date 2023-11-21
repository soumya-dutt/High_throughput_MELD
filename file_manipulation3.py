import os
import shutil

# Source directory containing subdirectories and files
source_dir = "/home/sdutta46/Desktop/msa_test"
# Destination directory where subdirectories and files will be copied
destination_dir = "/home/sdutta46/Desktop/msa_test1"

# Iterate through the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # Check if the file matches the pattern "repstr*.pdb"
        if file.startswith("repstr") and file.endswith(".pdb"):
            # Create the corresponding subdirectory structure in the destination directory
            relative_path = os.path.relpath(root, source_dir)
            destination_subdir = os.path.join(destination_dir, relative_path)
            os.makedirs(destination_subdir, exist_ok=True)

            # Construct the source and destination file paths
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_subdir, file)

            # Copy the file to the destination subdirectory
            shutil.copy2(source_file, destination_file)

print("Files copied successfully!")