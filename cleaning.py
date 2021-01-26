
#Cropping images

import astropy
from astropy.io import fits as asf
import glob
import os
import sys
from datetime import datetime as dt

home=os.path.expanduser("~")

path=home+"/Desktop/Astro/IBAC Research Group/Data/Sample/"
obj_list=glob.glob(path+"Obj/J*.fits")
try:
    mbias=asf.open(path+"Bias/mbias.fits")[0].data
    nsmflat=asf.open(path+"Flat/nsmflat.fits")[0].data
except FileNotFoundError:
    sys.exit("Master Bias and/or Normalized Master Flat not found.")


clean_path=path+"Clean/"
if not os.path.exists(clean_path):
    os.mkdir(clean_path)
pwd=os.getcwd()


today=str(dt.today().date())    
comm="Cleaned on "+today
for i in obj_list:
    print("Cleaning "+i+" ...")
    raw = asf.open(i)[0].data
    hdr = asf.open(i)[0].header
    clean=(raw-mbias)/nsmflat
    hdr["FILETYPE"]=("Cleaned Image", comm)
    hdul=asf.HDUList([asf.PrimaryHDU(clean, header=hdr)])
    hdul.writeto(clean_path+i.rpartition("/")[-1].rpartition(".")[0]+"_clean.fits", overwrite="True")
    print("\nDone.")
    hdul.close()
