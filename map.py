from items import *

room_dragon={
	"name":"dragon room",

	"description": 
	"""The room is large and bare, the chair sits in the center. A large Welsh flag is pinned to the wall facing the chair.
	From the damp in the room you are certain that it is underground. A pool of liquid has built under the chair, it looks slippery. """,

	"exits": {"west": "corridor","south": "exit"},

	"items": []

	}

room_boss= {
	"name":"boss room",
        
	"description":
	"""water trickles down the stone walls that are coated in a suspiciously viscid substance, a mass of darkness begins
to manifest before your eyes thickening becoming the embodiment of your worst nightmares. The mass' voice beckons demanding
you drop your weapon and surrender""",

	"exits": {"south": "corridor"},

	"items": [],

	"boss_alive": True

	}

armoury = {
	"name":"armoury",

	"description":
	"""You walk into a elongated room, with walls stacked high with equipment you recognise from GCSE History. You appear to have found an armoury
	 - how convenient. From full suits of rusty mail to rotting wooden shields, the room is packed. There only seem to be a 
	 few items that you could pick up that wouldn't fall apart instantly.""",

	"exits": {"east": "corridor"},

	"items": [item_helmet, item_chest, item_sword]
}

room_treasure ={
	"name":"treasure room",

	"description":
	"""You enter a magnificent room filled with riches you couldn't have imagined. From giant chests overflowing with gold 
	coins, and steel swords with diamond hilts. There are bubbeling liquids of all sorts of colours to your left, to your right 
	a beautiful handcrafted crossbow with the head of a wolf biting on the handle. Straight ahead of you is a pillar of glass 
	engraved with strange runes, and atop the pillar is a glowing tomb with simular runes all over the cover""",

	"exits": {"southwest": "corridor"},

	"items": [item_crown, item_coins]
}

corridor ={
	"name":"Corridor",

	"description":
	"""you have stumbled out of kirills office into a long forgotten under ground tunnel, dim lighting casts a shadow on the wooden doors spaced every so often.
you can exit north to a grand archway, north east to a door loosly chained, east back to the office and west to a slightly open wooden door.""",

	"exits": {"north": "boss", "northeast": "treasure", "east": "office", "west": "armoury"},

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
	"treasure": room_treasure,
	"corridor": corridor,
	"exit": room_exit
}
