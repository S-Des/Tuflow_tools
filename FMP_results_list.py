# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 11:04:02 2019

@author: Simon.Desmet
"""

# list all results files in folder - save to list text file for user to manually edit


import os # a module that allows os commands
import glob # a module that allows python to recognise specific file extentions
import datetime


FMPsavefldr  = raw_input("FMP 1D results folder path please:")

os.chdir(FMPsavefldr)#sets the path for working folder to current directory

os.getcwd()#prints current directory to see if the above has worked.


FMPresultsList = []

    
for filename in glob.glob('*.csv'): #defines new variable 'filename'loops through workingfolder and adds each 'filename' with .dat in it to listB
    print filename
    FMPresultsList.append(filename)
    

current_date = datetime.datetime.now().date()
date = str(current_date)
OUTPUTPATH = FMPsavefldr+"\\"+date+'_resultslist.txt'

output = open(OUTPUTPATH,'w')
for line in FMPresultsList:
    output.write(line)
    output.write("\n")
output.close()