import cv2
import numpy as np
import os

def add_contours_to_image(rgb_image, labeled_image, output_path):
    # Create a copy of the RGB image to draw contours on
    contour_image = rgb_image.copy()

    # Get the unique labels in the labeled image
    unique_labels = np.unique(labeled_image)

    for label in unique_labels:
        if label == 0:
            continue  # Skip the background

        # Create a binary mask for the current label
        mask = (labeled_image == label).astype(np.uint8)

        # Find contours for the current label
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours on the RGB image
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)  # Green color contours

    # Save the output image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure output directory exists
    cv2.imwrite(output_path, contour_image)
    print(f"Contours added and saved to {output_path}")




if __name__ == "__main__":
    import glob
    root_folder = "/home/guoj5/Documents"  # Replace with the path to your current folder
    train_png = "Bad_case_train"
    train_np = "Bad_case_train_labels"
    out_dir = "Bad_case_train_labels_png"

    # adjust
    root_folder = "/home/guoj5/Documents/qupath_projects/ground_truth"
    train_png = 'Bad_case_train'      # path to png
    train_np ='masks_npy'  # path to npy
    out_dir = 'masks_png'  # output path to save png+contours

    for img in os.listdir(os.path.join(root_folder, train_png)):
        if img.endswith(".png"):

            # load image, labels
            print(img)
            rgb_image = cv2.imread(os.path.join(root_folder, train_png, img))
            labeled_image = np.load(os.path.join(root_folder, train_np, img.replace(".png", ".npy"))).astype(np.uint16)

            # Construct the output path
            output_subdir = os.path.join(root_folder, out_dir)
            os.makedirs(output_subdir, exist_ok=True)
            output_path = os.path.join(output_subdir, img.replace('.png', '_contours.png'))

            # Add contours to the RGB image and save it
            add_contours_to_image(rgb_image, labeled_image, output_path)

        else:
            continue






