from PIL import Image


def shrinkImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width / 2)
    new_height = int(height / 2)
    img.thumbnail((new_width, new_height), Image.ANTIALIAS)
    img.save(imgPath, quality=100, optimize=True)

    return


def enlargeImage(imgPath):
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width * 2)
    new_height = int(height * 2)
    newImg = img.resize((new_width, new_height))
    newImg.save(imgPath)
    print(img)

    return
