#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:09:17 2021

@author: skilpatrick
"""

#%%
# is the OLR mean substantially different from the composite mean? 
# stdev - useful metric to understand this
# new metric: absolute difference between snow heights

"""
create map for 2020-2021 year
	how does this new year compare to the all-year OLR la nina year?
create one map for each of all-year OLR la nina year average
create one map for all years total
"""
#%%

# are each of the year like the composite mean? if they are then the plot is robust
# if they're not it's not so great from a prediction perspective
#%% Ferret installation & activation code
# to install Ferret in Python environment: conda create -n FERRET -c conda-forge pyferret ferret_datasets --yes
# to install PyFerret in Python environment: conda create -n FERRET -c conda-forge pyferret ferret_datasets --yes
# to start using PyFerret: conda activate FERRET
# to end PyFerret session: conda deactivate

#%% Get last row of each .dat file 

with open('spencer_meadow.dat') as f:
    print([line.split()[-1] for line in f])

#%% SNOTEL dictionary loaded from 'SNOTEL_means.txt'
import os 
#import regex as re

path = os.path.abspath('SNOTEL_means.txt')
#print(path)
contents = open('SNOTEL_means.txt', 'rt')
lines = contents.readlines()
#print(lines[1][-30:-2].strip())
text = []
SNOTEL = dict()

station = 0
for line in lines:

    if line != '-----------------------------------\n':
        text.append(line)
        #print(text)
    if line == '-----------------------------------\n':
    
        name = text[0].strip()
        ln = text[1][-30:-2].strip()
        noln = text[2][-30:-2].strip()
        enm = text[3].strip()
        noenm = text[4].strip()
        lnm = text[5].strip()
        nolnm = text[6].strip()
        mn = text[7].strip()
        stdev = text[8].strip()
        
        data = [ln, noln, float(enm[-7:]), float(noenm[-7:]), float(lnm[-7:]), float(nolnm[-7:]), float(mn[-7:]), float(stdev[-7:])]
        
        print(data)
        SNOTEL[name[7:]] = data

        text = []
        station +=1
        
        
        
#print(SNOTEL.get('fish_lake'))
print(SNOTEL)

#%% Using SNOTEL.dict to calculate how many standard deviations away the measurements are

# ALLSITE DATA
"""
ln = [1989, 1999, 2000, 2011]
oln = [1985, 1996, 2001 , 2008, 2012]
lnm = 46.4289
otherlnm = 38.2387
enm = 32.3248
otherenm = 29.1009
mn = 35.6793
stdev = 10.3890

"""
# standard deviations can be found in SNOTEL.get
#import numpy as np
import matplotlib.pyplot as plt

def stdevsAway(stations):
    magnitudes = []
    magnitudec = []
    values = list(SNOTEL.keys())
    #stations = ['blewitt_pass', 'corral_pass', 'cougar_mountain', 'fish_lake', 'harts_pass', 'lone_pine', 'lyman_lake', 'olallie_meadows', 'park_creek', 'pope_ridge', 'potato_hill', 'rainy_pass', 'spencer_meadow', 'stampede_pass', 'surprise_lakes', 'white_pass']
    for i in stations:
        #print(i+"'s standard deviation:", SNOTEL.get(str(i))[-1]) # get the standard deviation
        magnitude_station = float(format(abs((SNOTEL.get(str(i))[-2] - SNOTEL.get(str(i))[4])/SNOTEL.get(str(i))[-1]), ".4f"))
        magnitude_comp = float(format(abs((SNOTEL.get(str(i))[-2] - 38.2387)/10.3890), ".4f"))
        magnitudes.append(magnitude_station)
        magnitudec.append(magnitude_comp)
    #print("station magnitudes:", magnitudes)
    #print("composite magnitudes:", magnitudec)
    
    j = 0
    
    for i in magnitudec:
        
        if i <= 0.25:
            print(stations[j], "- lightest shade 237,248,251")
        
        elif i >= 0.25 and i <= 0.5:
            print(stations[j], "- second lightest shade 191,211,230")
            
        elif i >= 0.5 and i <= 1:
            print(stations[j], "- third lightest shade 158,188,218")
        
        elif i >= 1 and i <= 1.5:
            print(stations[j], "- third darkest shade 140,150,198")   
            
        elif i >= 1.5 and i <= 2.0:
            print(stations[j], "- second darkest shade 136,86,167")
            
        elif i >= 2 and i <= 2.5:
            print(stations[j], "- darkest shade 129,15,124")
        
        j += 1
    plt.xticks(rotation=80)
    
    #stat = plt.bar(values[:-1], magnitudes), plt.axhline(1, linestyle = '--', color = 'red'), plt.title("SNOTEL Stations With OLR La Niña Means > 1 Standard Deviation Away From The Stations' Mean")
    com = plt.bar(values[:-1], magnitudec), plt.axhline(1, linestyle = '--', color = 'red'), plt.title("SNOTEL Stations With OLR La Niña Means > 1 Composite Standard Deviation Away From The Composite OLR La Niña Mean")
    
    #return stat
    return com

    # OLR la niña mean:
    #print("OLR la niña mean is", format(abs((SNOTEL.get(str(key))[-2] - SNOTEL.get(str(key))[4])/SNOTEL.get(str(key))[-1]), ".4f"), "standard deviations away from the mean") # subtract OLR LAN mean from the mean and divide by std dev
    
    
    # OLR el niño mean:
    #print("OLR el niño mean is", format(abs((SNOTEL.get(str(key))[-2] - SNOTEL.get(str(key))[2])/SNOTEL.get(str(key))[-1]), ".4f"), "standard deviations away from the mean")
    
    # la niña mean:
    #print("la niña mean is", format(abs((SNOTEL.get(str(key))[-2] - SNOTEL.get(str(key))[5])/SNOTEL.get(str(key))[-1]), ".4f"), "standard deviations away from the mean")
    
    # el niño mean:
    #print("el niño mean is", format(abs((SNOTEL.get(str(key))[-2] - SNOTEL.get(str(key))[3])/SNOTEL.get(str(key))[-1]), ".4f"), "standard deviations away from the mean")
    
stations = ['blewitt_pass', 'corral_pass', 'cougar_mountain', 'fish_lake', 'harts_pass', 'lone_pine', 'lyman_lake', 'olallie_meadows', 'park_creek', 'pigtail_peak', 'pope_ridge', 'potato_hill', 'rainy_pass', 'sheep_canyon', 'spencer_meadow', 'stampede_pass', 'stevens_pass','surprise_lakes', 'white_pass']
stdevsAway(stations)

#%%
"""
name = 'cougar_mountain'
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 8.1800
noenm = 7.7833
lnm = 23.0400
nolnm = 24.7000
mn = 15.9333
stdev = 10.7980

key = name
data = [enm, noenm, lnm, nolnm, mn, stdev]

SNOTEL[str(key)] = str(data)

% usage: [enm,noenm,lnm,nolnm,mn,stdev,ret,yr1] = tseries('name_of_site') 
% enm =  olr el nino mean
% noenm = non-OLR el nino mean
% lnm = olr la nina mean
% nolnm = non-OLR La Nina mean
% mn = overall time series mean
% stdev = time series standard deviation
% ret = data returned as [year(:) data(:)]
% y1 = first year of data
"""
"""
name = blewitt_pass 
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 13.1600
noenm = 10.0333
lnm = 15.9800
nolnm = 15.7800
mn = 13.2200
stdev = 5.5312

name = corral_pass
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 32.3400
noenm = 29.0500
lnm = 41.5800
nolnm = 31.6600
mn = 33.4024
stdev = 9.5579
SNOTEL = {'blewitt_pass': [[1989, 1999, 2000, 2011, 2021], [1985, 1996, 2001, 2008, 2012], 13.1600, 10.0333, 15.9800, 15.9800, 13.2200, 5.5312],
          'corral_pass': [[1989, 1999, 2000, 2011, 2021], [1985, 1996, 2001, 2008, 2012], 8.81800, 7.7833, 23.0400, 24.7000, 15.9333, 10.7980],
          'cougar_mountain': }
name = cougar_mountain
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 8.1800
noenm = 7.7833
lnm = 23.0400
nolnm = 24.7000
mn = 15.9333
stdev = 10.7980

name = fish_lake
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 25.5250
noenm = 24.7000
lnm = 38.4600
nolnm = 33.3400
mn = 29.6098
stdev = 10.2354

name = harts_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 43.0600
noenm = 36.9833
lnm = 51.8400
nolnm = 42.1800
mn = 43.3872
stdev = 11.6386

name = lone_pine
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 31.3200
noenm = 27.1667
lnm = 54.8400
nolnm = 40.6600
mn = 37.0220
stdev = 17.4157

name = lyman_lake
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 60.9250
noenm = 56.2667
lnm = 67.0800
nolnm = 54.9000
mn = 57.7500
stdev = 13.3331

name = olallie_meadows
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 47.0200
noenm = 43.0667
lnm = 65.1800
nolnm = 59.0600
mn = 51.6564
stdev = 17.4086

name = park_creek
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 47.0000
noenm = 39.1167
lnm = 55.1200
nolnm = 46.7200
mn = 44.5651
stdev = 13.0535

name = pope_ridge
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 15.0600
noenm = 15.6167
lnm = 19.8200
nolnm = 18.0800
mn = 15.8825
stdev = 5.6001

name = potato_hill
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 21.4500
noenm = 21.9833
lnm = 38.3800
nolnm = 31.5000
mn = 28.0500
stdev = 10.3187

name = rainy_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 39.7200
noenm = 34.4167
lnm = 43.8800
nolnm = 39.6600
mn = 38.4667
stdev = 10.0855

name = sheep_canyon
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 24.3250
noenm = 23.2667
lnm = 59.2600
nolnm = 42.4400
mn = 36.6421
stdev = 18.8327

name = spencer_meadow
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 24.8400
noenm = 22.0667
lnm = 46.6000
nolnm = 35.4250
mn = 30.3053
stdev = 15.7588

name = stampede_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 35.7600
noenm = 32.3167
lnm = 48.7000
nolnm = 44.6600
mn = 39.5949
stdev = 14.4252

name = stevens_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 31.3800
noenm = 32.7667
lnm = 48.5600
nolnm = 39.5000
mn = 37.7293
stdev = 12.9577

name = surprise_lakes
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 44.6000
noenm = 35.2667
lnm = 63.8400
nolnm = 48.7200
mn = 46.0167
stdev = 17.1828

name = white_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 21.3400
noenm = 17.4500
lnm = 27.2600
nolnm = 23.8400
mn = 22.4125
stdev = 7.4027
"""

#%% results from La Nina [obs_mean,p,sig95] = boot(yr,all,[1989 1999 2000 2011 2021])
  # after running allsite 
"""
obs_mean = 45.8389
p = 0.9800
sig95 = 45.2068   26.2211
"""
#%% results from OLR La Nina[obs_mean,p,sig95] = boot(yr,all,[1985 1996 2001 2008 2012])
"""
obs_mean = 38.2387
p = 0.6990
sig95 = 44.5200   26.8474
"""
#%%


