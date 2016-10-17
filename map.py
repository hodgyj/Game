from items import *

room_office={
	"name":"kirills office",

	"description": 
	"""you have woken in a moderatly decorated office. The absence of overhead light casts shadows into the corners,
spilling under the desk and over top the framed black-and-white pictures on the wall. A desk stands before you layden
with books and papers all of incomprehensible text """,

	"exits": {"west": "Corridor","south": "exit"},

	"items": []

	}

room_boss= {
	"name":"boss room",
        
	"description":
	"""water trickles down the stone walls that are coated in a suspiciously viscid substance, a mass of darkness begins
to manifest before your eyes thickening becoming the embodiment of your worst nightmares. The mass' voice beckons demanding
you drop your weapon and surrender""",

	"exits": {"south": "Corridor"},

	"items": [item_key]

	}

armoury = {
	"name":"armoury",

	"description":
	"""You walk into a elongated room, with walls stacked high with equipment you recognise from GCSE History. You appear to have found an armoury
	 - how convenient. From full suits of rusty mail to rotting wooden shields, the room is packed. There only seem to be a 
	 few items that you could pick up that wouldn't fall apart instantly.""",

	"exits": {"east": "Corridor", "south": "empty"},

	"items": [item_helmet, item_chest, item_weapon]
}

empty_room ={
	"name":"empty",
        
	"description":
	"""you have entered an empty room""",

	"exits": {"north": "armoury"},

	"items": [item_note] #remove if you want, idk whats going on

}

room_treasure ={
	"name":"treasure room",

	"description":
	"""You enter a magnificent room filled with riches you couldn't have imagened. From giant chests overflowing with gold 
	coins, and steel swords with diamond hilts. There are bubbeling liquids of all sorts of colours to your left, to your right 
	a beautiful handcrafted crossbow with the head of a wolf biting on the handle. Straight ahead of you is a pillar of glass 
	engraved with strange runes, and atop the pillar is a glowing tomb with simular runes all over the cover""",

	"exits": {"south west": "Corridor"},

	"items": [item_crown, item_coins]
}

corridor ={
	"name":"Corridor",

	"description":
	"""you have stumbled out of kirills office into a long forgotten under ground tunnel, dim lighting casts a shadow on the wooden doors spaced every so often.
you can exit north to a grand archway, north east to a door loosly chained, east back to the office and west to a slightly open wooden door.""",

	"exits": {"north": "boss room", " north east": "treasure room", "east": "kirills office", "west": "armoury"},

	"items": [item_potion, item_book, item_laptop, item_prospectus]
}

room_exit = {
	"name": "Exit",

	"description":
	"""You exited. Well done""",

	"exits": {"north": "office"},

	"items": []
}

rooms = {
	"office": room_office,
	"boss": room_boss,
	"armoury": armoury,
	"empty": empty_room,
	"treasure": room_treasure,
	"corridor": corridor,
	"exit": room_exit
}
