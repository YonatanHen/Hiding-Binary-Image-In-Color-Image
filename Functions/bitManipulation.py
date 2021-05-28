def HVFlip(binImage):
    """ switching bits + replace even with odd rows"""
    for i in range(len(binImage) - 1):
        for j in range(len(binImage[i]) - 2):
            binImage[i][j], binImage[i][j + 1] = binImage[i][j + 1], binImage[i][j]
        binImage[i], binImage[i + 1] = binImage[i + 1], binImage[i]

    return binImage
