# Initialize variables to store the maximum number and its corresponding row
max_number = None
max_row = None

# Open and read the .txt file
with open('your_file.txt', 'r') as file:
    for line in file:
        # Split each line into its components using a comma as the separator
        parts = line.strip().split(',')
        
        # Ensure there are three columns in the line
        if len(parts) == 3:
            # Extract the third column (assuming it's a number)
            try:
                current_number = float(parts[2])
            except ValueError:
                # Handle cases where the third column is not a valid number
                continue

            # Check if this number is greater than the current maximum
            if max_number is None or current_number > max_number:
                max_number = current_number
                max_row = line

# Check if any valid number was found
if max_number is not None:
    print("The row with the biggest number is:")
    print(max_row)
    print("The biggest number is:", max_number)
else:
    print("No valid numbers found in the file.")

# Close the file (good practice)
file.close()
