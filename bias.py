
#Master Bias making code

import astropy
from astropy.io import fits as asf
import glob
import numpy as np
import os
import sys
from datetime import datetime as dt

home=os.path.expanduser("~")


path=home+"/Desktop/Astro/IBAC Research Group/Data/Sample/"
print("The current path to the data directory is: "+path+" (You can change this in the code, line 14)")
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

bias_list=glob.glob(path+"Bias/bias*.fits")

B=[]
hdr=asf.open(bias_list[0])[0].header
for bias in bias_list:
    b=asf.open(bias)
    arr=b[0].data
    b.close()
    B.append(arr)
    
B=np.array(B)
#print(B.shape)
MB=np.median(B, axis=0)
#print(MB.shape)
today=str(dt.today().date())
#print(today)
comm="Median combined on "+today
#print(comm)
hdr["FILETYPE"] =("Master Bias", comm)
mbias=asf.HDUList([asf.PrimaryHDU(MB, header=hdr)])
mbias.writeto(path+"Bias/mbias.fits", overwrite=True)
mbias.close()
print("Master Bias saved in the same directory 'Bias' with the name 'mbias.fits'.")
