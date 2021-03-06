#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:09:17 2021

@author: skilpatrick
"""
#%% Get last row of each .dat file 

with open('spencer_meadow.dat') as f:
    print([line.split()[-1] for line in f])

#%% create a file for the means

"""
blewitt_pass 
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 13.1600
noenm = 10.0333
lnm = 15.9800
nolnm = 15.7800
mn = 13.2200
stdev = 5.5312

corral_pass
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 32.3400
noenm = 29.0500
lnm = 41.5800
nolnm = 31.6600
mn = 33.4024
stdev = 9.5579

cougar_mountain
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 8.1800
noenm = 7.7833
lnm = 23.0400
nolnm = 24.7000
mn = 15.9333
stdev = 10.7980

fish_lake
ln = [1989, 1999, 2000, 2011, 2021]
noln = [1985, 1996, 2001, 2008, 2012]
enm = 25.5250
noenm = 24.7000
lnm = 38.4600
nolnm = 33.3400
mn = 29.6098
stdev = 10.2354

harts_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 43.0600
noenm = 36.9833
lnm = 51.8400
nolnm = 42.1800
mn = 43.3872
stdev = 11.6386

lone_pine
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 31.3200
noenm = 27.1667
lnm = 54.8400
nolnm = 40.6600
mn = 37.0220
stdev = 17.4157

lyman_lake
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 60.9250
noenm = 56.2667
lnm = 67.0800
nolnm = 54.9000
mn = 57.7500
stdev = 13.3331

olallie_meadows
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 47.0200
noenm = 43.0667
lnm = 65.1800
nolnm = 59.0600
mn = 51.6564
stdev = 17.4086

park_creek
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 47.0000
noenm = 39.1167
lnm = 55.1200
nolnm = 46.7200
mn = 44.5651
stdev = 13.0535

pope_ridge
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 15.0600
noenm = 15.6167
lnm = 19.8200
nolnm = 18.0800
mn = 15.8825
stdev = 5.6001

potato_hill
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 21.4500
noenm = 21.9833
lnm = 38.3800
nolnm = 31.5000
mn = 28.0500
stdev = 10.3187

rainy_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 39.7200
noenm = 34.4167
lnm = 43.8800
nolnm = 39.6600
mn = 38.4667
stdev = 10.0855

sheep_canyon
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 24.3250
noenm = 23.2667
lnm = 59.2600
nolnm = 42.4400
mn = 36.6421
stdev = 18.8327

spencer_meadow
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 24.8400
noenm = 22.0667
lnm = 46.6000
nolnm = 35.4250
mn = 30.3053
stdev = 15.7588

stampede_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 35.7600
noenm = 32.3167
lnm = 48.7000
nolnm = 44.6600
mn = 39.5949
stdev = 14.4252

stevens_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 31.3800
noenm = 32.7667
lnm = 48.5600
nolnm = 39.5000
mn = 37.7293
stdev = 12.9577

surprise_lakes
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 44.6000
noenm = 35.2667
lnm = 63.8400
nolnm = 48.7200
mn = 46.0167
stdev = 17.1828

white_pass
ln = [1989, 1999, 2000, 2011,2021]
noln = 1985, 1996, 2001, 2008, 2012]
enm = 21.3400
noenm = 17.4500
lnm = 27.2600
nolnm = 23.8400
mn = 22.4125
stdev = 7.4027
"""