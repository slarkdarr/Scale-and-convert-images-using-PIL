from PIL import Image

def rotate_image(img):
    img.rotate(-90)                 # Rotate image 90 degrees clockwise

def resize_image(img):
    return img.resize((128, 128))   # Resize image to 128x128

def convert_to_rgb(img):
    return img.convert('RGB')       # Convert image to RGB so it can be saved as JPEG

def save(img, outfile):
    img.save(outfile, 'JPEG')       # Save image with JPEG format
