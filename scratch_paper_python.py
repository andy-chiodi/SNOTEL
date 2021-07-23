#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:09:17 2021

@author: skilpatrick
"""
# include all-station mean for SWE in inches variation bar graph plot (and mean or median, see what works)

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
        enm = text[3].strip() #el niño mean
        noenm = text[4].strip() #non-OLR el niño mean
        lnm = text[5].strip() #la niña mean
        nolnm = text[6].strip() #non-OLR la niña mean
        mn = text[7].strip() #station's overall mean
        stdev = text[8].strip() #station's overall standard devation
        
        data = [ln, noln, float(enm[-7:]), float(noenm[-7:]), float(lnm[-7:]), float(nolnm[-7:]), float(mn[-7:]), float(stdev[-7:])]
              #[0: OLR la niña year list, 
              #1: non-OLR la niña year list, 
              #2: OLR el niño mean, 
              #3: non-OLR el niño mean, 
              #4: OLR la niña mean, 
              #5: non-OLR la niña mean, 
              #6: station's overall mean, 
              #7: station's overall standard devation]
        print(data)
        SNOTEL[name[7:]] = data

        text = []
        station +=1
print(SNOTEL)
#%% Using SNOTEL.dict to calculate how many standard deviations away the measurements are
"""# ALLSITE DATA
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
import matplotlib.pyplot as plt
def plotStdevAway(stations):
    
    print("By station Comparison")

    magnitudes = []
    
    values = list(SNOTEL.keys())
    #stations = ['blewitt_pass', 'corral_pass', 'cougar_mountain', 'fish_lake', 'harts_pass', 'lone_pine', 'lyman_lake', 'olallie_meadows', 'park_creek', 'pope_ridge', 'potato_hill', 'rainy_pass', 'spencer_meadow', 'stampede_pass', 'surprise_lakes', 'white_pass']
    for i in stations:
    #print(i+"'s standard deviation:", SNOTEL.get(str(i))[-1]) # get the standard deviation
        magnitude_station = float(format((SNOTEL.get(str(i))[4] - SNOTEL.get(str(i))[-2])/SNOTEL.get(str(i))[-1], ".4f"))
        magnitudes.append(magnitude_station)
    
    
    plt.xticks(rotation=80)
    stat = plt.bar(values[:-1], magnitudes, color=['blue', 'blue', 'blue', 'blue', 'blue', 'orange', 'blue', 'blue', 'blue', 'blue', 'blue', 'orange', 'blue', 'orange', 'orange', 'blue','blue','orange','blue']), plt.axhline(1, linestyle = '-', color = 'black'), plt.axhline(0, linestyle = '-', color = 'black'), plt.ylabel('Distance in Station Standard Deviations'+'\n'+'from Station OLR La Niña Mean'), plt.title("SNOTEL Stations With OLR La Niña Means > 1 Standard Deviation"+'\n'+"Away From The Stations' Mean")
    return stat
    
stations = ['blewitt_pass', 'corral_pass', 'cougar_mountain', 'fish_lake', 'harts_pass', 'lone_pine', 'lyman_lake', 'olallie_meadows', 'park_creek', 'pigtail_peak', 'pope_ridge', 'potato_hill', 'rainy_pass', 'sheep_canyon', 'spencer_meadow', 'stampede_pass', 'stevens_pass','surprise_lakes', 'white_pass']
plotStdevAway(stations)
#%% What colors should the maps get?
def colorSort(tag):
        
        magnitudes = []
        magnitudec = []
        #stations = ['blewitt_pass', 'corral_pass', 'cougar_mountain', 'fish_lake', 'harts_pass', 'lone_pine', 'lyman_lake', 'olallie_meadows', 'park_creek', 'pope_ridge', 'potato_hill', 'rainy_pass', 'spencer_meadow', 'stampede_pass', 'surprise_lakes', 'white_pass']
        for i in stations:
        #print(i+"'s standard deviation:", SNOTEL.get(str(i))[-1]) # get the standard deviation
            magnitude_station = float(format((SNOTEL.get(str(i))[-2] - SNOTEL.get(str(i))[4])/SNOTEL.get(str(i))[-1], ".4f"))
            magnitudes.append(magnitude_station)
            magnitude_comp = float(format((SNOTEL.get(str(i))[-2] - 38.2387)/10.3890, ".4f"))
            magnitudec.append(magnitude_comp)
        
        if tag == 'stat':
            list = magnitudes
        if tag == 'comp':
            list = magnitudec
           
        j = 0
        for i in list:
            if i <= -2:
                print(stations[j], "- darkest orange shade 70,35,2")
            elif i >= -2 and i <= -1:
                print(stations[j], "- medium orange shade 95,64,25") 
            elif i >= -1 and i <= 0:
                print(stations[j], "-  lightest orange shade 100,88,17")
            elif i >= 0 and i <= 1:
                print(stations[j], "-  lightest purple shade 85,85,92")  
            elif i >= 1 and i <= 2:
                print(stations[j], "- medium purple shade 60,56,76")   
            elif i >= 2:
                print(stations[j], "- darkest purple shade 33,15,53")
            j += 1

tag = input("By Station or By Composite? (enter 'stat' or 'comp') ")
colorSort(tag)
#%% # absolute difference in OLR la Niña Mean SWE in inches
# OLR la niña mean:
def olrlnMeanComp():
    tag = int(input('Plot, Plot & Text, or Text? (enter 1, 2 or 3) '))
    if tag == 1:
        values = list(SNOTEL.keys())
        ks = []
        for key in values[:-1]:
            k = SNOTEL.get(str(key))[5] - SNOTEL.get(str(key))[7]  # match other lines to this one
            ks.append(k)
        plt.xticks(rotation=80)
        image = plt.bar(values[:-1], ks), plt.axhline(0, linestyle = '-', color = 'black'), plt.ylabel('Snow Water Equivalent in Inches'), plt.title("SNOTEL Stations OLR La Niña variations from La Niña Mean SWE in Inches")
        return image
   
    if tag == 2:
        values = list(SNOTEL.keys())
        ks = []
        for key in values[:-1]:
            k = SNOTEL.get(str(key))[5] - SNOTEL.get(str(key))[7]
            ks.append(k)
            print(key+"'s OLR la niña mean is", format(k, ".4f"), "inches higher than the la niña mean") 
        plt.xticks(rotation=80)
        image = plt.bar(values[:-1], ks), plt.axhline(0, linestyle = '-', color = 'black'), plt.ylabel('Snow Water Equivalent in Inches'), plt.title("SNOTEL Stations OLR La Niña variations from La Niña Mean SWE in Inches")
        return image

    if tag == 3:
        values = list(SNOTEL.keys())
        ks = []
        for key in values[:-1]:
            k = SNOTEL.get(str(key))[5] - SNOTEL.get(str(key))[7]
            ks.append(k)
            print(key+"'s OLR la niña mean is", format(k, ".4f"), "inches higher than the la niña mean") 
        
olrlnMeanComp()
#%% Compare previous 4 OLR La Niña year means with 2021 OLR LNM
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def avg(list):
    return sum(list)/len(list)

def yearlyComp(tag):
    
    tag = int(tag)
    values = list(SNOTEL.keys())
    four_list = []
    fifth_list = []
    comp_list = []
    total_list = []
    
    lists = [[18.6, 18.7, 13.8, 13.8], [39.3, 51.0, 37.9, 36.9], [32.3, 26.8, 20.2, 15.4], 
             [30.4, 55.0, 35.2, 30.8], [42.9, 69.7, 36.1, 57.3], [35.6, 84.5, 51.7, 55.2], 
             [60.1, 88.5, 60.8, 66.8], [60.2, 86.6, 56.1, 58.9], [49.5, 72.1, 49.5, 48.2],
             [70.0, 76.2, 48.1, 57.8], [16.1, 28.5, 18.8, 17.9], [28.2, 50.8, 35.4, 37.7],
             [34.8, 61.7, 38.5, 44.0], [65.6, 77.9, 51.7, 50.2], [39.7, 73.2, 49.9, 36.9],
             [48.8, 63.0, 50.5, 32.6], [50.9, 56.7, 42.6, 37.0], [61.3, 84.2, 63.8, 57.4],
             [21.1, 35.1, 25.1, 22.5]]
    
    means = [ 15.0, 42.8, 20.5, 40.9, 53.2, 47.2, 59.2, 64.1, 56.3, 55.5, 17.8, 39.8, 40.4,
             50.9, 33.3, 48.6, 55.6, 52.5, 32.5]
    
    for four_lnms in lists:
        four_mean = avg(four_lnms)
        four_list.append(four_mean)
        
    for fifth_lnm in means:
        fifth_list.append(fifth_lnm)
        
        i = means.index(fifth_lnm)
        use= [fifth_lnm]
        
        lists[i].extend(use)
        five_years = lists[i]
        #print(five_years)
        
        comp_list.append(fifth_lnm - four_list[i])
        
        total_avg = avg(five_years)
        total_list.append(total_avg)

    if tag == 1:
        plt.xticks(rotation=80)
        four_image = plt.bar(values[:-1], four_list, color = 'green'), plt.yticks(np.arange(0, 80, step=10)), plt.ylabel('Snow Water Equivalent in Inches'), plt.title("1989, 1999, 2000, 2011 OLR La Niña Year")
        return four_image
    
    if tag == 2:
        plt.xticks(rotation=80)
        fifth_image = plt.bar(values[:-1], fifth_list, color = 'green'), plt.yticks(np.arange(0, 80, step=10)), plt.ylabel('Snow Water Equivalent in Inches'), plt.title("2021 OLR La Niña Year")
        return fifth_image
    
    if tag == 3:
        plt.xticks(rotation=80)
        comp_image = plt.bar(values[:-1], comp_list, color = 'green'), plt.yticks(np.arange(-20, 20, step=5)), plt.axhline(0, linestyle = '-', color = 'black'), plt.ylabel('Snow Water Equivalent in Inches'), plt.title("Change in SWE in Inches from [1989, 1999, 2000, 2011]-average to 2021")
        return comp_image
    
    if tag == 4:
        plt.xticks(rotation=80)
        total_image = plt.bar(values[:-1], total_list, color = 'green'), plt.yticks(np.arange(0, 80, step=10)), plt.ylabel('Snow Water Equivalent in Inches'), plt.title("All-Year OLR La Niña: [1989, 1999, 2000, 2011, 2021]")
        return total_image
        
tag = input("1. First 4 years OLR La Niña SWE"+'\n'+"2. 2021 OLR La Niña SWE"+'\n'+"3. Change in SWE from first four years to 2021 OLR La Niña SWE"+'\n'+"4. All-year OLR La Niña SWE"+'\n'+"Enter 1, 2, 3 or 4: ")
yearlyComp(tag)
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
"""
# OLR el niño mean:
print("OLR el niño mean is", format(abs((SNOTEL.get(str(key))[-2] - SNOTEL.get(str(key))[2])/SNOTEL.get(str(key))[-1]), ".4f"), "standard deviations away from the mean")

# la niña mean:
print("la niña mean is", format(abs((SNOTEL.get(str(key))[-2] - SNOTEL.get(str(key))[5])/SNOTEL.get(str(key))[-1]), ".4f"), "standard deviations away from the mean")

# el niño mean:
#print("el niño mean is", format(abs((SNOTEL.get(str(key))[-2] - SNOTEL.get(str(key))[3])/SNOTEL.get(str(key))[-1]), ".4f"), "standard deviations away from the mean")
"""
