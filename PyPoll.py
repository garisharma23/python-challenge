
import csv


# variable declarations 
totalVotes = 0.0

khanVotes = 0
khanPercent = 0.0

correyVotes = 0
correyPercent =0.0

liVotes = 0
liPercent = 0.0


otooleyVotes =0
otooleyPercent = 0.0

electionWinner = " "

with open('election_data.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		
		current = row["Candidate"]

		totalVotes = totalVotes+1
		
		#vote logic 
		if(current == "Khan"):
			khanVotes =khanVotes + 1
		elif(current == "Correy"):
			correyVotes=correyVotes + 1
		elif(current == "Li"): 
			liVotes = liVotes +1
		elif(current == "O'Tooley"): 
			otooleyVotes = otooleyVotes +1
		else:
			print("Error:  Corrupted voting data") 

	#percent calculations 
	knanPercent = round((khanVotes / totalVotes) *100,3)
	correyPercent = round((correyVotes / totalVotes) *100,3)
	liPercent = round((liVotes / totalVotes) *100,3)
	otooleyPercent = round((otooleyVotes / totalVotes) *100,3)


	#electrion determination logic  
	if( (khanVotes >correyVotes) and (khanVotes >liVotes) and (khanVotes > otooleyVotes)):
		electionWinner = "Khan"
	elif( (correyVotes >khanVotes) and (correyVotes >liVotes) and (correyVotes > otooleyVotes)):
		electionWinner = "Correy" 
	elif ( (liVotes >khanVotes) and (liVotes >correyVotes) and (liVotes > otooleyVotes)):
		electionWinner = "Li"
	elif ( (otooleyVotes >khanVotes) and (otooleyVotes >correyVotes) and (otooleyVotes > liVotes)):
		electionWinner = " O'Tooley"
	else: 
		print("Error: Tie")


	#Print to screen 
	print("Election Results")
	print("=====================")
	print("Total Votes: "+ str(totalVotes))
	print("=====================")
	print("Khan: " + str(knanPercent) + "%(" + str(khanVotes)+ ")") 
	print("Correy: " + str(correyPercent) + "%(" + str(correyVotes)+ ")") 
	print("Li: " + str(liPercent) + "%(" + str(liVotes)+ ")") 
	print("O'Tooley: " + str(otooleyPercent) + "%(" + str(otooleyVotes)+ ")") 
	print("=====================")
	print("Election Winner:  " + electionWinner) 
	print("=====================")
  
	#print to file 
	outputFile = open("results.txt", "w")
	outputFile.write("Election Results")
	outputFile.write("\n")
	outputFile.write("=====================")
	outputFile.write("\n")
	outputFile.write("Total Votes: "+ str(totalVotes)) 
	outputFile.write("\n") 
	outputFile.write("=====================")
	outputFile.write("\n") 
	outputFile.write("Khan: " + str(knanPercent) + "%(" + str(khanVotes)+ ")") 
	outputFile.write("\n") 
	outputFile.write("Correy: " + str(correyPercent) + "%(" + str(correyVotes)+ ")") 
	outputFile.write("\n") 
	outputFile.write("Li: " + str(liPercent) + "%(" + str(liVotes)+ ")") 
	outputFile.write("\n")
	outputFile.write("O'Tooley: " + str(otooleyPercent) + "%(" + str(otooleyVotes)+ ")")
	outputFile.write("\n") 
	outputFile.write("=====================")
	outputFile.write("\n")
	outputFile.write("Election Winner:  " + electionWinner) 
	outputFile.write("\n") 
	outputFile.write("=====================")
	outputFile.write("\n") 


		


