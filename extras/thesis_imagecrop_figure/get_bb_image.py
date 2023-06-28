import cv2

def draw_bounding_boxes(image_path, annotation_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Read the annotation file
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    # Denormalize and draw bounding boxes on the image
    for line in lines:
        class_num, x_center, y_center, width_a, height_a = map(float, line.split())

        # Denormalize the bounding box coordinates
        img_height, img_width, _ = image.shape
        x = int((x_center - width_a/2) * img_width)
        y = int((y_center - height_a/2) * img_height)
        width = int(width_a * img_width)
        height = int(height_a * img_height)

        # Draw the bounding box on the image
        cv2.rectangle(image, (x, y), (x+width, y+height), (0, 255, 0), 2)

    # Save the image with bounding boxes
    cv2.imwrite(output_path, image)

def draw_bounding_boxes_emphize(image_path, annotation_path, output_path, highlighted_indices=[], highlight_color=(0, 255, 0), line_thickness=2):
    """
    Emphasize bbs of highlited indicis
    """
    # Load the image
    image = cv2.imread(image_path)

    # Read the annotation file
    with open(annotation_path, 'r') as f:
        lines = f.readlines()

    # Denormalize and draw bounding boxes on the image
    for i, line in enumerate(lines):
        class_num, x_center, y_center, width_a, height_a = map(float, line.split())

        # Denormalize the bounding box coordinates
        img_height, img_width, _ = image.shape
        x = int((x_center - width_a/2) * img_width)
        y = int((y_center - height_a/2) * img_height)
        width = int(width_a * img_width)
        height = int(height_a * img_height)

        # Determine the color and line thickness for the bounding box
        color = highlight_color if i in highlighted_indices else (0, 255, 0)
        thickness = line_thickness if i in highlighted_indices else 6

        # Draw the bounding box on the image
        cv2.rectangle(image, (x, y), (x+width, y+height), color, thickness)

    # Save the image with bounding boxes
    cv2.imwrite(output_path, image)

def main():
    # Input image and annotation paths
    image_path = 'train_0.jpg'
    annotation_path = 'train_0.txt'

    # Output image path
    output_path = 'train_0_bb.jpg'

    # Call the function to draw bounding boxes
    draw_bounding_boxes(image_path, annotation_path, output_path)
    
    # Output image path of enph image
    output_path = 'train_0_bb_emph.jpg'

    # List of indices of bounding boxes to highlight
    highlighted_indices = [0, 55, 59, 111, 123]  # Example indices

    # Color for highlighted bounding boxes (BGR format)
    highlight_color = (0, 0, 255)  # Green

    # Line thickness for highlighted bounding boxes
    line_thickness = 15

    # Call the function to draw bounding boxes
    draw_bounding_boxes_emphize(image_path, annotation_path, output_path, highlighted_indices, highlight_color, line_thickness)


if __name__ == '__main__':
    main()
