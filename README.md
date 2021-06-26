# DataSecurityProject


This project implements the Improved method using two Exclusive-OR to a binary image in RGB color image steganography algorithm 
which described here: https://www.sciencepubco.com/index.php/ijet/article/view/19692

The project is an OO final project of the College Data Security course

To see which packages you should install to run the code, type and run 'pip freeze' in the terminal :)

The encrypted image had been saved as colorImage.png whereas decrypted image was saved as a binaryImage.png, both pictures based on the pictures' given files in the Pictures directory.

In addition, we added 3 improvements to the algorithm:
1. Resizing images before encryption to improve algorithm speed.
2. Flipping bits to improve the security.
3. Checksum to each pixel to improve data transformation reliability.


### Screenshots:

Main menu:

![main menu](/Images/mainMenu.PNG)

Encryption results window:

![encryption](/Images/encrypted-image.PNG)

Decryption results window:

![decryption](/Images/decrypted-image.PNG)
