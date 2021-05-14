from scipy import misc

arr = misc.imageio.imread('lena.png') # 640x480x3 array
arr[20, 30] # 3-vector for a pixel