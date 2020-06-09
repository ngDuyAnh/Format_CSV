# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:58:26 2019
Format Data Feeder
@author: Duy Anh
"""

# Instruction to format data
keepCol = (0,1,2,3,4,5,6,7,8) # The columns of data that we want to keep - zero-index!

# File path
dataFrom_csv = "flightComputer_data_unfiltered.csv" # File to read and format from
dataTo_csv = "flightComputer_data_filtered.csv"     # FIle to write the formated data to in .csv

# Enable the ability to input file name or path
changeFile = False
if changeFile:
    dataFrom = str(input("Read from: "))  # Get file to read for format
    dataTo = str(input("Format to: "))    # Get the file to write the formatted data to
    
    # Set the read and write file
    dataFrom_csv = dataFrom + ".csv"
    dataTo_csv = dataTo + ".csv"

# Format the data read from csv (dataFrom_csv) and write to csc (dataTo_csv)
getData = open(dataFrom_csv, 'r') # Get pointer to the file for read
writeData = open(dataTo_csv, 'w') # Get pointer to the file for write
for line in getData:
    line = line.strip()    # Clear any whitespace
    line = line.split(',') # Get column value separate by comma ','
    
    # Get the data that we want to write
    dataStr = ""
    for index in keepCol:
        dataStr = dataStr + line[index] + ','
    # Remove and replace the last comma to '\n'
    dataStr = dataStr[:len(dataStr) - 1] + '\n'
    
    # Write the desire column to dataTo_csv
    writeData.write(dataStr)
    
# Close file
getData.close()
writeData.close()    

# Print status done
print("Finish separate the desired data!")
input("END!")