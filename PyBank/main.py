import os
import csv

fileLoad = os.path.join("resources", "budget_data.csv")

# file to hold the output of analysis
analysisFile = os.path.join("analysis", "budget_analysis.txt")

#initialize variables
totalMonths = 0     # total months
revenue = 0         # total profit/loss
monthlyChanges = [] # list of monthly changes
months = []         # list of months

with open(fileLoad) as bankData:           # read the csv file
    reader = csv.reader(bankData)          # create reader object
    header = next(reader)                  # read header row
    firstRow = next(reader)                # move to the first row
    previousRevenue = float(firstRow[1])   # establish previous revenue
    totalMonths += 1         
    for row in reader:
        totalMonths += 1                            # increment total months
        revenue += float(row[1])                    # add on to total revenue, index 1 for prof/loss
        netChange = float(row[1]) - previousRevenue # calculate net change
        monthlyChanges.append(netChange)            # append next netChange to monthlyChange list
        months.append(row[0])                       # add first month when change occurred, index 0 for month
        previousRevenue = float(row[1])             # update previous revenue

# calculate average net change per month
averageChange = sum(monthlyChanges) / len(monthlyChanges)

# get greatest increase and greatest decrease
highProf = [months[0], monthlyChanges[0]]  # greatest profit and month
highLoss = [months[0], monthlyChanges[0]]  # greatest loss and month

# calculate greatest increase/decrease
for m in range(len(monthlyChanges)):
    if (monthlyChanges[m] > highProf[1]):
        highProf[1] = monthlyChanges[m] # if value is > greatest increase, then replace value
        highProf[0] = months[m]         # update month
    if (monthlyChanges[m] < highLoss[1]):
        highLoss[1] = monthlyChanges[m] # if value is < greatest decrease, then replace value
        highLoss[0] = months[m]         # update month

# start generating the output
output = (
    f"\n\nFinancial Analysis \n"
    f"------------------------------------------\n"
    f"Total Months...............{totalMonths}\n\n"
    f"Net Revenue................${revenue:,.2f}\n"
    f"Average Change.............${averageChange:,.2f}\n\n"
    f"Greatest Profit Increase...{highProf[0]} in the amount of ${highProf[1]:,.2f}\n"
    f"Greatest Profit Decrase....{highLoss[0]} in the amount of ${highLoss[1]:,.2f}\n"
    )
# print the output to console
print(output)

# export the output to the text file
with open(analysisFile, "w") as textFile:
    textFile.write(output)