import os
from PIL import Image

def rotate_image(img):
    return img.rotate(-90)          # Rotate image 90 degrees clockwise

def resize_image(img):
    return img.resize((128, 128))   # Resize image to 128x128

def convert_to_rgb(img):
    return img.convert('RGB')       # Convert image to RGB so it can be saved as JPEG

def save(img, outfile):
    img.save(outfile, 'JPEG')

def process_image(filename, directory):
    infile = os.path.join(directory, filename)          # Input file appended with the directory
    outfile = os.path.join('/opt/icons', filename)      # Output file appended with the directory

    # Image is processed here
    with Image.open(infile) as img:
        img_rotated = rotate_image(img)
        img_resized = resize_image(img_rotated)
        img_converted = convert_to_rgb(img_resized)
        save(img_converted, outfile)

def main():
    directory = 'images/'    # Images folder
    for filename in os.listdir(directory):
        if filename.startswith('ic_'):
            process_image(filename, directory)

if __name__ == '__main__':
    main()
