import os
import csv

#Dictionary to accumulate the votes of each candidate
votes_dict = {}

def get_vote(data_row, votes_dict):
    '''
    function that extracts voter data from a row and aggegates
    each candidates votes in a dictionary
    '''
    voter_id, county, candidate = data_row
    
    if voter_id != 'Voter ID':
        if candidate in votes_dict:
            votes_dict[candidate] = votes_dict[candidate] + 1
        else:
            votes_dict[candidate] = 1

def summarize_election(votes_dict):
    '''
    function that prints the election results to the screen
    '''
    #get total votes
    total_votes = 0
    winner_votes = 0
    winner = ''
    for k, v in votes_dict.items():
        total_votes  = total_votes + v
        if v > winner_votes:
            winner_votes = v
            winner = k
    #list candidate name, vote percentage, total votes
    print('Election Results')
    print('-------------------------')
    print('Total Votes: {}'.format(total_votes))
    print('-------------------------')
    for k, v in votes_dict.items():
        print('{}: {:,.2f}% ({})'.format(k,v/total_votes,v))
    #declate winner
    print('-------------------------')
    print('Winner: {}'.format(winner))
    print('-------------------------')

def write_results(votes_dict, outfile):
    '''
    function that saves the election results to a text file
    outfile is open/close this function in the current implementation
    '''
    #get total votes
    total_votes = 0
    winner_votes = 0
    winner = ''
    for k, v in votes_dict.items():
        total_votes  = total_votes + v
        if v > winner_votes:
            winner_votes = v
            winner = k
    #list candidate name, vote percentage, total votes
    outfile.write('Election Results\n')
    outfile.write('-------------------------\n')
    outfile.write('Total Votes: {}\n'.format(total_votes))
    outfile.write('-------------------------\n')
    for k, v in votes_dict.items():
        outfile.write('{}: {:,.2f}% ({})\n'.format(k,v/total_votes,v))
    #declate winner
    outfile.write('-------------------------\n')
    outfile.write('Winner: {}\n'.format(winner))
    outfile.write('-------------------------\n')

#Get a list of all files to analyze
files_path = os.listdir('data')
#create a file to gather our analysis results
output_file = os.path.join('output','electon_results.txt')
outfile = open(output_file, 'w', newline='')
#Create a csv writer
csv_writer = csv.writer(outfile, delimiter=',')
for file in files_path:
    file = os.path.join('data',file)
    #read the file to acccess its contents
    with open(file, 'r', newline='') as infile:
        #Create a csv reader
        csv_reader = csv.reader(infile, delimiter=',')
        for row in csv_reader:
            #use a function to accumulate votes per candidate on a dictionary
            get_vote(row, votes_dict)
#print results to terminal
summarize_election(votes_dict)
#Write results to txt file
write_results(votes_dict, outfile)
#Must close file if not use inside 'with ...'
outfile.close()
    