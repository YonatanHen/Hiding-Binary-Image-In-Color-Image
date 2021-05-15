import numpy as np
from PIL import Image
import sys
from functions.errorMessages import errorMessage

# To see the full output uncommit the line below
np.set_printoptions(threshold=sys.maxsize)


def RGBConvert(path):
    '''Opens an image file and convert it to RGB, then convert the RGB values to binary
    For binary images, the values will be series of ones or zeroes, we can take the lsb because it represents
    the whole bits of the pixel'''

    img = Image.open(path)
    arr = np.array(img)

    binArr = np.unpackbits(arr, axis=2)
    arrToImage(arr, 'RGB')
    # print(binArr)
    return binArr, img


def binaryConvert(path):
    '''Opens an image file and convert it to RGB, then convert the RGB values to binary
    For binary images, the values will be series of ones or zeroes, we can take the lsb because it represents
    the whole bits of the pixel'''

    img = Image.open(path)
    arr = np.array(img)
    # Convert boolean to binary
    arr = np.array([x.astype(int) for x in arr])
    # print(binArr)
    return arr, img


def arrToImage(arr, type):
    '''Function converts an arrray of bits to color image'''

    #Set new image name, according to received image type
    if type == 'RGB':
        imageName = 'colorImg.png'
    elif type == 'L':
        imageName = 'binaryImg.png'
    else:
        print('Err')
        return

    # Convert array to image
    img = Image.fromarray(arr, type)

    #Save the image
    img.save(imageName)
    img.show()
