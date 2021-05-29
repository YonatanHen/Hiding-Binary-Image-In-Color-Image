def divideSequence(sequence):
    """Returning 3 lists that each one of them contains 8 bits out of the 24 bits sequence"""

    x1 = []
    x2 = []
    x3 = []

    for k in range(len(sequence)):
        if k >= 0 and k <= 7:
            x1.append(sequence[k])
        if k >= 8 and k <= 15:
            x2.append(sequence[k])
        if k >= 16 and k <= 23:
            x3.append(sequence[k])

    # Converting the three 8 bit sequences into integer numbers
    x1 = int(''.join(map(str, x1)), 2)
    x2 = int(''.join(map(str, x2)), 2)
    x3 = int(''.join(map(str, x3)), 2)

    return x1, x2, x3


def proccessChecksum(x1, x2, x3, checksum):
    """Those are the calculations themselves of creating/testing a checksum"""

    result = x1 + x2
    if result.bit_length() == 9:
        result = result & 0x0FF  # Removing the carry
        result = result + 0x01  # Summing the checksum with the carry
    result = result + x3
    if result.bit_length() == 9:
        result = result & 0x0FF  # Removing the carry
        result = result + 0x01  # Summing the checksum with the carry
    if checksum is not None:  # For testing an existing checksum
        result = result + int(checksum,2)
        if result == 0xFF:
            return True
        else:
            return False
    else:  # For creating a new checksum
        return result


def createChecksum(embeddedImage):
    """This algorithm will create a checksum for every 24 bit sequence of the embedded image"""

    checksumArr = []  # A list of checksums, checksum for each sequence

    for i in range(len(embeddedImage)):
        for j in range(len(embeddedImage[i])):
            # Creating 3 numbers that each of them will contain 8 bits out of the 24 bits from the sequence
            x1, x2, x3 = divideSequence(embeddedImage[i][j])

            # Creating the checksum
            checksum = proccessChecksum(x1, x2, x3, None)
            checksum = bin(checksum)
            checksumArr.append(checksum)

    return checksumArr


def testChecksum(embeddedImage, checksumArr):
    """Testing the checksum to see if it's valid"""

    for i in range(len(embeddedImage)):
        for j in range(len(embeddedImage[i])):
            # Creating 3 numbers that each of them will contain 8 bits out of the 24 bits from the sequence
            x1, x2, x3 = divideSequence(embeddedImage[i][j])
            for checksum in checksumArr:
                result = proccessChecksum(x1, x2, x3, checksum)
                if result is False:  # checksum is invalid
                    return result
    return True  # if for every iteration the checksum is 11111111, return true
