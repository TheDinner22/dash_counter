import numpy as np
# https://stackoverflow.com/questions/57657765/read-pdf-as-a-picture
from pdf2image.pdf2image import convert_from_path
import tempfile

class Pixel:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if (not self.is_black() and not self.is_white()):
            print("ERROR: we only expect to see black and white pixels")

    def is_black(self):
        if (self.r == self.g and self.g == self.b and self.b == 0):
            return True
        return False
    def is_white(self):
        if (self.r == self.g and self.g == self.b and self.b == 255):
            return True
        return False


with tempfile.TemporaryDirectory() as path:
    images = convert_from_path('lectures/inclass25.pdf', output_folder=path)

    pdf_height = 0
    for image in images:
        pdf_height += image.height
    print(f"pdf_height: {pdf_height}")

    bound = (images[0].width - images[0].width//16, 0, images[0].width, images[0].height)
    cropped = images[0].crop(bound)
    cropped.show("test")
        

    
