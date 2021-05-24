from PIL import Image
import cv2

def shrinkImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width - width / 100)
    new_height = int(height - width / 100)
    img.thumbnail((new_width, new_height))
    img.save(imgPath, quality=95)
    print(img)

    return


def enlargeImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width + width / 100)
    new_height = int(height + width / 100)
    newImg = img.resize((new_width, new_height))
    newImg.save(imgPath, quality=95)


    return
