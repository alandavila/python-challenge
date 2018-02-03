import os
import csv
import datetime

states = {
    'Utah' : 'UT' ,
    'North Carolina' : 'NC' ,
    'Arizona' : 'AZ' ,
    'Virgin Islands' : 'VI' ,
    'Kentucky' : 'KY' ,
    'Minnesota' : 'MN' ,
    'New Hampshire' : 'NH' ,
    'Maine' : 'ME' ,
    'Alaska' : 'AK' ,
    'Texas' : 'TX' ,
    'New York' : 'NY' ,
    'Arkansas' : 'AR' ,
    'Delaware' : 'DE' ,
    'Indiana' : 'IN' ,
    'New Jersey' : 'NJ' ,
    'West Virginia' : 'WV' ,
    'Wisconsin' : 'WI' ,
    'Kansas' : 'KS' ,
    'Alabama' : 'AL' ,
    'Florida' : 'FL' ,
    'Ohio' : 'OH' ,
    'District of Columbia' : 'DC' ,
    'California' : 'CA' ,
    'Northern Mariana Islands' : 'MP' ,
    'National' : 'NA' ,
    'Georgia' : 'GA' ,
    'Missouri' : 'MO' ,
    'Vermont' : 'VT' ,
    'Massachusetts' : 'MA' ,
    'Oklahoma' : 'OK' ,
    'South Carolina' : 'SC' ,
    'Montana' : 'MT' ,
    'Mississippi' : 'MS' ,
    'North Dakota' : 'ND' ,
    'Illinois' : 'IL' ,
    'Puerto Rico' : 'PR' ,
    'Nebraska' : 'NE' ,
    'Pennsylvania' : 'PA' ,
    'Oregon' : 'OR' ,
    'Colorado' : 'CO' ,
    'Guam' : 'GU' ,
    'South Dakota' : 'SD' ,
    'Washington' : 'WA' ,
    'Virginia' : 'VA' ,
    'Connecticut' : 'CT' ,
    'Rhode Island' : 'RI' ,
    'Hawaii' : 'HI' ,
    'American Samoa' : 'AS' ,
    'Michigan' : 'MI' ,
    'Iowa' : 'IA' ,
    'Idaho' : 'ID' ,
    'Maryland' : 'MD' ,
    'Wyoming' : 'WY' ,
    'Louisiana' : 'LA' ,
    'Tennessee' : 'TN' ,
    'Nevada' : 'NV' ,
    'New Mexico' : 'NM' 
}

def parse_a_row(row):
    #check for header and ignore it
    ID, Name, DOB, SSN, State = row
    if ID == 'Emp ID':
        return None
    #Name has format of : John Doe
    first_name, last_name = Name.split(' ')
    #DOB has format of YYYY-MM-DD
    # split YYYY, MM and DD, then use map to convert to integers, convert the result to a list
    #finally use * to feed the list to datetime.date element-wise
    dob = datetime.date( *list(map(int,DOB.split('-')) ) )
    #now convert dob to the desired format
    dob = dob.strftime("%m/%d/%y")
    #hide first 5 numbers of sss and just grab las four
    ssn = '***-**-' + SSN.split('-')[-1]
    return ID, first_name, last_name, dob, ssn, states[State]

#Get a list of all data files to read located in folder 'data'
all_files = os.listdir('data')

#Open an output file to gather our results
outfile = open(os.path.join('output','new_records.csv'), 'w', newline='')
#Add a csv writer
csv_writer = csv.writer(outfile, delimiter=',')
#add header
csv_writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

#Loop over all files to parse
for afile in all_files:
    #Need to add the path to file before we open it
    afile = os.path.join('data',afile)
    if afile.endswith('csv'):
        #Analyze file here
        with open(afile, 'r', newline='') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            for row in csv_reader:
                parsed_row = parse_a_row(row)
                #check for header here 
                if parsed_row:
                    csv_writer.writerow(parsed_row)
#Close outpuf file
outfile.close()
