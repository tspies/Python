import random
import os

print("   Welcome to Tower Dice simulator\n")
print("   You may have up to 6 die at a time, each dice can have between 2 - 20 sides")
print("   Press any key to continue . . .")
def setup():
	die_list = []
	run = True

	while run:
		print(" How many die's would you like to use?")
		die_number = input()
		if die_number > 0 and die_number< 7:
			print("Good number")
			for x in range(0, int(die_number)):
				valid_side = False
				while not valid_side:
					die_sides = input("   Please input how many sides you want dice to have.")
					if die_sides > 1 and die_sides < 21:
						die_list.append(die_sides)
						print("Dice: " +str(x + 1)+ " dice sides: " + str(die_sides))
						valid_side = True
					else:
						print("Invalid number of sides please input a number between 2 and 20")
			run = False
		else:
			print(" Invalid die number, please input a number between 1 and 6")
	return die_list

def play(d_list):
	roll = True
	os.system('clear')
	print("Press Enter To Roll your die ")
	raw_input("")
	while roll:
		for i in range(0, len(d_list)):
			randomNum = random.randint(1, d_list[i])
			print("Dice: " + str(i + 1) + " == [ " + str(randomNum) + " ] ")
		print("Press Enter to roll again or type ' exit ' to quit")
		try: 
			playAgain = input()
			if playAgain == "yes":
				continue
			else:
				os.system('clear')
				print("Good Bye")
				roll = False
		except:
			continue
			
d_list = setup()
play(d_list)
