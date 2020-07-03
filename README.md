# Image-to-Qrcode-Cryptography
The pyhton program to convert images into QRcodes which can be used for carrying confidential informations in a safer ways.
here the image is splitted into no of QRcodes according to the size of the image.
Inorder to extract the image back one have to arrange all the Qrcodes that are generated earlier in correct order to extract the exact information stored.
steps involved:

  step 1: The Image is converted intto N-d numpy arrays containing its pixel value.
  
  step 2: Them N-D numpy arrays arrays are converted into 1 D arrays
  
  step 3: The 1D array which is very long is splitted into number of arrays based on the size 
  
  step 4: These arrays are converted into no of QR codes 
  
  Step 5: While Extracting these QRcodes must be placed in order which it is encoded to get the exact image data from the QRcodes

