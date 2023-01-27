import os

# Define the directory to search
directory = './files'

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Get the full path of the file
    file_path = os.path.join(directory, filename)

    # Check if the file is a text file
    if file_path.endswith('.txt'):
        # Open the file and read its contents
        with open(file_path, 'r') as f:
            contents = f.read()

        # Check if the file contains the word "important"
        if 'important' in contents:
            print(f'{file_path} contains the word "important"')
