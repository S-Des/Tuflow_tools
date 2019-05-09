inputFilename = raw_input("file path for .DAT to extract sections from:")
outputFilePath = raw_input("output folder path please:")+'\\'



with open(inputFilename) as f:
    content = f.readlines()

    sectionHeaders = []

    for index,line in enumerate(content):
        if line.startswith("SECTION"):
            sectionHeaders.append(index)



    lines = list(content)


    for sectionHeaderLine in sectionHeaders:
        sectionIndex = sectionHeaderLine
        numberofSectionPoints = int(lines[sectionIndex+3]) # gets number of lines with section data in
        sectionlableIndex = sectionIndex+1# get the index of the line with the section label on it
        firstlinetoCopy = sectionIndex+4# get the first line of section data
        lastlinetoCopy = firstlinetoCopy+numberofSectionPoints# last line of section data = first line + number of lines
        linestoCopy = range(firstlinetoCopy, lastlinetoCopy)# create a list with the index range of these lines
        OutputCSVLines = []
        OutputCSVLines.append(lines[sectionlableIndex])
        csvColumnHeaderString = 'x,z,n,\n'# add a line with the ESTRY csv column headers
        OutputCSVLines.append(csvColumnHeaderString)
        for i in linestoCopy:# take each line, put commas in and remove FMP idiosyncrasies 
            originalLine = lines[i]#opens a line
            size = 10# we want to put a comma every 10 spaces based on standard .DAT formatting
            parts = [originalLine[i:i+size] for i in range(0, len(originalLine), size)]#split the line into sections of 10
            commaLine = (','.join(parts) + ',')  #afix part of the line to a comma and then add a comma
            commaLine = commaLine.strip(' ')#remove all spaces
            commaLine = commaLine[:-1]#drop an additional , off the end of the line.
            OutputCSVLines.append(commaLine)
        print OutputCSVLines
        sectionName = lines[sectionIndex+1]
        sectionNametrim = sectionName.rstrip('\r\n')
        outputFilename = outputFilePath+sectionNametrim+'.csv'
        output = open(outputFilename,'w')
        for CSVline in OutputCSVLines:
            output.write(CSVline)
        output.close()
        
            

            
        
            


    #write to file


        
