#import necessary libraries
import os
import csv

#create pathes to the file with employee data and new modified file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
employee_data_csv = os.path.join('employee_data.csv')
employee_data_csv_m = os.path.join('employee_data_m.csv')

#open data file for reading
with open(employee_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #open new modified file for writing
    with open(employee_data_csv_m, "w", newline='') as output:
        csvwriter = csv.writer(output, delimiter=',')
        
        #skip the header of the old data file
        csvheader=next(csvreader)
        #create the header of the modified data file
        csvwriter.writerow(["Emp ID", "First Name", "Last Name","DOB", "SSN", "State"])
    

    
        for row in csvreader: 
            #split the full name into first and last name
            full_name=row[1]
            first_name = full_name.split()[0]
            last_name = full_name.split()[1]
            
            #create the new format for the date
            old_date=row[2]
            birth_year=old_date.split("-")[0]
            birth_month=old_date.split("-")[1]
            birth_day=old_date.split("-")[2]
            date=[birth_month,birth_day,birth_year]
            new_date="/".join(map(str, date))
            
            #create the new format for SSN
            old_ssn=row[3]
            last_4=old_ssn.split("-")[2]
            first_3="***"
            second_2="**"
            ssn=[first_3, second_2, last_4]
            new_ssn="-".join(map(str,ssn))

            
            #create the new format for the state
            old_state=row[4]
            
            us_state_abbrev = {
                'Alabama': 'AL',
                'Alaska': 'AK',
                'Arizona': 'AZ',
                'Arkansas': 'AR',
                'California': 'CA',
                'Colorado': 'CO',
                'Connecticut': 'CT',
                'Delaware': 'DE',
                'Florida': 'FL',
                'Georgia': 'GA',
                'Hawaii': 'HI',
                'Idaho': 'ID',
                'Illinois': 'IL',
                'Indiana': 'IN',
                'Iowa': 'IA',
                'Kansas': 'KS',
                'Kentucky': 'KY',
                'Louisiana': 'LA',
                'Maine': 'ME',
                'Maryland': 'MD',
                'Massachusetts': 'MA',
                'Michigan': 'MI',
                'Minnesota': 'MN',
                'Mississippi': 'MS',
                'Missouri': 'MO',
                'Montana': 'MT',
                'Nebraska': 'NE',
                'Nevada': 'NV',
                'New Hampshire': 'NH',
                'New Jersey': 'NJ',
                'New Mexico': 'NM',
                'New York': 'NY',
                'North Carolina': 'NC',
                'North Dakota': 'ND',
                'Ohio': 'OH',
                'Oklahoma': 'OK',
                'Oregon': 'OR',
                'Pennsylvania': 'PA',
                'Rhode Island': 'RI',
                'South Carolina': 'SC',
                'South Dakota': 'SD',
                'Tennessee': 'TN',
                'Texas': 'TX',
                'Utah': 'UT',
                'Vermont': 'VT',
                'Virginia': 'VA',
                'Washington': 'WA',
                'West Virginia': 'WV',
                'Wisconsin': 'WI',
                'Wyoming': 'WY',
            }
            for state in us_state_abbrev:
                if (old_state==state):
                    new_state=us_state_abbrev[state]
                 
            #write to the new modified file
            csvwriter.writerow([row[0], first_name, last_name, new_date, new_ssn, new_state])