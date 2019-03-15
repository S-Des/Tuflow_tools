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


#TUFLOW = raw_input("TUFLOW.exe path:")#gets path of TUFLOW 
TUFLOW = r"C:\TUFLOW\w64\TUFLOW_iDP_w64.exe"#gets path of TUFLOW



#get path to working folder


runsfolder = raw_input("Tuflow runs folder path:")#get the results folder we are working in


# in this version of the program we will take all .dat, later we may add options for just h, v, d or 100year etc

os.chdir(runsfolder)#sets the path for working folder to current directory

os.getcwd()#prints current directory to see if the above has worked.

modelversion = raw_input("Model version number/ID:")

tcfpath=''
# get correct TCF

for filename in glob.glob('*.tcf'):#defines new variable 'filename'loops through workingfolder and adds each 'filename' with .dat in it to listB
    if modelversion in filename: 
        tcfpath = filename
    else:
        continue

print tcfpath


#get batch scenario

scenario = raw_input("scenario?")


#get events

eventlines = []

for filetef in glob.glob('*.tef'):
    with open(filetef) as tef:
        tefcontent =tef.readlines()
        for line in tefcontent:
            if "Define Event" in line: 
                eventlines.append(line)
            else: 
                continue
        

events = []
for x in eventlines:
    y = x.split('==')
    z = y.strip(' ')
    events.append(z)

print events
    
    

batchlines = []

for returnperiod in events: # creates new varible 'inputfile' from each item in list inputlistB
    line = '%RUN64% '+'-s '+scenario+'-e '+returnperiod+'-b '+tcfpath
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
output.write('set TUFLOWEXE64='+TUFLOW)
output.write(r'set RUN64=start "TUFLOW" /low /wait /min "%TUFLOWEXE64%" -b')
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