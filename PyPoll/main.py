#import necessary libraries
import os
import csv


#pass to data file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
poll_data_csv = os.path.join('election_data.csv')

#open csv file to read from row by row
with open(poll_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    csvheader=next(csvreader)

    #initialise variables for total number of votes, list of candidate names, 
    #and list of votes for corresponding candidates
    total_votes=0
    candidate_names=[]
    candidate_votes =[]
  
   #search row by row to find the total votes, build the list of candidates,
   #build the list of corresponding votes for each candidate
    for row in csvreader:
        
        total_votes=total_votes + 1
            
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            candidate_votes.append(0)
        
        candidate_votes[candidate_names.index(row[2])] = candidate_votes[candidate_names.index(row[2])]+1

    #initialising variables for winner's name and winner's percentages
    winner_name=candidate_names[0]
    winner_per = 0.00
    
    #printing results to the screan
    print("Election results")
    print("--------------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------------------------------")
    print (f"List of candidates: ")

    for i in range(0,len(candidate_names)):

        per_won=format((candidate_votes[i]/total_votes)*100, ".2f")
        if (winner_per < float(per_won)):
            winner_per=float(per_won)
            winner_name = candidate_names[i]
        print(f"{candidate_names[i]}:  {per_won}% ({candidate_votes[i]})")
       
    print("----------------------------------------------------")
    print(f"The Winner is: {winner_name}")
    print("----------------------------------------------------")

    #print results to the file
    poll_data_output = os.path.join('poll_data_output.txt')
    with open(poll_data_output,"w") as output:
    
        print("Election results", file=output)
        print("--------------------------------------------------------", file=output)
        print(f"Total votes: {total_votes}", file=output)
        print("--------------------------------------------------------")
        print("List of candidates:", file=output)
        for i in range(0,len(candidate_names)):
            per_won=format((candidate_votes[i]/total_votes)*100, ".2f")
            print(f"{candidate_names[i]}:  {per_won}% ({candidate_votes[i]})", file=output)
        print("----------------------------------------------------", file=output)
        print(f"The Winner is: {winner_name}", file=output)
        print("----------------------------------------------------", file=output)