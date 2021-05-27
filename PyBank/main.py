#Dependencies
import os
import csv
from statistics import mean

#Define the Location
bank_csv = os.path.join("..","PyBank","Resources","budget_data.csv")

#initialize variable to hold total number of months in the data
num_months = 0

#inititalize variable to hold the net total amount of "Profit/Losses" over the entire period
net_total = 0

#initialize list to hold the calculated changes in "Profit/Losses" over the entire period
change_pl = []

#Open and read csv
with open(bank_csv, encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #converting the data set into a list for easier manipulation
    list_of_rows = list(csv_reader)
   
    #iterating list to calculate net total and changes in Profit/Lossess, starting at 1 because 0 is header
    for i in range(1,len(list_of_rows)):
        #cummulative total of Profit/Losses
        net_total += int(list_of_rows[i][1])

        #calculating and adding changes to change_pl list to later calculate average change
        # only executing till i+1 is less than size of data
        if i+1 < len(list_of_rows):
            change_pl.append ( int(list_of_rows[i+1][1]) - int(list_of_rows[i][1]))

    #preparing to print results
    line_break = "-------------------------"
    results_print = ("Financial Analysis\n"
                      f"{line_break}\n"
                      f"Total Months: {(len(list_of_rows))-1}\n"
                      f"Total: ${net_total}\n"
                      f"Average Change: ${'{:.2f}'.format(mean(change_pl))}\n"
                      f"Greatest Increase in Profits: {list_of_rows[(change_pl.index(max(change_pl)))+2][0]} (${max(change_pl)})\n"
                      f"Greatest Decrease in Profits: {list_of_rows[(change_pl.index(min(change_pl)))+2][0]} (${min(change_pl)})\n"                   
                     )
    print(results_print)                 

    # Specify the file to write to
    output_path = os.path.join("..","PyBank","Analysis","results_PyBank.txt")
    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as f:
        f.writelines(results_print)
