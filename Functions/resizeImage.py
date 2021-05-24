from PIL import Image
import cv2

def reduceImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width / 1.5)
    new_height = int(height / 1.5)
    newImg = img.resize((new_width, new_height), Image.BICUBIC)
    newImg.save(imgPath, quality=95, optimized=True)
    print(img)

    return


def enlargeImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width * 1.5)
    new_height = int(height * 1.5)
    newImg = img.resize((new_width, new_height), Image.ANTIALIAS)
    newImg.save(imgPath, quality=95)


    return
