from PIL import Image
import cv2

def shrinkImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width / 2)
    new_height = int(height / 2)
    img.thumbnail((new_width, new_height), Image.ANTIALIAS)
    img.save(imgPath, quality=95, optimized=True)
    print(img)

    return


def enlargeImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width * 2)
    new_height = int(height * 2)
    newImg = img.resize((new_width, new_height), Image.ANTIALIAS)
    newImg.save(imgPath, quality=95)


    return
