#Dependencies
import os
import csv
from statistics import mean
from collections import Counter

#Define the Location of file to be analyzed
election_csv = os.path.join("..","PyPoll","Resources","election_data.csv")

#initialize list to store candidate names
candidates_list=[]

#Open and read csv
with open(election_csv, encoding='utf-8-sig') as csv_file:
    
    #convert csv to a list of dictionaries for easier manipulation
    election_rows=csv.DictReader(csv_file)

    #iterating list of dictionaries for extract Candidat Names in a separate list
    for row in election_rows:
        candidates_list.append(row['Candidate'])
 
    #using counter from collections module to store unique candidate list in a dictionary with the total number of votes received by each
    counter_dict=Counter(candidates_list)

    #using sum function to calculate sum of all the values in the unique candidate list dictionary 
    total_votes=sum(counter_dict.values())

    #preparing to print results
    line_break = "-------------------------"
    results_print = ("Election Results\n"
                      f"{line_break}\n"
                      f"Total Votes: {total_votes}\n"
                      f"{line_break}\n"
                     )
    
    #looping through counter dict items to extract keys and values and use them to calculate percentage votes and display alongside
    for key, value in counter_dict.items():
        per_value= '{:.3f}%'.format(value/total_votes*100)
        #appending to results_print to add results to the string
        results_print += f"{key}: {per_value} ({value})\n"

    results_print += f"{line_break}\n"   
    #using most common function form collections module, identifying which candidate received the most votes 
    results_print += f"Winner: {counter_dict.most_common(1)[0][0]}\n"
    results_print += f"{line_break}\n"    

    print(results_print)


    # Specify the file to write to
    output_path = os.path.join("..","PyPoll","Analysis","results_PyPoll.txt")
    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as f:
        f.writelines(results_print)

     