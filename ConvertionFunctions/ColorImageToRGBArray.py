import numpy as np
from PIL import Image
import sys

#To see the full output uncommit the line below
np.set_printoptions(threshold=sys.maxsize)

def RGBConvert(path):
    #Open file and convert to RGB
    img = Image.open(path)
    arr = np.array(img)

    binArr = np.unpackbits(arr,axis=2)


    print(binArr)