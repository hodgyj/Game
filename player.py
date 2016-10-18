from items import *
from map import rooms

inventory = []

# Start game at the reception
current_room = rooms["dragon room"]
gibberish = 0
attempts = 0
name = ""
quest = ""
answer = ""

attempt_exit = ["You know you actually have to play the game before leaving?",
	"You can't go there yet, what's the point in leaving early?",
	"Why are you even playing this game if you didn't want to finish it?",
	"Do you quit everything in life this quickly?",
	"For the love of all that is holy why are you still trying?!? STOP IT ALREADY!!!",
	"Why don't you just close the application? If you don't want to play the damn game just close it",
]