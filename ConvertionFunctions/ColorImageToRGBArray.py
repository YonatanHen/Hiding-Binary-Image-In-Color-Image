import numpy as np
from PIL import Image

def RGBConvert(path):
    img = Image.open(path)
    arr = np.array(img)  # 640x480x4 array
    print(arr)