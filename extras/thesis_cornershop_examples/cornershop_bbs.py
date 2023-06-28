import cv2
import os
import xml.etree.ElementTree as ET
import random

def crop_and_label_bounding_boxes(image_path, annotation_path, num_crops, output_directory):
    # Read the image
    image = cv2.imread(image_path)

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Parse the annotation file
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    # Collect the bounding box coordinates, labels, and indices
    bounding_boxes = []
    labels = []
    indices = []
    for i, obj in enumerate(root.iter('object')):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        label = obj.find('name').text

        bounding_boxes.append((xmin, ymin, xmax, ymax))
        labels.append(label)
        indices.append(i)

    # Shuffle the indices to randomly select crops
    random.shuffle(indices)

    # Crop and label the bounding boxes
    cropped_images = []
    cropped_indices = []
    for idx in indices[:num_crops]:
        xmin, ymin, xmax, ymax = bounding_boxes[idx]
        label = labels[idx]

        # Crop the bounding box
        crop = image[ymin:ymax, xmin:xmax]

        # Save the crop to a separate file
        crop_filename = f"crop_{label}.jpg"
        crop_filepath = os.path.join(output_directory, crop_filename)
        cv2.imwrite(crop_filepath, crop)

        # Add the crop and its index to the lists
        cropped_images.append(crop_filepath)
        cropped_indices.append(idx)

    return cropped_images, cropped_indices

def draw_bb_and_emphasize_crops(image_path, annotation_path, special_indices, emphasis_color, emphasis_thickness,
                          default_color, default_thickness, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Parse the annotation file
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    # Collect all bounding boxes and their indices
    bounding_boxes = []
    indices = []
    for i, obj in enumerate(root.iter('object')):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        bounding_boxes.append((xmin, ymin, xmax, ymax))
        indices.append(i)

    # Filter the indices to keep only the special indices
    selected_indices = [idx for idx in indices if idx in special_indices]

    # Draw bounding boxes for all objects
    for i, bbox in enumerate(bounding_boxes):
        xmin, ymin, xmax, ymax = bbox
        bbox_color = emphasis_color if i in selected_indices else default_color
        bbox_thickness = emphasis_thickness if i in selected_indices else default_thickness
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), bbox_color, bbox_thickness)

    # Crop and emphasize the selected bounding boxes
    for idx in selected_indices:
        xmin, ymin, xmax, ymax = bounding_boxes[idx]
        crop = image[ymin:ymax, xmin:xmax]
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), emphasis_color, emphasis_thickness)

    # Save the output image
    cv2.imwrite(output_path, image)
    print(f"Image with emphasized crops saved to {output_path}")

def draw_bbs(image_path, annotation_path, color, thickness, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Parse the annotation file
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    for obj in root.iter('object'):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        #draw BB
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, thickness)
    
    # Save the output image
    cv2.imwrite(output_path, image)
    print(f"Image with bounding boxes saved to {output_path}")
    
def main():
    image_path = "p1.jpg"
    annotation_path = "p1.xml"
    num_crops = 6  # Number of crops to extract
    output_directory = "crops"

    # cropped_images, cropped_indices = crop_and_label_bounding_boxes(image_path, annotation_path, num_crops, output_directory)

    # print("Cropped images:")
    # for i, crop in enumerate(cropped_images):
    #     print(f"Index: {cropped_indices[i]}, File: {crop}")
        
    # emphasis_color = (0, 0, 255)  # Red color for emphasized crops
    # emphasis_thickness = 15  # Thickness of emphasized crops
    # default_color = (0, 255, 0)  # Green color for non-emphasized crops
    # default_thickness = 6  # Thickness of non-emphasized crops
    # output_path = "p1_bb_emph.jpg"

    # draw_bb_and_emphasize_crops(image_path, annotation_path, cropped_indices, emphasis_color, emphasis_thickness,
    #                       default_color, default_thickness, output_path)
    
    output_path = "p1_bb.jpg"
    color = (0, 255, 0)
    thickness = 6
    draw_bbs(image_path, annotation_path, color, thickness, output_path)


if __name__ == "__main__":
    main()


