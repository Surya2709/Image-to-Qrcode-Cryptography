from PIL import Image
import numpy as np
import sys
import decoder
import encoder


#loading the digital Image
image=Image.open('/home/darkhand/Documents/github/Image-to-Qrcode-Generator/src/flower.jpg')
#converting image to array
Matrix=np.asarray(image)
#recording the shape of the array
shape=Matrix.shape
data_size=313
#flattening the array to about 1d
np.set_printoptions(threshold=sys.maxsize)
flat_array=Matrix.flatten()


if __name__ == "__main__":
    c=Processor(flat_array,data_size,'/home/darkhand/Documents/github/Image-to-Qrcode-Generator/qrcodes')
    d=decoder(shapekeyhere,)







