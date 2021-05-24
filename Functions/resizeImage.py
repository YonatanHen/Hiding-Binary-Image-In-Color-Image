from PIL import Image


def shrinkImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width / 2)
    new_height = int(height / 2)
    newImg = img.resize((new_width, new_height), Image.ANTIALIAS)
    newImg.save(imgPath, quality=90, optimize=True)

    return


def enlargeImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width * 2)
    new_height = int(height * 2)
    newImg = img.resize((new_width, new_height), Image.ANTIALIAS)
    newImg.save(imgPath, quality=95, optimize=True)
    print(img)

    return
