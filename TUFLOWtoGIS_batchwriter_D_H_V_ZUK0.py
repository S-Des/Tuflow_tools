# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 18:46:03 2016

@author: simon.desmet
"""

#asci batch writer

# program for opening a folder, reading all file names, 
# identifying the correct dat files and writing a batch file to post process them.

import os # a module that allows os commands
import glob # a module that allows python to recognise specific file extentions
import datetime
import sys
# get path for TUFLOWGIS


TUFLOWGIS = raw_input("TUFLOWGIS.exe path:")#gets path of TUFLOW to GIS.exe from user


 

#get path to working folder


workingfolder = raw_input("Working/results folder path:")#get the results folder we are working in


# in this version of the program we will take all .dat, later we may add options for just h, v, d or 100year etc

os.chdir(workingfolder)#sets the path for working folder to current directory

os.getcwd()#prints current directory to see if the above has worked.


# id files to post process - read in just the files i need using glob
#PATH1 = raw_input("folder path please:") # sometimes this commented out to save time
  # my default path when not asking user for an input


inputlistB = []

    
for filename in glob.glob('*h.dat'): #defines new variable 'filename'loops through workingfolder and adds each 'filename' with .dat in it to listB
    print filename
    inputlistB.append(filename)
    
for filename in glob.glob('*v.dat'):#defines new variable 'filename'loops through workingfolder and adds each 'filename' with .dat in it to listB
    print filename
    inputlistB.append(filename)
    
for filename in glob.glob('*d.dat'):#defines new variable 'filename'loops through workingfolder and adds each 'filename' with .dat in it to listB
    print filename
    inputlistB.append(filename)

for filename in glob.glob('*ZUK0.dat'):#defines new variable 'filename'loops through workingfolder and adds each 'filename' with .dat in it to listB
    print filename
    inputlistB.append(filename)


print inputlistB#checks that all files we want are in list by printing them

#-------------------------------------------------------------------------
#perform operation on files listed in list

batchlines = []

for filename in inputlistB: # creates new varible 'inputfile' from each item in list inputlistB
    line = TUFLOWGIS+' -b'+' -asc'+' -max '+filename
    linestr = str(line)
    batchlines.append(linestr)
    
print batchlines
# with list of files, create new list with only 'X.dat' files retained


# create new file



# for loop over list of file names writing a batch line for each.

# save the resulting batch file.


current_date = datetime.datetime.now().date()
date = str(current_date)
OUTPUTPATH = workingfolder+"\\"+date+'_process.bat'

output = open(OUTPUTPATH,'w')
for line in batchlines:
    output.write(line)
    output.write("\n")
output.close()




# run the batch?

#YESNO = raw_input("Do you want to run the batch? TYPE 'Y' or 'N':")
#print YESNO

#if "Y" or "y" in YESNO:
#    from subprocess import Popen
#    p = Popen(OUTPUTPATH)
#    stdout, stderr = p.communicate()
#else:
 #   sys.exit(0)
#