import pyqrcode
from PIL import Image
import math
import main

class Processor(object):
    def __init__(self,array,data_size,destination_folder):
        self.array=array
        self.data_size=data_size
        self.counter=1
        self.beg=0
        self.end=self.data_size
        self.destination_folder=destination_folder
        print('Shapekey:',main.shape)
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
        name=f"/{file_name}.png"
        qr_code.png(name,scale=10)
        image=Image.open(name)
        image=image.resize((400,400),Image.ANTIALIAS)
        destination=self.destination_folder+name
        image.save(destination,'PNG')
        print('Saving: ',name)
        self.counter+=1