# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 12:45:41 2016

@author: simon.desmet
"""

# read in a csv file, 
#identify line 1 of the time series data,
# ask user for current time step and desired timestep
#delete additional timesteps (rows) down to desired timestep - auto save output

#if possible do it entirely in CORE.



import os # a module that allows os commands
import glob # a module that allows python to recognise specific file extentions

#-----------------------------------------------------------------------

PATH1 = raw_input('path?')

print "is this correct?"
print PATH1


 

INPUTPATH = PATH1

#-----------------------------------------------------------------------

currentTS = 0.08333

CTS = float(currentTS)
# asks user for decimal input, converts to float from string.

print CTS
#-----------------------------------------------------------------------


newTS = 0.25

NTS = float(newTS)


print NTS

# asks user for new time step and converts to float.



#-----------------------------------------------------------------------



startline = int(2)


print startline

# asks for starting line for process, and converts it to an integer.



#-----------------------------------------------------------------------

# now we determine how what lines need to be deleted

save = NTS/CTS

saveno = int(save)

# takes the new time step then divides it by the old to get the line number we want to save.
# we then create a new list of lines from the old but only with the lines of thi





#-----------------------------------------------------------------------

# now we read in the file & operate

with open(INPUTPATH) as f: # open the file at our input path
    content = f.readlines() # read file into variable content

    
lines = list(content)
print startline
linesstart = lines[startline:] # trims everything off before the startline
print startline
header = lines[0:startline] # saves the lines before the start line to new header list
newlines = linesstart[::saveno] # copys every X line into new list called newlines, where x is our saveno line that we want to keep
print newlines
finallines = header+newlines #new list that sticks our header to our new timestep lines
    

            


#-----------------------------------------------------------------------

# now we write the output.

#for inputfile in inputlistB: # creates new varible 'inputfile' from each item in list inputlistB
 #   with open(inputfile) as f: # with - so does what follows with this line in effect, opens file as f
#        content =f.readlines() # creates new varible 'content' and reads entire file into it.
  #      print content

ppos = PATH1.index('.')


PATHA = PATH1[0:ppos]
PATHB = PATH1[ppos:]

OUTPUTPATH = PATHA+'_NEWTS'+PATHB

output = open(OUTPUTPATH,'w')
for line in finallines:
    output.write(line)
output.close()
