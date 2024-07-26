## Overview

This repository provides a set of scripts and instructions for processing and visualizing image data for deep learning projects. The workflow involves using QuPath for exporting images, renaming them, converting to numpy arrays, and generating visualizations of the labeled data. Follow the steps below to set up and run the scripts efficiently.

## Prerequisites

- [QuPath](https://qupath.github.io)
- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - numpy
  - tifffile
  - matplotlib
  - opencv-python

## Workflow

### Step 1: QuPath Script Editor

1. Open QuPath.
2. Navigate to `Automate -> Script editor`.
3. Load the `export_to_tiff.groovy` script by dragging it to the editor.
4. Hit `Run` to process the entire project.

### Step 2: Rename TIFF Files

Use the `rename_tif.py` script to rename the TIFF files as needed.
rename tif (labels): python script ‘rename_tif.py’. Change the directory to the path to the tif folder

### Step 3: Convert TIFF to Npy

Use the `convert_tif_to_numpy` script to rename the TIFF files as needed.
define path  to the tif folder, and output dir 

### Step 4: Prepare images 

Ensure you have images (e.g., PNG) that correspond to the .npy or .tif masks				

### Step 5: Create Contour Visualizations

1. Organize the folders into a root folder with the following structure:
   ```
   root_folder/
   ├── train_png/  # Folder containing the images (e.g., PNG)
   ├── train_np/   # Folder containing the numpy label/masks
   └── out_dir/    # Output folder for the contours
   ```
	- root_folder: the directory of the folders above 
	- train_png: the image (e.g. png)  folder 
	- train_np: the npy label/masks  folder 
	- out_dir: the output folder of the contours

2. Use the `qupath_npy_png.py` script to create a folder of contours (image + labels overlay) for visualization
 
## Scripts

- **export_to_tiff.groovy**: Script for exporting images from QuPath to TIFF format.
- **rename_tif.py**: Python script for renaming TIFF files.
- **convert_tif_to_numpy.py**: Python script for converting TIFF files to numpy arrays.
- **qupath_npy_png.py**: Python script for creating contours (image + labels overlay) for visualization.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
