import cv2
from PIL import Image

def resize():
    img = Image.open('assets/source-photo.jpg')
    img.thumbnail((1000, 1000), Image.LANCZOS)
    img.save('assets/source-photo.jpg', 'JPEG')

resize()
