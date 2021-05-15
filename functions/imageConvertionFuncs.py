import numpy as np
from PIL import Image
import sys

#To see the full output uncommit the line below
np.set_printoptions(threshold=sys.maxsize)

def RGBConvert(path):
    '''Opens an image file and convert it to RGB, then convert the RGB values to binary
    For binary images, the values will be series of ones or zeroes, we can take the lsb because it represents
    the whole bits of the pixel'''

    img = Image.open(path)
    arr = np.array(img)

    binArr = np.unpackbits(arr,axis=2)


    # print(binArr)
    return binArr


def binaryConvert(path):
    '''Opens an image file and convert it to RGB, then convert the RGB values to binary
    For binary images, the values will be series of ones or zeroes, we can take the lsb because it represents
    the whole bits of the pixel'''

    img = Image.open(path)
    arr = np.array(img)

    #Convert boolean to binary
    arr = list(map(lambda x: x.astype(int), arr))


    # print(binArr)
    return arr