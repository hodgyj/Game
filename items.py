# It seems for python to be happy you have to define the function and what it does first, 
# and then set the value of use_func to the function we want to execute
# def use_key():
#     import player 
#     if not player.current_room["kirills office"]: #For some reason this isnt working I hate python !! This if statement will now return false.
#         print("You cannot use that here.")
#         return False 
#     else:
#         # Code for using key goes here
#         return True # Returns True if used so that it can be removed
# I'll explain what's wrong here tomorrow

item_key = {
    "id": "key",

    "name": "key",

    "description":
    """A rusted old key.""",

    "use": "removeable", 

    "use_func": use_key() # Don't forget if you don't put the brackets it will treat it as a variable not a function
}

item_weapon = {
    "id": "weapon",

    "name": "sword",

    "description":
    """The steel sword is adorned with the head of a wyvern."""

}

item_potion = {
    "id": "potion",

    "name": "health potion",

    "description":
    """The label reads this potion can restore 150hp, you also notice the expiry
date is from 2 years ago."""
}

item_book = {
    "id": "book",

    "name": "python for dummies",

    "description":
    """a dog eared papered back version for the key to success in python."""
}

item_laptop = {
    "id": "laptop",

    "name": "laptop",

    "description":
    """displayed on the laptop screen is a file containing the answers for python lab 3."""
}

item_prospectus = {
    "id": "prospectus",

    "name": "prospectus",

    "description":
    """in bold writing on the cover of this prospectus reads studying computer science in cardiff university."""
}

item_chest = {
    "id": "chest",

    "name": "chest armour",

    "description":
    """the rusted chestpiece is almost useless,
the weight of the armour is too much for you and you fall to the ground.
The rusted armour breaks on impact."""
}

item_helmet = {
    "id": "helmet",

    "name": "Warrior's helmet",

    "description":
    """next to the chest armour you see a magnificent helmet carved out of anchient metal. It is calling for you.
You put it on but your head is too small for it."""
}

item_note = {
    "id": "note",

    "name": "crushed paper",

    "description":
    """you pick up the crushed piece of paper, there are notes left on the paper which reads.. i saw a bright light
coming from the north east in the corridor, could it be something more?"""
}

item_crown = {
    "id": "crown",

    "name": "crown",

    "description":
    """you put the crown on, you look fabulous."""
}

item_coins = {
    "id": "coins",

    "name": "gold coins",

    "description":
    """modern currency doesnt allow for gold coins, these are useless."""
}

item_orb = {
    "id":"orb",

    "name": "celestial sphere",

    "description":
    """A shiny looking orblike object. There are ancient carvings on it and illustrations to show how it can used"""
    #when opened can be used as a teleport or u choose between to 2: "the orb does nothing u idiot"-nicks idea

}


