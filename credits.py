import time

def roll_credits():
	credits = [
	"\nThank you for playing our hastily made text based adventure game",
	"\nDesigned by: gods perfect idiot",
	"\nProduced by: the real heroes here",
	"\nCharacter design: James",
	"\nNarrator design: Luca, Alastair",
	"\nMurderers: Alastair, Luca, Dervla",
	"\nInsult co-ordinator: Alastair, Luca, James, Dervla",
	"\nWorld creators: creators: Nick, Natalie, Sam, Alastair",
	"\nLab rats: Nick, Alastair, Sam, Natalie",
	"\nGame coders: Dervla, James, Luca",
	"\nSpecial thanks to Louie for being the hardest working member of the team."]

	for line in credits:
		print(line)
		time.sleep(0.1)


		