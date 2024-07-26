"""
convert qupath saved/exported 'tiff' to '.npy'
"""
import os
import numpy as np
from tifffile import imread

def convert_tif_to_npy(tif_path, npy_path):
    # Read the .tif file
    tif_data = imread(tif_path)
    # Save the data as .npy
    np.save(npy_path, tif_data)
    print(f'Converted: {tif_path} -> {npy_path}')

def convert_all_tif_files(masked_directory, output_directory):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(masked_directory):
        if filename.endswith(".tif"):
            base_filename = os.path.splitext(filename)[0]
            tif_path = os.path.join(masked_directory, filename)
            npy_path = os.path.join(output_directory, base_filename + ".npy")
            convert_tif_to_npy(tif_path, npy_path)

# Specify the directories
masked_directory = '/home/guoj5/Documents/qupath_projects/ground_truth/masks'  # Replace with the actual path to your "masked" folder
output_directory = '/home/guoj5/Documents/qupath_projects/ground_truth/masks_npy'  # Replace with the desired path for the output folder

# Convert all .tif files in the masked directory
convert_all_tif_files(masked_directory, output_directory)
