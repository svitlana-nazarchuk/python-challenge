#import necessary libraries
import os
import csv

# Create path to the data file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data_csv = os.path.join('budget_data.csv')



#open csv file with data
with open(budget_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header
    csv_header = next(csvreader)

    second_row = next(csvreader)
    
    #initialise variables
    month_total=1
    total_lp=int(second_row[1])
    beg_lp=int(second_row[1])
    total_change=0
    gr_incr=0
    gr_decr=0

    
    for row in csvreader:

        #calculate total number of months
        month_total=month_total + 1
        #calculate total profits/losses
        total_lp=total_lp + int(row[1])
        #calculate total change in profits/losses from month to month
        change=int(row[1]) - beg_lp
        total_change=total_change + change
        
        #find the month with the greatest increase in profit
        if (change > gr_incr):
            gr_incr = change
            gr_month = row[0]

        #find the month with the greatest decrease in profit
        if (change < gr_decr):
            gr_decr = change
            low_month = row[0]

        beg_lp=int(row[1])

    #find the average change in profit
    average_change = total_change/(month_total-1)
    average_change = format(average_change, ".2f")
 

    #print results to the screan
    print("Financial Analysis")
    print("--------------------------------------------------------")
    print(f"Total Months: {month_total}")
    print(f"Total: ${total_lp}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {gr_month} (${gr_incr})")
    print(f"Greatest Decrease in Profits: {low_month} (${gr_decr})")
    print("--------------------------------------------------------")

#create and open file for the output of the results   
budget_data_output = os.path.join('budget_data_output.txt')
with open(budget_data_output,"w") as output:
    
    #print results to the output file
    print("Financial Analysis", file=output)
    print("--------------------------------------------------------", file=output)
    print(f"Total Months: {month_total}", file=output)
    print(f"Total: ${total_lp}", file=output)
    print(f"Avetage Change: ${average_change}", file=output)
    print(f"Greatest Increase in Profits: {gr_month} (${gr_incr})", file=output)
    print(f"Greatest Decrease in Profits: {low_month} (${gr_decr})", file=output)
    print("--------------------------------------------------------", file=output)

