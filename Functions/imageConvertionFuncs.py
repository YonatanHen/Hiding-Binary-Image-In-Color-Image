import numpy as np
from PIL import Image
import sys
from Functions.errorMessages import errorMessage

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

    img = Image.open(path)
    arr = np.array(img)

    # Convert boolean to binary
    newArr = [[1 if x else 0 for x in y] for y in arr]

    # Improving the Algorithm - David ##
    for i in range(0, len(newArr)-2, 2):
        newArr[i], newArr[i + 1] = newArr[i + 1], newArr[i]
    for i in range(len(newArr)):
        for j in range(len(newArr[i])-1):
            newArr[i][j], newArr[i][j + 1] = newArr[i][j + 1], newArr[i][j]

    print(newArr)
    # print(binArr)
    return arr, img


def arrToImage(arr, type):
    '''Function converts an arrray of bits to color image'''
    encryptArr = arr
    # Set new image name, according to received image type
    if type == 'RGB':
        imageName = 'colorImg.png'
        # Pack bits again and convert array to image
        encryptArr = np.packbits(arr, axis=2)
        img = Image.fromarray(encryptArr, type)

        # Save the image
        img.save(imageName)
        img.show()
    elif type == 'L':
        imageName = 'binaryImg.png'
        print(np.array([[255 if x == 1 else 0 for x in y] for y in arr]))

        #revert changes - David
        for i in range(0, len(arr) - 2, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for i in range(len(arr)):
            for j in range(len(arr[i]) - 1):
                arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        img2 = Image.fromarray(np.array([[255 if x == 1 else 0 for x in y] for y in arr]), 'PA').convert('1')
        print(img2)
        # Save the image
        img2.save(imageName)
        img2.show()
    else:
        print('Err')
        return





