import os
import shutil
from datetime import datetime 

def copy_files(source_directory, destination_directory):
    try:
        if not os.path.exists(source_directory): #checking if source exists
            raise FileNotFoundError(f"Source directory '{source_directory}' not found.")

        if not os.path.exists(destination_directory): #if destinstion dir is not present it willnot creates it
            os.makedirs(destination_directory)

        for filename in os.listdir(source_directory): #looping for every file
            source_filepath = os.path.join(source_directory, filename)
            destination_filepath = os.path.join(destination_directory, filename)

            shutil.copy2(source_filepath, destination_filepath) # copying the file
            print(f"File '{filename}' copied to '{destination_directory}'")

        print("All files copied successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
source_directory = r"C:\vlearn assignment\Source"
destination_directory = r"C:\vlearn assignment\Destination"

copy_files(source_directory, destination_directory)