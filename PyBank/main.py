## Dependencies
import os
import csv
import statistics


## Specifies the path for the file
PyBankcsv = os.path.join("Resources","budget_data.csv")

monthCount = 0
totalRevenue = 0
largestIncrease = 0
largestDecrease = 0
bestMonth = ''
worstMonth = ''

## Create the lists to store data
change = []
monthToMonthChange = []

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        #tracks the totals 
        monthCount = monthCount + 1
        totalRevenue = totalRevenue + int(row[1])

        if int(row[1]) > largestIncrease:
            bestMonth = (row[0])
            largestIncrease = int(row[1])

        elif int(row[1]) < largestDecrease:
            worstMonth = (row[0])
            largestDecrease = int(row[1])
            
    # Stores the revenue chagnes 
        change.append(int(row[1]))


# calculate the monthly revenue changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])

    # list the changes 
    monthToMonthChange.append(monthlyChange)   

# calculate the mean of the list to find the average change
averageChange = statistics.mean(monthToMonthChange)



print("--------------------------------------------------")
print("                Financial Analysis")
print("--------------------------------------------------")
print("Total Months: "+ str(monthCount))
print("Total: £" + str(totalRevenue))
print("Average Change:  £" + str(round(averageChange, 3)))
print("Greatest Increase in Profits: " + str(bestMonth) + " (£" + str(largestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(worstMonth) + " (£" + str(largestDecrease) + ")")
print ('\n')

# Writes the findings to a txt file
f = open("financialAnalysis.txt", "w")
f.write('\n')
f.write("------------------------------------------------")
f.write('\n')
f.write("Financial Analysis for Python Bank")
f.write('\n')
f.write("------------------------------------------------")
f.write('\n')

f.write("Total Months: "    + str(monthCount))
f.write('\n')
f.write("Total: £" + str(totalRevenue))
f.write('\n')
f.write("Average Change: £" + str(round(averageChange, 3)))
f.write('\n')
f.write("Greatest Increase in Profits: " + str(bestMonth) + " (£" + str(largestIncrease) + ")")
f.write('\n')
f.write("Greatest Decrease in Profits: " + str(worstMonth) + " (£" + str(largestDecrease) + ")")
f.write('\n')


