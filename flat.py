#Author: Parth Nayak
#Normalised Super Master Flat making code

import astropy
from astropy.io import fits as asf
import glob
import numpy as np
import os
import sys
from datetime import datetime as dt

home=os.path.expanduser("~")

path=home+"/Desktop/Astro/IBAC Research Group/Data/Sample/"
print("The current path to the data directory is:"+path+" (You can change this in the code, line 14)")
truce=input("Is the path correct? [y|n]")
if truce=='':
    truce='y'
if truce=="n":
    path=input("Please specify the full path to the data directory:")
    truce='y'
if truce!='y':
    sys.exit("Invalid choice.")
if path[-1]!="/":
    path+="/"

flat_list=glob.glob(path+"Flat/flat*.fits")
#print(flat_list)
try:
    mb=asf.open(path+"Bias/mbias.fits")
except FileNotFoundError:
    sys.exit("Master Bias not found.")
mbias=mb[0].data
mb.close()

F=[]
hdr=asf.open(flat_list[0])[0].header
for flat in flat_list:
    f=asf.open(flat)
    arr=f[0].data
    f.close()
    F.append(arr)
    
F=np.array(F)
#print(F.shape)
MFlat=np.median(F, axis=0)
#print(MFlat.shape)
SMFlat=MFlat-mbias
mean=np.mean(SMFlat)
NSMFlat=SMFlat/mean
today=str(dt.today().date())
comm="Median combined on "+today
hdr["FILETYPE"] =("Normalized Super Master Flat", comm)
nsmflat=asf.HDUList([asf.PrimaryHDU(NSMFlat, header=hdr)])
nsmflat.writeto(path+"Flat/nsmflat.fits", overwrite=True)
nsmflat.close()
print("Normalised Super Master Flat saved in the same directory 'Flat' as 'nsmflat.fits'.")