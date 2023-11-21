import mdtraj as md
import time

start = time.time()
# Define the input trajectory and topology files
trajectory_file = 'trajectory0.dcd'
topology_file = '1stframe.pdb'

# Load the trajectory and topology
traj = md.load(trajectory_file, top=topology_file)

# Specify the stride interval
stride = 10  # Replace with your desired stride value

# Stride the trajectory
strided_traj = traj[slice(0, traj.n_frames, stride)]

# Define the output file for the strided trajectory
output_file = 'strided_trajectory_mdtraj.dcd'

# Save the strided trajectory to a new file
strided_traj.save(output_file)

print(f'Strided trajectory saved as {output_file}')

end = time.time()

print(end - start)