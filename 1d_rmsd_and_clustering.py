import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt

# Load your trajectory file (.dcd) and topology file (.pdb or .gro)
traj = md.load('trajectory0.dcd', top='1stframe.pdb')

# Compute the backbone atoms selection
backbone_atoms = traj.top.select('backbone')

# Align the frames to a reference structure (optional but recommended)
ref_frame = traj[0]
traj.superpose(reference=ref_frame, atom_indices=backbone_atoms)

# Get the number of frames
num_frames = traj.n_frames

# Creating a dummy rmsd list
rmsd_list = np.zeros(num_frames)

# Calculating rmsd wrt initial frame 
#k = 1
for i in range(num_frames):
    rmsd_val = md.rmsd(traj[i], traj[0], atom_indices=backbone_atoms)
    rmsd_list[i] = rmsd_val
    # k += 1
    # print(k)

# Saving the rmsd file    
np.savetxt('1d_rmsd.dat', rmsd_list)


# plotting stuff

# Load the data from the .dat file
data_file = "1d_rmsd.dat"
data = np.loadtxt(data_file)

# Create a simple line plot
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(data, label="RMSD Data")
plt.title("RMSD Trajectory Plot")
plt.xlabel("Frame")
plt.ylabel("RMSD Value (nm)")
plt.legend()
plt.grid(True)

# Save the plot as a .png image
plt.savefig("rmsd_plot.png")

# Creating the separate clusters
file_path = '1d_rmsd.dat'

# Create empty dictionary to store groups
groups = {}

# Open and read the .dat file
with open(file_path, 'r') as file:
    for index, line in enumerate(file):
        try:
            number = float(line.strip())
            # Calculate the group number based on the value
            group_number = int(number // 0.1)
            # Add the index to the corresponding group
            if group_number not in groups:
                groups[group_number] = []
            groups[group_number].append(index)
        except ValueError:
            print(f"Skipping line {index + 1} as it doesn't contain a valid number.")

for group_number, index_list in groups.items():
    group_file_name = f'group_{group_number}.dat'
    with open(group_file_name, 'w') as group_file:
        for index in index_list:
            group_file.write(f"{index}\n")