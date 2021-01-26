import astropy
from astropy.io import fits as asf
import glob
import os
import sys
from datetime import datetime as dt
import getpath as sidc

def crop(arr, x_start=0, x_end=-1, y_start=0, y_end=-1):
    return arr[y_start:y_end, x_start:x_end]


path=sidc.getpath()   #Use my custom defined function in getpath.py
print("The current path to the data directory is:"+path)
print("Delete dirname.txt to change this")


bias_list=glob.glob(os.path.join(path,"Bias","bias*.fits"))	#List of all bias files - system independent
flat_list=glob.glob(os.path.join(path,"Flat","flat*.fits"))	#List of all flat files - system independent
obj_list=glob.glob(os.path.join(path,"Obj","*.fits"))		#List of all obj files - system independent

file_list=bias_list+flat_list+obj_list

for file in file_list:
    print(file)
    hdul=asf.open(file, mode='update')
    hdr=hdul[0].header
    if "CROP" in hdr.keys():
        if hdr["CROP"]=="True":
            print("Already cropped.")
            continue
        else:
            print("Cropping image...")
    else:
        print("Cropping image...")
    arr=hdul[0].data
    arr=crop(arr, x_start=64, x_end=2106)
    hdul[0].data=arr
    comm="Image cropped on "+str(dt.today().date())
    hdr["CROP"]=("True", comm)
    hdul[0].header=hdr
    hdul.flush()
    
    hdul.close()
    
print("Crop successful!")