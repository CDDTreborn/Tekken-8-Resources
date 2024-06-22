# Python script to search for keywords in .json files in a directory and all subfolders.
# Copy and save this script as "search_json.py"
# Make sure to update the json_directory and search_string variables to your needs.
# Open a cmd prompt
# Set the directory to where you saved the .py file
# Run the script by typing: python search_json.py

import json
import os

# Directory containing JSON files
json_directory = 'path/to/your/json/files'

# Strings to search for
search_string_1 = 'your_first_search_string'
search_string_2 = 'your_second_search_string'

# Function to search for the string in JSON data
def search_in_json(data, search_string):
    found = False
    if isinstance(data, dict):
        for key, value in data.items():
            if search_string in key or (isinstance(value, str) and search_string in value):
                found = True
            if search_in_json(value, search_string):
                found = True
    elif isinstance(data, list):
        for item in data:
            if search_in_json(item, search_string):
                found = True
    elif isinstance(data, str):
        if search_string in data:
            found = True
    return found

# Lists to keep track of files containing the search strings
files_containing_string_1 = []
files_containing_string_2 = []

# Walk through all files and subdirectories in the directory
for root, dirs, files in os.walk(json_directory):
    for file_name in files:
        if file_name.endswith('.json'):
            json_file_path = os.path.join(root, file_name)
            with open(json_file_path, 'r') as file:
                try:
                    json_data = json.load(file)
                    if search_in_json(json_data, search_string_1):
                        files_containing_string_1.append(json_file_path)
                    if search_in_json(json_data, search_string_2):
                        files_containing_string_2.append(json_file_path)
                except json.JSONDecodeError:
                    print(f'Error decoding JSON from file: {json_file_path}')

# Print out the search strings and the files containing them
print(f'Search string 1: {search_string_1}\n')
if files_containing_string_1:
    print('The first search string was found in the following files:')
    for file_path in files_containing_string_1:
        print(file_path)
else:
    print('The first search string was not found in any files.')

print(f'\nSearch string 2: {search_string_2}\n')
if files_containing_string_2:
    print('The second search string was found in the following files:')
    for file_path in files_containing_string_2:
        print(file_path)
else:
    print('The second search string was not found in any files.')

