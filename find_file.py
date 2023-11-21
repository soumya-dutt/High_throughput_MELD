 # This script find the name of the directories where the 1stframe.pdb file exists
import os
 
 # Define the root directory you want to start the search from
root_directory = '/scratch/sdutta46/MSA_sorted'
 
 # Initialize counters for subdirectories with '1stframe.pdb' and '.pdb' files
subdirectories_with_1stframe_pdb = []
 #subdirectories_with_pdb_files = []
 
 # Walk through the directory tree
for dirpath, dirnames, filenames in os.walk(root_directory):
     # Check if the file  exists in the current directory
    if '1stframe.pdb' in filenames:                     # Change the file name that you want to check for.
         subdirectories_with_1stframe_pdb.append(dirpath)
     # Check if any '.pdb' file exists in the current directory
    # if any(filename.endswith('.pdb') for filename in filenames):
    #      subdirectories_with_pdb_files.append(dirpath)

 # Print subdirectories with '1stframe.pdb' and '.pdb' files separately
print("Subdirectories with the file:")
for subdir in subdirectories_with_1stframe_pdb:
    print(subdir)
 
 #print("\nSubdirectories with '.pdb' files:")
 #for subdir in subdirectories_with_pdb_files:
 #    print(subdir)
 
 # Print the counts
print("\nNumber of subdirectories with '1stframe.pdb' file:", len(subdirectories_with_1stframe_pdb))











































