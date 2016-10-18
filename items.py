import time
# It seems for python to be happy you have to define the function and what it does first, 
# and then set the value of use_func to the function we want to execute
def use_key():
    import player 
    #if not player.current_room["kirills office"]: #For some reason this isnt working I hate python !! This if statement will now return false.
    if player.current_room["name"] != "kirills office": 
        print("You cannot use that here.")
        return False 
    else:
        print("""You put the key into the door and slowly turn it, you hear a satifying click as the lock slides back. \n
As the door opens you are blinded by the light from outside. As you begin to leave you think back on the day and ponder. . .
just how in the world did you tie yourself to the chair like that?""")

        time.sleep(4)
        print("""\n'Oh well' you think, 'at least I got to kill a troll'.""")
        time.sleep(5)
        exit()
        return True # Returns True if used so that it can be removed
        #(Doesnt really matter cause the game ends)
# I'll explain what's wrong here tomorrow
# I fixed it but for some reason it didnt get added in my commit

item_key = {
    "id": "key",

    "name": "a key",

    "description":
    """A rusted old key.""",

    "use": "removeable", 

    "use_func": use_key # Don't forget if you don't put the brackets it will treat it as a variable not a function
    # It's still treated as a function, if you put the brackets it seems to run the function on startup
}

item_sword = {
    "id": "sword",

    "name": "a sword",

    "description":
    """The steel sword is adorned with the head of a wyvern."""

}

item_potion = {
    "id": "potion",

    "name": "a health potion",

    "description":
    """The label reads this potion can restore 150hp, you also notice the expiry
date is from 2 years ago."""
}

item_book = {
    "id": "book",

    "name": "a python for dummies book",

    "description":
    """a dog eared papered back version for the key to success in python."""
}

item_laptop = {
    "id": "laptop",

    "name": "a laptop",

    "description":
    """displayed on the laptop screen is a file containing the answers for python lab 3."""
}

item_prospectus = {
    "id": "prospectus",

    "name": "a prospectus",

    "description":
    """in bold writing on the cover of this prospectus reads studying computer science in cardiff university."""
}

item_chest = {
    "id": "chest",

    "name": "some chest armour",

    "description":
    """the rusted chestpiece is almost useless,
the weight of the armour is too much for you and you fall to the ground.
The rusted armour breaks on impact."""
}

item_helmet = {
    "id": "helmet",

    "name": "a Warrior's helmet",

    "description":
    """next to the chest armour you see a magnificent helmet carved out of anchient metal. It is calling for you.
You put it on but your head is too small for it."""
}

item_note = {
    "id": "note",

    "name": "some crushed paper",

    "description":
    """you pick up the crushed piece of paper, there are notes left on the paper which reads.. i saw a bright light
coming from the north east in the corridor, could it be something more?"""
}

item_crown = {
    "id": "crown",

    "name": "a crown",

    "description":
    """you put the crown on, you look fabulous."""
}

item_coins = {
    "id": "coins",

    "name": "some gold coins",

    "description":
    """modern currency doesnt allow for gold coins, these are useless."""
}

item_orb = {
    "id":"orb",

    "name": "a celestial sphere",

    "description":
    """A shiny looking orblike object. There are ancient carvings on it and illustrations to show how it can used"""
    #when opened can be used as a teleport or u choose between to 2: "the orb does nothing u idiot"-nicks idea

}


