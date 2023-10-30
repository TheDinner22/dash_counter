import numpy as np
# https://stackoverflow.com/questions/57657765/read-pdf-as-a-picture
from pdf2image.pdf2image import convert_from_path
import tempfile

def is_black(rgb_tuple):
    if (rgb_tuple[0] == rgb_tuple[1] and rgb_tuple[1] == rgb_tuple[2] and rgb_tuple[2] == 0):
        return True
    return False
def is_white(rgb_tuple):
    if (rgb_tuple[0] == rgb_tuple[1] and rgb_tuple[1] == rgb_tuple[2] and rgb_tuple[2] == 255):
        return True
    return False


Ys = []
Xs = []
paths = [
    "lectures/inclass1.pdf", 
    "lectures/inclass2.pdf", 
    "lectures/inclass3.pdf", 
    "lectures/inclass4.pdf", 
    "lectures/inclass5.pdf", 
    "lectures/inclass6.pdf", 
    "lectures/inclass7.pdf", 
    "lectures/inclass8.pdf", 
    "lectures/inclass9.pdf", 
    "lectures/inclass10.pdf", 
    "lectures/inclass11.pdf", 
    "lectures/inclass12.pdf", 
    "lectures/inclass13.pdf", 
    "lectures/inclass14.pdf", 
    "lectures/inclass15.pdf", 
    "lectures/inclass16.pdf", 
    "lectures/inclass17.pdf", 
    "lectures/inclass18.pdf", 
    "lectures/inclass19.pdf", 
    "lectures/inclass20.pdf", 
    "lectures/inclass21.pdf", 
    "lectures/inclass22.pdf", 
    "lectures/inclass23.pdf", 
    "lectures/inclass24.pdf", 
    "lectures/inclass25.pdf", 
    "lectures/reviewsession1.pdf", 
    "lectures/reviewsession2.pdf", 
]
for path in paths:
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(path, output_folder=path)

        # total height (Y)
        pdf_height = 0
        for image in images:
            pdf_height += image.height
        print(f"pdf_height: {pdf_height}")
        Ys.append(pdf_height)

        # number of squigles (X) (became number of pixels)
        squiggles_pixel_count = 0
        for image in images:
            ## crop image (we only care about right side)
            bound = (image.width - image.width//16, 0, image.width, image.height) ## arbitrary bound
            cropped = image.crop(bound)
            # cropped.show("test")
            ## get pixels as list
            pixels = []
            for i in range(cropped.height):
                for j in range(cropped.width):
                    pixels.append(cropped.getpixel((j, i)))

            for pixel in pixels:
                if not is_white(pixel):
                    squiggles_pixel_count += 1
        Xs.append(squiggles_pixel_count)
    print(Ys)
    print(Xs)
    print()
