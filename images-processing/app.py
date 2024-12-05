import os
import sys

from PIL import Image, ImageFilter

if sys.argv[1] == "-r" or sys.argv[1] == "--resize":
    for file in sys.argv[2:]:
        base_name = os.path.basename(file)

        if not os.path.exists(file):
            print("File does not exist: {file}")
            continue

        try:
            with Image.open(file) as img:
                new_file_name = f"resized_{os.path.basename(file).split('.')[0]}_width_{sys.argv[3]}.png"
                img.thumbnail((int(sys.argv[3]), int(sys.argv[3])))
                img.save(new_file_name)
                print(f"Processed image {new_file_name}")
        except Exception as e:
            print(f"Failed to process image {base_name}: {e}")

elif sys.argv[1] == "-d" or sys.argv[1] == "--directory":
    image_dir = sys.argv[2]
    output_dir = sys.argv[3]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(image_dir):
        base_name = os.path.basename(file).split(".")[0]
        img_path = os.path.join(image_dir, file)

        if not os.path.exists(img_path):
            print("File does not exist: {file}")
            continue

        try:
            with Image.open(img_path) as img:
                new_file_name = os.path.join(output_dir, f"{base_name}.png")
                img.save(new_file_name)
                print(f"Processed image {new_file_name}")
        except Exception as e:
            print(f"Failed to process image {base_name}: {e}")

else:
    for file in sys.argv[1:]:
        base_name = os.path.basename(file)

        if not os.path.exists(file):
            print("File does not exist: {file}")
            continue

        try:
            with Image.open(file) as img:
                new_file_name = f"gray_scale_{os.path.basename(file).split(".")[0]}.png"
                filtered_img = img.convert("L").filter(ImageFilter.DETAIL)
                filtered_img.save(new_file_name)
                print(f"Processed image {new_file_name}")
        except Exception as e:
            print(f"Failed to process image {base_name}: {e}")

print("Done")
