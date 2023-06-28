import torch
import torchvision.transforms as transforms
from PIL import Image
from pathlib import Path
import torchvision.transforms.functional as TF

def transformation_pipeline(img_input_path:Path, img_output_path:Path):
    
    image = Image.open(img_input_path)
    # Convert images to RGB. This is important
    # as the model was trained on RGB images.
    image = image.convert("RGB")

    # Image transformation pipeline.
    # Must match the training transformation pipeline
    pipeline = transforms.Compose([
      transforms.Resize(256),
      transforms.CenterCrop(256),
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    transformed_img = pipeline(image)
    
    # rescale values to be between 0-255
    min_val_abs = abs(torch.min(transformed_img))
    transformed_img +=  min_val_abs
    max_value = torch.max(transformed_img)
    transformed_img /= max_value # values between 0-1
    transformed_img *= 255 #values between 0-255
    #print(transformed_img)
    # Convert the tensor to a PIL image
    pil_image = TF.to_pil_image(transformed_img)

    # Save the PIL image to a file
    pil_image.save(img_output_path)
    
def main():
    img_input_path = Path("crop_Cecemel.jpg")
    img_output_path = Path("transfromed_cecemel.jpg")
    
    transformation_pipeline(img_input_path, img_output_path)
    
if __name__ == "__main__":
    main() 

