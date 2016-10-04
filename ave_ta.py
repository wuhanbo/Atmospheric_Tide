#! /usr/bin/env python
# Read in the netCDF file created by Plasim, as processed by burn

import numpy as np
from netCDF4 import Dataset
import csv
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('GTK')
#matplotlib.use('Agg')
#plt.ioff()
#from math import sqrt

global fh, lon, lat, time_days, time_hours, surface_pressure, y_fft, y_fft_plot, x_fft, N_x, ta, ave_ta, talist

#if (len(sys.argv)==1):
#    print "you need to enter the name of a file to read"
#    print len(sys.argv)
#    sys.exit()
#file_name = str(sys.argv)
#file_to_read = str(sys.argv[1])

def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step

talist = []
x = "diagfi4"

file_to_read = "/mnt/scratch-lustre/hanbo/LMDZ_finite/earth_24.0h/output/"+str(x)+".nc"
print('file name=', file_to_read)
fh = Dataset(file_to_read, "r")
    #lon = fh.variables["lon"][:]
    #lat  = fh.variables["lat"][:]
    #time_days = fh.variables["time"][:]
    #time_hours = time_days * 18.
    #ps = fh.variables["ps"][:]   #Pressure in mb for each (time,lat,lon)
ta = fh.variables["temp"][:]
    #print len(ps[0,0,:])
    #y_fft = np.zeros((len(ps[0,:,0]), len(ps[0,0,:])))
a = ta.mean(axis=0)
b = a.mean(axis=1)
c = b.mean(axis=1)
#ave_ta = c[::-1]
ave_ta = c.tolist()
print c
print c.mean

height = [0.004,0.017415589434569632,0.04197041134830409,0.09573548831202484,0.19905425549248695,0.37769312558816376,0.6610287582071787,1.0796026837077486,1.6625722655258326,2.4354958342473516,3.4187160120951323,4.626429653543951,6.066400344124698,7.740192276155182,9.643775222138789,11.768354425931134,14.1013017714798,16.627094227201624,19.32819502090663,22.185838414361832,25.18069885199589,28.293439635520574,31.505145841252258,34.797651936445185,38.153777455852705,41.55748503457441,44.99397475019655,48.44972762641897,51.91250966210532,55.371346124067344]

#plt.ioff()
plt.plot(ave_ta,height)
plt.xlabel("Temperture/K")
plt.ylabel("Height/km")
plt.title("Temperture Profile for Earth: 24.0h")
plt.show()
#plt.savefig("/mnt/scratch-lustre/hanbo/LMDZ/Temp_profile.pdf")
#plt.show()
#plt.close()

    #surf_ta = np.mean(ta[:,9,:,:])
fh.close()
    #talist.append(ave_ta)
    #print ave_ta


    

#des = "/mnt/scratch-lustre/hanbo/Plasim/T21/g-20_ta/g-20_ave_ta.csv"
#ta_array = np.asarray(talist)
#np.savetxt(des, ta_array)
