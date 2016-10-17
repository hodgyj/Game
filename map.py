room_office={
	"name":"kirills office",

	"description": 
	"""you have woken in a moderatly decorated office. The absence of overhead light casts shadows into the corners,
spilling under the desk and over top the framed black-and-white pictures on the wall. A desk stands before you layden
with books and papers all of incomprehensible text """,

	"exits": {"west": "Corridor","south": "exit"}

	}

room_boss= {
	"name":"boss room",
        
	"description":
	"""water trickles down the stone walls that are coated in a suspiciously viscid substance, a mass of darkness begins
to manifest before your eyes thickening becoming the embodiment of your worst nightmares. The mass' voice beckons demanding
you drop your weapon and surrender""",

	"exits": {"south": "Corridor"}

	}

Armoury = {
	"name":"armoury",

	"description":
	"""you are in the armoury""",

	"exits": {"east": "Corridor", "south": "emty"}
}

empty_room ={
	"name":"empty",
        
	"description":
	"""you have entered an empty room""",

	"exits": {"north": "armoury"}

}

room_death ={
	"name":"room of death",

	"description":
	"""you are in the death room""",

	"exits": {"south west": "Corridor"}
}

corridor ={
	"name":"Corridor",

	"description":
	"""you have stumbled out of kirills office into a long forgotten under ground tunnel, dim lighting casts a shadow on the wooden doors spaced every so often.
you can exit north to the boss' room, north east to the room of death, east back to kirills office and west to the armoury""",

	"exits": {"north": "boss room", " north east": "room of death", "east": "kirills office", "west": "armoury"}
}
