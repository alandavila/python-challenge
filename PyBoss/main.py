import os
import csv

def parse_a_row(row):
    return ['a']

#Loop over files to analyze.
all_files = os.listdir()
all_csv_files = []

#open an output file stream
outfile = open('new_records.csv', 'w', newline='')
#add a csv writer
csv_writer = csv.writer(outfile, delimiter=',')

for afile in all_files:
    if afile.endswith('csv'):
        all_csv_files.append(afile)
        #analyze file here
        with open(afile, 'r', newline='') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            for row in csv_reader:
                print(row)
                #csv_writer.writerow(row)
#close outpuf file
outfile.close()
