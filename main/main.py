from PIL import Image
import numpy as np
import sys
import math
import os
import io
import pyqrcode

#loading the images
image=Image.open('path to the file')
#converting the images into a numpy array 
Matrix=np.asarray(image)
#saving the shape of the array thats the key
shape=Matrix.shape
data_size=313
#flattening the array to about 1d

np.set_printoptions(threshold=sys.maxsize)
flat_array=Matrix.flatten()
size=len(flat_array)
divisor=math.ceil(size/data_size)
#starting the qrcode func
#print(divisor)

class Processor(object):
    def __init__(self,array,data_size):
        self.array=array
        self.data_size=data_size
        self.counter=1
        self.beg=0
        self.end=self.data_size
        self.process()

    def process(self):
        divisor=math.ceil(len(self.array)/self.data_size)
        while(int(divisor))!=0:
            data=str(self.array[self.beg:self.end])
            self.qr_generator(data)
            self.beg=self.end
            self.end=self.end+self.data_size
            divisor-=1

    def qr_generator(self,text):
        qr_code=pyqrcode.create(text)
        file_name='Qrcode'+str(self.counter)
        name=f"{file_name}.png"
        qr_code.png(name,scale=10)
        image=Image.open(name)
        image=image.resize((400,400),Image.ANTIALIAS)
        image.save(name)
        print('Saving: ',name)
        self.counter+=1
        
if __name__ == "__main__":
    c=Processor(flat_array,data_size)


