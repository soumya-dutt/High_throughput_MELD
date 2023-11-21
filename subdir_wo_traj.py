import os

# Define the root directory where you want to start the search
root_directory = "/scratch/sdutta46/MSA_sorted"

# Define the name of the file you want to search for
file_to_find = "trajectory0.dcd"

# Initialize a list to store subdirectories without the file
subdirectories_without_file = []

# Get a list of immediate subdirectories in the root directory
immediate_subdirectories = next(os.walk(root_directory))[1]

# Check if the file is missing in each immediate subdirectory
for directory in immediate_subdirectories:
    subdirectory_path = os.path.join(root_directory, directory)
    if not os.path.isfile(os.path.join(subdirectory_path, file_to_find)):
        subdirectories_without_file.append(subdirectory_path)

# Print the subdirectories without the file
for directory in subdirectories_without_file:
    print("Directory without {} file: {}".format(file_to_find, directory))

