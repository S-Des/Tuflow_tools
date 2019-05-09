# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:56:32 2019

@author: simon.desmet
"""

# FMP to bank line extractor

inputFilename = raw_input("file path for .DAT to extract sections from:")
outputFilePath = raw_input("output folder path please:")+'\\'

leftrightLines = []
OutputCSVLines = []

with open(inputFilename) as f:
    content = f.readlines()
    lines = list(content)
    for line in lines:
        if 'left' in line:
            leftrightLines.append(line)
        elif 'right' in line:
            leftrightLines.append(line)
        else:
            continue
            

    for a in leftrightLines:
        originalLine = a#opens a line
        size = 10# we want to put a comma every 10 spaces based on standard .DAT formatting
        parts = [originalLine[i:i+size] for i in range(0, len(originalLine), size)]#split the line into sections of 10
        commaLine = (','.join(parts) + ',')  #afix part of the line to a comma and then add a comma
        commaLine = commaLine.strip(' ')#remove all spaces
        commaLine = commaLine[:-1]#drop an additional , off the end of the line.
        commaLineBits = commaLine.split(',')
        commaLineBits2 = []
        for bit in commaLineBits:
            bit.strip(' ')
            commaLineBits2.append(bit)
        OutputCSVLines.append(commaLine)

        outputFilename = outputFilePath+'test'+'.csv'
        output = open(outputFilename,'w')
        for CSVline in OutputCSVLines:
            output.write(CSVline)
        output.close()