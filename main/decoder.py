import qrtools
class decoder:
    def __init__(self,shapekey,Folderpath):
        self.shapekey=shapekey
        self.Folderpath=Folderpath
        self.decode()

    def decode(self):
        qr=qrtools.QR()
        files = os.listdir(self.Folderpath) # dir is your directory path
        one_d_array=[]
        for filename in files:
            file=self.Folderpath+filename
            qr.decode(file)
            one_d_array.append(qr.data)
            file=None
        #reforming the array back to the original shape
        extracted_array=np.asarray(one_d_array).reshape(self.shapekey)
        #convert back array to image
        extracted_image=Image.fromarray(extracted_array)
        extracted_image.show()
        extracted_image.save()



        