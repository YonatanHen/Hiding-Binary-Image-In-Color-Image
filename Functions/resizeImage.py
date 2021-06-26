from PIL import Image

def reduceImage(imgPath):
    """Function reduce image height and width by 1.5 of the original size"""
    img = Image.open(imgPath)
    width, height = img.size
    new_width = int(width / 1.5)
    new_height = int(height / 1.5)
    newImg = img.resize((new_width, new_height), Image.BICUBIC)
    newPath = imgPath[:-4] + ' shrinked.png'
    newImg.save(newPath, quality=95, optimized=True)

    return newPath
