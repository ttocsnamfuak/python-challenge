#PyBank Script
import os
import csv

#Get the filename to open
fileName = "budget_data_1.csv"


#set paths for files
bankBudget_csv = os.path.join("raw_data", fileName)


#Variables to track budget
totMonths = 0
totRev = 0
lmRev = 0
revChg = 0
revChgLst = []
monChgLst = []
minMonRev = 0
maxMonRev = 0
avgMonRevChg = 0
grtRevChg =["",0]
lstRevChg =["",9999999999999999999999]

# Lists to store data
month = []
monthRevenue = []


#Open the file and then read the file
with open(bankBudget_csv, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    for row in csvreader:
        #add up the months and the revenue
        totMonths = totMonths + 1
        totRev = totRev + int(row['Revenue'])
        
        #calc monthly revenue change
        revChg = int(row["Revenue"]) - lmRev #change in rev = revenue - lstmonths rev
        lmRev = int(row["Revenue"]) #set last months revenue to this month
        revChgLst = revChgLst + [revChg] #add the rev change to the list
        monChgLst = monChgLst + [row["Date"]] #add the date to the list
        
        #figure out the biggest increase
        if (revChg > grtRevChg[1]):
            grtRevChg[1] = revChg #set the Rev amt in the array
            grtRevChg[0] = row['Date'] #set the date in the array
 
        #figure out the biggest decrease
        if (revChg < lstRevChg[1]):
            lstRevChg[1] = revChg #set the Rev amt in the array
            lstRevChg[0] = row['Date'] #set the date in the array
       
# Calculate the Average Revenue Change
avgMonRevChg = sum(revChgLst) / len(revChgLst)

#print to the terminal
print("\nFinancial Analysis \n--------------------------------------------------")
print("Total Months: " + str(totMonths))
print("Total Revenue:  $" + str(totRev))
print("Average Monthly Change: " + str(avgMonRevChg)) 
print("Greatest Monthly Increase: " + str(grtRevChg[0]) + "  $(" + str(grtRevChg[1]) + ")")   
print("Greatest Monthly Decrease: " + str(lstRevChg[0]) + "  $(" + str(lstRevChg[1]) + ")")


#create the output file    
fileOutName = "bank_analysis.txt"
outputFile = os.path.join(fileOutName)
with open(outputFile, "w") as txt_file:
# txt_file.write( "Python is a great language.\nYeah its great!!\n")
    txt_file.write("\nFinancial Analysis \n--------------------------------------------------")
    txt_file.write("\nTotal Months: " + str(totMonths))
    txt_file.write("\nTotal Revenue: $" + str(totRev))
    txt_file.write("\nTotal Average Monthly Change: $" + str(totRev))
    txt_file.write("\nGreatest Monthly Increase: " + str(grtRevChg[0]) + "  $(" + str(grtRevChg[1]) + ")")
    txt_file.write("\nGreatest Monthly Decrease: " + str(lstRevChg[0]) + "  $(" + str(lstRevChg[1]) + ")")