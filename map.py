from items import *

room_dragon={
	"name":"dragon room",

	"description": 
	"""
	The room is large and bare, the chair sits in the center. A large Welsh flag is pinned to the wall facing the chair.
	From the damp in the room you are certain that it is underground. A pool of liquid has built under the chair, 
	it looks slippery. Oh look at that, its all over your shoe, you are careless arn't you. """,

	"exits": {"west": "corridor","south": "exit"},

	"items": []

	}

room_boss= {
	"name":"boss room",
        
	"description":
	"""
	The room is slightly flooded with the slipery liquid you have found throughout, and across from you is a giant throne. 
	The creature sitting upon it lifts it eyeys to meet yours, and you feel a sence of dread . . . do you really care what else is in 
	the room? You've got bigger problems right now. Oh, and by the way, I don't think you're really in this guys league . . . """,

	"exits": {"south": "corridor"},

	"items": [],

	"boss_alive": True

	}

armoury = {
	"name":"Armoury",

	"description":
	"""
	You walk into a elongated room, with walls stacked high with equipment you recognise from GCSE History. You appear to have found an armoury
	 - how convenient. From full suits of rusty mail to rotting wooden shields, the room is packed. There only seem to be a 
	 few items that you could pick up that wouldn't fall apart instantly. This room was made specficly to give you and advantage, try not to die.""",

	"exits": {"east": "corridor"},

	"items": [item_helmet, item_chest, item_sword]
}

room_treasure ={
	"name":"Treasure Room",

	"description":
	"""
	You enter a magnificent room filled with riches you couldn't have imagined. From giant chests overflowing with gold 
	coins, and steel swords with diamond hilts. There are bubbeling liquids of all sorts of colours to your left, to your right 
	a beautiful handcrafted crossbow with the head of a wolf biting on the handle. Straight ahead of you is a pillar of glass 
	engraved with strange runes, and atop the pillar is a glowing tomb with simular runes all over the cover. What? What do you 
	mean you wanted an Iphone? How are you disapointed with THIS? You really are infuriating.""",

	"exits": {"southwest": "corridor"},

	"items": [item_crown, item_coins]
}

corridor ={
	"name":"Corridor",

	"description":
	"""
	Ah, you appear to have found the corridor, no one saw that coming. It is long and dimly lit, but you can just about make out the three door in front 
	of you. There is a grand archway at the end of the corridor . . . pssst . . . thats the boss. On the right hand side of that is a door with a broken 
	chain that probaly used to keep it locked, I know this because its supposed to still be locked. Don't go in there, seriously, just don't. To the west 
	is an old wooden door, cracked at the bottom and slightly open, looks like a lazy developer trying to tell you to go in, you know, because it's an 
	armoury, and you can gear oh just forget about it already you really don't catch on quickly at all.""",
#You have stumbled out of kirills office into a long forgotten under ground tunnel, dim lighting casts a shadow on the wooden doors spaced every so often.
#	you can exit north to a grand archway, north east to a door loosly chained, east back to the office and west to a slightly open wooden door.
	"exits": {"north": "boss", "northeast": "treasure", "east": "dragon room", "west": "armoury"},

	"items": [item_potion, item_book, item_laptop, item_prospectus]
}

room_exit = {
	"name": "Exit",

	"description":
	"""Congradulations! Despite all your flaws, weaknesses, mishaps and failiours, you somehow stumbled out of this mess, or at least you think you did.
	What? You want a prize, is freedom not enough for you? Too bad, no cookie for you.""",

	"exits": {"north": "dragon room"},

	"items": []
}

rooms = {
	"dragon room": room_dragon,
	"boss": room_boss,
	"armoury": armoury,
	"treasure": room_treasure,
	"corridor": corridor,
	"exit": room_exit
}
