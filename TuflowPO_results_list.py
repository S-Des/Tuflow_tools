# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 11:04:02 2019

@author: Simon.Desmet
"""

# list all results files in folder - save to list text file for user to manually edit


import os # a module that allows os commands
import glob # a module that allows python to recognise specific file extentions
import datetime


POsavefldr  = raw_input("PO line results folder path please:")

os.chdir(POsavefldr)#sets the path for working folder to current directory

os.getcwd()#prints current directory to see if the above has worked.


POresultsList = []

    
for filename in glob.glob('*PO.csv'): #defines new variable 'filename'loops through workingfolder and adds each 'filename' with .dat in it to listB
    print filename
    POresultsList.append(filename)
    

current_date = datetime.datetime.now().date()
date = str(current_date)
OUTPUTPATH = POsavefldr+"\\"+date+'_POresultslist.txt'

output = open(OUTPUTPATH,'w')
for line in POresultsList:
    output.write(line)
    output.write("\n")
output.close()