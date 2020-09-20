import re
soccer_dict = {}
with open("soccer.txt") as file:
	for line in file:
		line = line.split(', ')
		# Exracting the scores from line
		score1 = re.findall(r"\d+", line[0])
		score2 = re.findall(r"\d+", line[1])
		# Extracting team names from line
		team1 = re.sub(r'\d+', '', line[0])
		team2 = re.sub(r'\d+', '', line[1])
		# Stripping whitespace and newlines
		team1 = team1.rstrip()
		team2 = team2.rstrip()

		# Checking if team already exists in soccer_dict - Adding if not
		if ((team1 in soccer_dict) == False or (team2 in soccer_dict) == False):
			if ((team1 in soccer_dict) == False):
				soccer_dict[team1] = 0
			if ((team2 in soccer_dict) == False):
				soccer_dict[team2] = 0
		# Checking which team won and adding score to soccer_dict value
		if ((score1 > score2) or (score2 > score1)):
			if (score1 > score2):
				soccer_dict[team1] += 3
			else:
				soccer_dict[team2] += 3
		# Adding score to both teams in case of a draw
		elif (score1 == score2):
			soccer_dict[team1] +=1
			soccer_dict[team2] +=1
i = 0
previous_score = -1
for key, value in sorted(soccer_dict.iteritems(), key=lambda (k,v): (-v,k)):
	if (value != previous_score):
		i = i + 1
		previous_score = value
	if (value == 1):
		print ('%d. %s %s pt' % (i, key, value))
	else:
		print ('%d. %s %s pts' % (i, key, value))