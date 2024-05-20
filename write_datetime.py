#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time as a string for the content
current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Format the date and time as a string for the filename
# Ensure the filename is valid by replacing spaces and colons with underscores
filename_time_str = now.strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{filename_time_str}.txt"

# Write the current date and time to the file
with open(filename, "w") as file:
    file.write(f"Current date and time: {current_time_str}")

print(f"Date and time written to {filename}")


# In[ ]:




