import os
import xml.etree.ElementTree as ET

def calculate_dataset_statistics(input_folder, output_file):
    # Variables to store statistics
    unique_classes = set()
    total_objects = 0
    total_images = 0

    # Iterate over all XML files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            xml_path = os.path.join(input_folder, filename)

            # Parse the XML file
            tree = ET.parse(xml_path)
            root = tree.getroot()

            # Extract bounding box information for each object
            for obj_elem in root.findall("object"):
                name_elem = obj_elem.find("name")
                bbox_elem = obj_elem.find("bndbox")

                if name_elem is not None and bbox_elem is not None:
                    class_name = name_elem.text
                    unique_classes.add(class_name)
                    total_objects += 1

            total_images += 1

    # Calculate additional statistics
    objects_per_image = total_objects / total_images
    classes_per_image = len(unique_classes) / total_images

    # Log the statistics to the output file
    with open(output_file, "w") as f:
        f.write("Dataset Statistics:\n")
        f.write("-------------------\n")
        f.write(f"Total Images: {total_images}\n")
        f.write(f"Total Objects: {total_objects}\n")
        f.write(f"Unique Classes: {len(unique_classes)}\n")
        f.write(f"Objects per Image: {objects_per_image:.2f}\n")
        f.write(f"Classes per Image: {classes_per_image:.2f}\n")

    print("Statistics saved to", output_file)


def main():
    input_folder = "racks"
    output_file = "cornershop_stats.txt"
    calculate_dataset_statistics(input_folder, output_file)


if __name__ == "__main__":
    main()
