import numpy as np
from PIL import Image
import sys
from Functions.bitManipulation import HVFlip

# To see the full output uncommit the line below
np.set_printoptions(threshold=sys.maxsize)


def RGBConvert(path):
    '''Opens an image file and convert it to RGB, then convert the RGB values to binary
    For binary images, the values will be series of ones or zeroes, we can take the lsb because it represents
    the whole bits of the pixel'''

    img = Image.open(path)
    arr = np.array(img)
    # Organize pixels in 3-d array of 24-bit
    binArr = np.unpackbits(arr, axis=2)
    return binArr, img


def binaryConvert(path):
    '''Opens an image file and convert it to RGB, then convert the RGB values to binary
    For binary images, the values will be series of ones or zeroes, we can take the lsb because it represents
    the whole bits of the pixel'''

    img = Image.open(path).convert('L')

    arr = np.array(img)

    # Convert boolean to binary
    newArr = ~arr
    newArr[newArr > 0] = 1
    newArr = HVFlip(newArr)

    return newArr, img


def arrToImage(arr, type):
    '''Function converts an arrray of bits to color image'''
    encryptArr = arr
    # Set new image name, according to received image type
    if type == 'RGB':
        imageName = 'encryptedImage.png'
        # Pack bits again and convert array to image
        encryptArr = np.packbits(arr, axis=2)
        img = Image.fromarray(encryptArr, type)

        # Save the image
        img.save(imageName)
        return img
    elif type == 'L':
        imageName = 'decyptedImage.png'
        # print(np.array([[255 if x == 1 else 0 for x in y] for y in arr]))
        width = len(arr)
        height = len(arr[0])
        arr = np.array(arr).flatten()
        arr = np.array(list(map(lambda x: 255 if x == 0 else 0, arr))).reshape(width, height)
        img2 = Image.fromarray(arr.astype('uint8'), 'L').convert('1')
        # Save the image
        img2.save(imageName)
        return img2
    else:
        print('Err')
        return
