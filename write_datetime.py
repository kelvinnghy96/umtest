from datetime import datetime
import os

# Get the current date and time
now = datetime.now()

# Format the date and time as a string for the content
current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Format the date and time as a string for the filename
# Ensure the filename is valid by replacing spaces and colons with underscores
filename_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{filename_time_str}.txt"

# Specify the directory where you want to save the file
directory = r"C:\Users\kelvi\Desktop\testing py scheduler"

# Create the full path
full_path = os.path.join(directory, filename)

# Write the current date and time to the file
with open(full_path, "w") as file:
    file.write(f"Current date and time: {current_time_str}")

print(f"Date and time written to {full_path}")
