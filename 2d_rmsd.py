import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

start = time.time()

# Load your trajectory file (.dcd) and topology file (.pdb or .gro)
traj = md.load('strided_trajectory_mdtraj.dcd', top='1stframe.pdb')

# Compute the backbone atoms selection
backbone_atoms = traj.top.select('backbone')

# Align the frames to a reference structure (optional but recommended)
ref_frame = traj[0]
traj.superpose(reference=ref_frame, atom_indices=backbone_atoms)
print('superpose done')
# Get the number of frames
num_frames = traj.n_frames

# Initialize an empty RMSD matrix
rmsd_matrix = np.zeros((num_frames, num_frames))
print("dummy matrix created")
# Calculate RMSD values for all pairs of frames
k = 1
for i in range(num_frames):
    for j in range(i, num_frames):
        rmsd_value = md.rmsd(traj[i], traj[j], atom_indices=backbone_atoms)
        rmsd_matrix[i, j] = rmsd_value
        rmsd_matrix[j, i] = rmsd_value
        k += 1
        print(k)

np.savetxt('2d_rmsd_matrix.dat', rmsd_matrix)

# Create a heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(rmsd_matrix, cmap='viridis', cbar=True, square=True)

# Add labels and title
plt.xlabel('Frame Index')
plt.ylabel('Frame Index')
plt.title('RMSD Heatmap')

# Save the heatmap as a .png image
plt.savefig('rmsd_heatmap.png')

end = time.time()
print(end - start)
# Show the heatmap
#plt.show()

