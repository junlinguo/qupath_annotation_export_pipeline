'''
Rename qupath exported tiff's filenames
'''

import os

def rename_tif_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png.tif"):
            new_filename = filename.replace(".png.tif", ".tif")
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

# Specify the directory
masks_directory = '/home/guoj5/Documents/qupath_projects/ground_truth/masks'  # Replace with the actual path to the "masks" folder

# Call the function to rename files
rename_tif_files(masks_directory)
