import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# 
total_months = 0
total_amount = 0
first_row = None
total_change = 0
profit_increase = 0
profit_decrease = 0 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader, None)

    for row in csvreader:
        total_months = total_months + 1
        amount = int(row[1])
        total_amount = total_amount + amount

        if first_row is not None:    
            change = amount - first_row
            total_change = change + total_change

            if profit_increase < change:
                profit_increase = change
                profits_row = row[0]
            
            if profit_decrease > change:
                profit_decrease = change
                decrease_row = row[0]

        first_row = amount


print("""Financial Analysis

----------------------------""")
print(f"Total Months: {total_months}")        
print(f"Total:  ${total_amount}")
print(f"Average Change: ${int(total_change/total_months)}")
print(f"Greatest Increase in Profits: {profits_row} (${profit_increase})")
print(f"Greatest Decrease in Profits: {decrease_row} (${profit_decrease})")  

analysis = os.path.join("Analysis","analysis.txt")
        
with open(analysis, 'w') as text_file:

    text_file.write(f"""Financial Analysis
    -------------------------
    Total Months:  {total_months}
    Total:  ${total_amount}
    Average Change: ${int(total_change/total_months)})
    Greatest Increase in Profits: {profits_row} (${profit_increase})
    Greatest Decrease in Profits: {decrease_row} (${profit_decrease})
    --------------------------------""")