import os
import csv

PyBank_csv_path= os.path.join("budget_data.csv")
output_file= "budget_data.txt"

totalmonth = 0
totalprofitloss = 0
previous_revenue = 0
revenue_array = []

greatestIncreaseMonth = " "
greatestIncreaseAmount = 0.0 

greatestDecreaseMonth = " " 
greatestDecreaseAmount = 0.0

with open(PyBank_csv_path) as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		currentMonth = int(row['Date'])
		monthlyMoney = (row['Profit/Losses'])
		
		
		totalmonth = totalmonth + 1 
		totalprofitloss = totalprofitloss + monthlyMoney 
		revenue_array.append(monthlyMoney) 

		delta_revenue  = monthlyMoney - previous_revenue
		
		if(delta_revenue > greatestIncreaseAmount):
			greatestIncreaseAmount = delta_revenue
			greatestIncreaseMonth = currentMonth 

		if(delta_revenue < greatestDecreaseAmount):
			greatestDecreaseAmount = delta_revenue
			greatestDecreaseMonth = currentMonth 

	previous_revenue = monthlyMoney 
	
	average_change = sum(revenue_array) / len(revenue_array)


	

#Output

print( "Total months: " + str(totalmonth))
print("Total: " + str(totalprofitloss))
print("Greatest Increase: " + greatestIncreaseMonth + ":::" +  str(greatestIncreaseAmount) )
print("Greatest Decrease: " +greatestDecreaseMonth+ ":::" + str(greatestDecreaseAmount))
print("Average Change : " + str(average_change))

# to print output in text file 
with open(output_file, "w") as txt_file:
    txt_file.write("Total Months: " + str(totalmonth))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(totalprofitloss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_array) / len(revenue_array),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatestIncreaseMonth[0]) + " ($" + str(greatestIncreaseMonth[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatestDecreaseMonth[0]) + " ($" + str(greatestDecreaseMonth[1]) + ")")	 
        


