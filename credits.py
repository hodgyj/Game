import time

def roll_credits():
	credits = [
	"\nThank you for playing our hastily made text based adventure game",
	"\nDesigned by: gods perfect idiot",
	"\nProduced by: the real heroes here",
	"\nCharacter design: James",
	"\nNarrator design: Luca",
	"\nAnnoying publisher who doesn't understand development time: Alastair",
	"\nInsult co-ordinator: Alastair",
	"\nitem creators: Nick, Natalie, Sam.",
	"\nGame coders: Dervla, James, Luca",
	"\nSpecial thanks to Louie for being the hardest working member of the team."]

	for line in credits:
		print(line)
		time.sleep(0.1)


		