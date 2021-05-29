def createChecksum(embeddedImage):
    """This algorithm will create a checksum for every 24 bit sequence of the embedded image"""

    checksumArr=[] # A list of checksums, checksum for each sequence

    for i in range(len(embeddedImage)):
        for j in range(len(embeddedImage[i])):

            # Creating 3 lists that each of them will contain 8 bits out of the 24 bits
            x1 = []
            x2 = []
            x3 = []

            for k in range(len(embeddedImage[i][j])):
                if k>=0 and k<=7:
                    x1.append(embeddedImage[i][j][k])
                if k>=8 and k<=15:
                    x2.append(embeddedImage[i][j][k])
                if k >= 16 and k <= 23:
                    x3.append(embeddedImage[i][j][k])

            # Converting the three 8 bit sequences into integer numbers
            x1 = int(''.join(map(str, x1)), 2)
            x2 = int(''.join(map(str, x2)), 2)
            x3 = int(''.join(map(str, x3)), 2)

            checksum=x1+x2
            if checksum.bit_length()==9:
                checksum=checksum&0x0FF # Removing the carry
                checksum=checksum+0x01 # Summing the checksum with the carry
            checksum=checksum+x3
            if checksum.bit_length()==9:
                checksum=checksum&0x0FF # Removing the carry
                checksum=checksum+0x01 # Summing the checksum with the carry
            checksum=bin(checksum)
            checksumArr.append(checksum)

    return checksumArr


