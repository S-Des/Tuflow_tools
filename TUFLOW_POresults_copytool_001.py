# -*- coding: utf-8 -*-
"""
Created on Mon Mar 04 11:32:54 2019

@author: Simon.Desmet
"""

import os # a module that allows os commands
import pandas as pd

POsavefldr  = raw_input("PO results folder path please:")

os.chdir(POsavefldr)#sets the path for working folder to current directory

os.getcwd()#prints current directory to see if the above has worked.



filelist =  raw_input("results list file path:") # txt file with a list of the files we are interested in.

resultslist = open(filelist).readlines() # reads list out of txt file and saves as a list
resultslist = resultslist[:-1] # !!!!trim the final blank line off the list. !!! note if there is no blank line at bottom of the list, this will drop last file in list!
print resultslist




#open first results csv, get number of rows and time series and copy to new blank database
fst = resultslist[1].rstrip() # finds 1st csv file name in list and strips off the /n
fstcsv = pd.read_csv(fst, header=1) # open first csv and trim first csv to header row
timeseries = fstcsv[['Time']] # strips down frstcsv to just the timeseries column
collectedDF = timeseries # creates are base dataframe as a copy of the time series dataframe


#collectedresults = pd.DataFrame(index=fstcsv.index) # creates a new dataframe with rows equal to first csv





# get column headers to be copied from user
nocolumns = raw_input('how many columns to copy:') # asks user how many individual colummns they want to copy from each results file
counts = int(nocolumns) # puts the above into an interger as counts

cheaderlist = [] # blank list for column headers
for x in range(0,counts): # asks user for column header strings. one for each number specified above
   cheader = raw_input('column header:')
   cheaderlist.append(cheader)



#open each file in list, load CSV as dataframe copy desired column into collectedresults

for csvfile in resultslist:
    item = (csvfile).rstrip()#strips the /n fromt the file name
    csv1 = pd.read_csv(item, header=0) # open csv file as pandas table csv1 with first 5 lines ignored and line 6 as header
    csv2 = csv1.filter(like='Flow', axis=1)
    # remame headers to with node label
    headerlist = list(csv2.columns.values)# creates a list with the current headers in it
    row1list =  csv2[0:1].values.tolist()# creates a list with the row 0, due to coding method it is a list within a list, hence next line
    row1 = row1list[0]
    newheaders = []#empty list for new headers
#    for x in row1:#takes list of names from row1 and iterates through it adding string from headerlist and '_' before saving to new empty list
#        counter = 0
#        y = headerlist[counter]
#        x = y+'_('+x+')'
#        newheaders.append(x)
#        counter = counter+1
    csv2.columns = row1 # relabels all columns to row1 names
    #pop row 1
    csv3 = csv2[1:] # drops first row of dataframe
    for H in cheaderlist:# for header in list of headers created
        df1 = csv3[[H]]#strips dataframe down to single column
        df1.columns = [H+'-'+item[:-4]] # rename the column to H - header + csv file name minus extension
        joinedDF = collectedDF.join(df1, how='left') # .join joins the existinc collectedDF to the df1 table based on left index i think
        collectedDF = joinedDF # makes collectedDF

collectedDF.to_csv(path_or_buf=POsavefldr+'\\'+cheaderlist[1]+'to'+cheaderlist[-0]+'.csv', sep=',')
    
