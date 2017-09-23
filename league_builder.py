
#Import csv to handle read/write csv files
import csv

#Create a function to parse csv file of teams,
def parseCSVfile(fileName):
	#initialize dictionary, list of experienced and nonExperienced players
	dictPlayers={}
	experiencedPlayers =[]
	nonExperiencedPlayers = []
	with open(fileName,'r') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[0]!="Name":
				dictPlayers[row[0]]={"height":row[1], 'experienced':row[2], 'guardian_name': row[3]}
				if row[2]=="YES":
					experiencedPlayers.append(row[0])
				else:
					nonExperiencedPlayers.append(row[0])
	return dictPlayers, experiencedPlayers,nonExperiencedPlayers



def createTeams(experiencedList,nonExperiencedList,dictPlayers):
	#initialize the three teams
	sharks = []
	dragons = []
	raptors = []
	#Create dictionary of team names
	teamNames = ["Sharks", "Dragons", "Raptors"]
	teams = [sharks, dragons, raptors]
	count = 0
	for team in teams:
		for i in range(3):
			name = experiencedList.pop()
			dictPlayers[name]["team"] = teamNames[count]
			team.append(name)
			name = nonExperiencedList.pop()
			dictPlayers[name]["team"] = teamNames[count]
			team.append(name)
		count += 1
	return teams


#Write to a file teams.txt
def writeTeamsToCSV(fileName,teamList,dictPlayers):
	teamNames = ["Sharks", "Dragons", "Raptors"]
	with open(fileName, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',')
		for i in range(len(teamList)):
			writer.writerow([teamNames[i]])
			for player in teamList[i]:
				writer.writerow([player, dictPlayers[player]['experienced'], dictPlayers[player]['guardian_name']])

def writeLetterGuardian(teamList,dictPlayers):
	for i in dictPlayers.keys():
		name =  i
		guardian_name = dictPlayers[i]["guardian_name"]
		team = dictPlayers[i]["team"]
		fileName = i.lower()
		fileName = fileName.split()
		fileName = "_".join(fileName)
		message = " Dear {},\n We are happy to inform you that {} has been accepted to the {}. The first practice session will be on the 1st of September, 2017 at 14:00.\n Please make sure that {} makes it on time to his first practice. \n sincerely yours, \n Hassan Sirelkhatim"
		with open(fileName+".txt", 'w') as file:
			file.write(message.format(guardian_name,name,team,name))
			
if __name__ == "__main__":
	dictNames, experienced, nonExperienced = parseCSVfile("soccer_players.csv")
	teams = createTeams(experienced,nonExperienced,dictNames)
	writeTeamsToCSV("teams.txt", teams,dictNames)
	writeLetterGuardian(teams,dictNames)
