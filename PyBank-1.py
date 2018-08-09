import os
import csv

#PyBank_csv_path= os.path.join("PyBank","Resources","budget_data.csv")

totalmonth= 0
totalprofitloss=0
previous_revenue=0
revenue_array = []

greatestIncreaseMonth = " "
greatestIncreaseAmount = 0.0 

greatestDecreaseMonth = " " 
greatestDecreaseAmount = 0.0

with open('budget_data.csv') as csvfile:
 	reader = csv.DictReader(csvfile)
	for row in reader:
		currentMonth = row['Date']
		monthlyMoney = int(row['Profit/Losses'])
		
		
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


	



	print( "Total months: " + str(totalmonth))
	print("Total: " + str(totalprofitloss))
	print("Greatest Increase: " + greatestIncreaseMonth + ":::" +  str(greatestIncreaseAmount) )
	print("Greatest Decrease: " +greatestDecreaseMonth+ ":::" + str(greatestDecreaseAmount))
	print("Average Change : " + str(average_change))

	 
        


