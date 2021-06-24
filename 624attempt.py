#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:09:17 2021

@author: skilpatrick
"""
#import pandas as pd

with open('spencer_meadow.dat') as f:
    print([line.split()[-1] for line in f])
    

#corral['per_pupil_spending'].fillna(corral['per_pupil_spending'].mean(), inplace = True)