#Importing data
import os
import csv

# Grabbing Location of Data
budget_csv = os.path.join('Resources', 'budget_data.csv')

# open and read csv
with open(budget_csv) as csv_file :
    csv_reader = csv.reader(csv_file,delimiter=",")

    # skip header
    csv_header=next(csv_file)
    print(f"Header: {csv_header}")

    #defining counter
    counter = 0
    monthlist = []
    changelist = []
    monthly_change= []
    

    # Read each row of data
    for row in csv_reader :
        months=(row[0])
        monthlist.append(months)
        profit=int(row[1])
        changelist.append(profit)
        number_months=len(monthlist)
       
#creating for loop to establish the change in values   
    for i in range(len(changelist) - 1):
    #reading the data for the monthly change
        monthly_change.append(changelist[i+1]-changelist[i])
#finding the positive increase or the max in the data
positive_value=max(monthly_change)
   
#finding the negative value or the min in the data
negative_value=min(monthly_change) 

#Profit/Losses over the entire peroid
net_total=sum(changelist)

#Changes in Profit/Losses
average_change = sum(monthly_change)/len(monthly_change)

#Print in python
print("Financial Analysis")  
print("------------------")
print(f"Total Months: {number_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: Aug-16 ({positive_value})")
print(f"Greatest Decrease in Profits: Feb-14 ({negative_value})")

#create a new file       
with open('Financial_Analysis.txt', 'w') as file:

    #inputing information into text file
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months: {number_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: (${positive_value})\n")
    file.write(f"Greatest Decrease in Profits: (${negative_value})\n")


