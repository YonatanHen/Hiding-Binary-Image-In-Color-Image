# Utility functions:

def XOR(a, b):
    """Implements XOR operation: if a != b return true, else false."""
    return a is not b


# End of utility functions

# Constants:

# RGB array is 24-bit array which divided to 3 parts, counting starts from 0 so lsb of every strip is the
# value of the length of the last bit in the strip - 1
lsbR = 7
lsbG = 15
lsbB = 23


def embeddingAlgorithm(colorImgArr, binaryImgArr):
    """Function implements the embedding algorithm which described in chapter 6.1 in the article.
    Note that zip stops when the shorter of the values stops"""

    for row, binRow in zip(range(len(colorImgArr)), range(len(binaryImgArr))):
        for col, binCol in zip(range(0, row + 1), range(0, binRow)):
            if not XOR(binaryImgArr[binRow][binCol], colorImgArr[row][col][lsbR]):  # XOR(LSB of Img_s, LSB of R part of Img_c)) = 00 or 11, i.e false
                if not XOR(1, colorImgArr[row][col][lsbG]):  # LSB of G part = 1, i.e XOR(1,LSB of G) = false
                    colorImgArr[row][col][lsbB] = 1
                else:
                    colorImgArr[row][col][lsbB] = 0
            else:  # XOR(LSB of Img_s, LSB of R part of Img_c)) = 01 or 10, i.e true
                if XOR(0, colorImgArr[row][col][lsbG]):  # LSB of G part = 1, i.e XOR(0,LSB of G) = true
                    colorImgArr[row][col][lsbB] = 0
                else:
                    colorImgArr[row][col][lsbB] = 1

    return colorImgArr


def reconstructedAlgorithm():
    """Function implements the reconstructed algorithm which described in chapter 6.2 in the article"""
    return