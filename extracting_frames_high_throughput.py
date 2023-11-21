import mdtraj as md
import os
import shutil

# Set the main directory path
main_directory = '/home/sdutta46/Desktop/msa_test'
output_directory = '/home/sdutta46/Desktop/msa_test1'  # Specify the output directory

# Function to extract frames from DCD and save as PDB files
def extract_frames_from_dcd(dcd_file, topology_file, output_dir):
    traj = md.load(dcd_file, top=topology_file)
    stride = 20
    selected_frames = traj[::stride]

    for i, frame in enumerate(selected_frames):
        pdb_file_name = f'frame_{i * stride}.pdb'
        pdb_file_path = os.path.join(output_dir, pdb_file_name)
        frame.save(pdb_file_path)

# Traverse subdirectories and process DCD files
for root, dirs, files in os.walk(main_directory):
    for file in files:
        if file.endswith('trajectory0.dcd'):
            dcd_file_path = os.path.join(root, file)
            topology_file_path = os.path.join(root, '1stframe.pdb')  # Adjust topology file path

            # Create subdirectory structure in the output directory
            relative_path = os.path.relpath(root, main_directory)
            output_subdirectory = os.path.join(output_directory, relative_path)

            # Create the subdirectory if it doesn't exist
            os.makedirs(output_subdirectory, exist_ok=True)

            # Call the function to extract frames and save as PDB
            extract_frames_from_dcd(dcd_file_path, topology_file_path, output_subdirectory)