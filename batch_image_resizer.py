from PIL import Image
import os

def resize_images(folder_path, width):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('jpg', 'jpeg', 'png', 'bmp')):
            img_path = os.path.join(folder_path, file_name)
            img = Image.open(img_path)
            aspect_ratio = img.height / img.width
            new_height = int(width * aspect_ratio)
            resized_img = img.resize((width, new_height))
            resized_img.save(os.path.join(folder_path, f"resized_{file_name}"))
            print(f"Resized: {file_name}")

folder_path = input("Enter the folder path with images: ")
width = int(input("Enter the width to resize images to: "))
resize_images(folder_path, width)
print("All images resized!")
