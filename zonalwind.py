#! /usr/bin/env python
# module load gcc/4.9.1 hdf5/1.8.14-gcc-4.9.1 python/2.7.9
# These modules have to be exactly these versions, or netcdf cannot be found.

# Read in the netCDF file created by Plasim, as processed by burn
from scipy.fftpack import fft
import sys
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import pickle

target = "diagfi7"

file = '/mnt/scratch-lustre/hanbo/LMDZ/earth_24.0h/output/'+target+'.nc'
# !!!waste 2 hrs in this path because initially /cita/scratch-lustre would not work!! Only /cita/d/scratch-lustre!!!!!!!!!

fh = Dataset(file, "r")
ua = fh.variables["u"][:]
a = ua.mean(axis=0)
b = a.mean(axis=2)
c = b [::-1]
print c.shape

with open("u_"+target+".txt","wb") as f:
	pickle.dump(c,f)

#fig, ax = plt.subplots()
#fig.canvas.draw()
#xlabel = [-90, -60, -30, 0, 30, 60, 90]
#ylabel = [0,10,20,30,40,52]
#ax.set_xticklabels(xlabel)
#ax.set_yticklabels(ylabel)

#plt.pcolor(c)
#plt.colorbar()


#plt.xlim(-90,90)
#plt.xlabel("Latitude/degree")
#plt.ylabel("Height/km")
#plt.title("Zonal wind for Earth: 24.0h")

#plt.show()

fh.close()

