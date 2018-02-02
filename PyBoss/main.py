import os
import csv

def parse_a_row(row):
    return ['a']

#Get a list of all data files to read
all_files = os.listdir('data')

#Open an output file to gather our results
outfile = open(os.path.join('output','new_records.csv'), 'w', newline='')
#Add a csv writer
csv_writer = csv.writer(outfile, delimiter=',')

#Loop over all files to parse
for afile in all_files:
    #Need to add the path to file before we open it
    afile = os.path.join('data',afile)
    if afile.endswith('csv'):
        #Analyze file here
        with open(afile, 'r', newline='') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            for row in csv_reader:
                csv_writer.writerow(parse_a_row(row))
#Close outpuf file
outfile.close()
