#! /usr/bin/env python
# Read in the netCDF file created by Plasim, as processed by burn
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import sys
import numpy as np
from netCDF4 import Dataset
import csv
from math import sqrt

global fh, lon, lat, time_days, time_hours, surface_pressure, y_fft, y_fft_plot, x_fft, N_x

if (len(sys.argv)==1):
    print "you need to enter the name of a file to read"
    print len(sys.argv)
    sys.exit()
file_name = str(sys.argv)
file_to_read = str(sys.argv[1])
print('file name=', file_to_read)
#
#fh = Dataset("One_year-first_try.nc", "r")
fh = Dataset(file_to_read, "r")
#lon = fh.variables["lon"][:]
#lat  = fh.variables["lat"][:]
time_days = fh.variables["time"][:]
time_hours = time_days * 18.
ps = fh.variables["ps"][:]   #Pressure in mb for each (time,lat,lon)

print len(ps[0,0,:])
y_fft = np.zeros((len(ps[0,:,0]), len(ps[0,0,:])))

for lat in range(len(ps[0,:,0])):
    for lon in range(len(ps[0,0,:])):
        y_fft[lat,lon] = abs(fft(ps[:,lat,lon]))[730]*2/(len(ps[:,0,0]))

#print y_fft.shape
#a = np.asarray([ [1,2,3], [4,5,6], [7,8,9] ])
#np.savetxt('test.csv',y_fft)
#len_of_ps=len(ps[:,0,0])
#len_of_fft=len(y_fft[:,0,0])
#f = open('fft_test.out','w')
#f.write(str(y_fft))
#f.close()
#print len_of_ps
#print "\n"
#print len_of_fft

fh.close()



#print y_fft
#res = [x, y, z, ....]
csvfile = "<path to output csv or txt>"

#Assuming res is a flat list
#with open(csvfile, "w") as output:
#    writer = csv.writer(output, lineterminator='\n')
#    for val in res:
#        writer.writerow([val])    

#Assuming res is a list of lists
with open('test.csv', 'w') as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(np.asarray(y_fft))
