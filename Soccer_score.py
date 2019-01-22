# While Read One line
#     Parse String into Array [team, score, team, score]
#     compare score - Who Wins?
#                   - Who Draw?
#                   - Who Loses?
#     FUNC If Win (A score > B score visa)
#         Check if winning team is already in array
#             if not - add to array [score - 1] element
#         Check losing team is already in array
#             if not add to array [score - 1] elemnt
#         win team + 3

#     FUNC If Draw (A score = B score)
#         Check if both teams exit in array
#             else add
#         A score + 1 --- B score + 1

#     sort by score
#     Check for score duplicates
#         Sort alphabetically by team names if duplicate

#     Check length of dictionary
#     While i < len(dictionary)
#     print (i. "team name" "team score")

import re
soccer_dict = {}
with open("soccer.txt") as file:
	for line in file:
		line = line.split(', ')
		score1 = re.findall(r"\d+", line[0])
		score2 = re.findall(r"\d+", line[1])
		team1 = re.sub(r'\d+', '', line[0])
		team2 = re.sub(r'\d+', '', line[1])

		team1 = team1.rstrip()
		team2 = team2.rstrip()

		if ((team1 in soccer_dict) == False or (team2 in soccer_dict) == False):
			if ((team1 in soccer_dict) == False):
				soccer_dict[team1] = 0
			if ((team2 in soccer_dict) == False):
				soccer_dict[team2] = 0
		if ((score1 > score2) or (score2 > score1)):
			if (score1 > score2):
				soccer_dict[team1] += 3
			else:
				soccer_dict[team2] += 3
		elif (score1 == score2):
			soccer_dict[team1] +=1
			soccer_dict[team2] +=1
i = 1
for key, value in sorted(soccer_dict.items(), reverse=True, key=lambda kv: kv[1]):
	if (value == 1):
		print ('%d. %s %s pt' % (i, key, value))
		i = i + 1
	else:
		print ('%d. %s %s pts' % (i, key, value))
		i = i + 1