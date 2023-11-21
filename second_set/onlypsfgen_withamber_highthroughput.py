import os
import subprocess
import glob

# Specify the path to the main directory containing subdirectories
main_directory = '/home/sdutta46/Desktop/MSA_set2'

# Define the VMD script content
vmd_script = """
package require psfgen 
amber    on
resetpsf
# Loading the molecule
mol new {}

# Separating all the protein chains.
set protein [atomselect top protein]
set chains [lsort -unique [$protein get pfrag]]
foreach chain $chains {{
    set sel [atomselect top "pfrag $chain"]
    $sel writepdb prot_frag${{chain}}.pdb
}}
# Making PSF from PDB using psfgen

topology /home/sdutta46/Desktop/amber22_src/dat/leap/cmd/leaprc.protein.ff14SB

pdbalias residue HIS HIE
pdbalias residue HIS HID
pdbalias atom ILE CD1 CD

foreach chain $chains {{
    segment $chain {{pdb prot_frag${{chain}}.pdb}}  
    coordpdb prot_frag${{chain}}.pdb $chain      
    guesscoord  
}}
writepdb prot_new.pdb
writepsf prot_new.psf
mol delete all
quit

"""

# Specify the patterns to delete
patterns_to_delete = ["*frag*", "*onlyprot*"]  # Add more patterns as needed

# Traverse subdirectories and process PDB files
for root, dirs, files in os.walk(main_directory):
    for filename in files:
        if filename.endswith(".pdb"):
            pdb_path = os.path.join(root, filename)
            output_directory = root
            with open(os.path.join(output_directory, 'temp_vmd_script.tcl'), 'w') as vmd_script_file:
                vmd_script_file.write(vmd_script.format(pdb_path))

            # Change the working directory to the output directory
            os.chdir(output_directory)

            # Execute VMD script using subprocess
            subprocess.run(['vmd', '-dispdev', 'text', '-e', 'temp_vmd_script.tcl'])

            # Remove files matching specified patterns
            for pattern in patterns_to_delete:
                for file_to_delete in glob.glob(pattern):
                    os.remove(file_to_delete)

            # Clean up temporary VMD script
            os.remove(os.path.join(output_directory, 'temp_vmd_script.tcl'))

            # Change the working directory back to the original main directory
            os.chdir(main_directory)

