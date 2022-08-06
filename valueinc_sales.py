#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:40:19 2022

@author: ayodejifalokun
"""

#use pip pandas readcsv to read the csv file
#pip used to install packages
#windows
#right click anaconda prompt as admin
#pip install pandas
#mac
#terminal
#pip install pandas

import pandas as pd
# file_name = pd.read_csv('file.csv')    <--- format of read_csv

#data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')

#get your data into a dataframe generally in python

#summary of the data
data.info()

#Python data types
# test = str, object
# numeric = int, float

#playing around with variables
var = ['apple','pear','banaa']
vartuple =  ('apple','pear','banaa')
varr = range(14)
varjson = {'name':'John Doe','location':'london'}
var = {'apple','pear','banaa'}
varl= True
print(varl)

#working with calculations
#defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#MMathOperations
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction= (SellingPricePerItem - CostPerItem) * NumberOfItemsPurchased
