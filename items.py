import time
import random

# It seems for python to be happy you have to define the function and what it does first, 
# and then set the value of use_func to the function we want to execute
def use_key():
    import player
    import game
    #if not player.current_room["kirills office"]: #For some reason this isnt working I hate python !! This if statement will now return false.
    if player.current_room["name"].lower() != "dragon room": 
        no_use()
    else:
        print("""\
        
        You put the key into the door and slowly turn it, you hear a satifying click as the lock slides back.
        As the door opens you are blinded by the light from outside. As you begin to leave you think back on the day and ponder. . .
        just how in the world did you tie yourself to the chair like that? What, you think someone tied you up? No one would do that . . . """)

        time.sleep(4)
        print("""
        'Oh well' you think, 'at least I got to kirill a troll'.""")
        time.sleep(2)
        if len(player.quest) < 4:
            print("""
        Well, usually I would congratulate you on completing your quest, but you put in as much effort as one of our team mates.""")
        print(str("""
        Congratulations Player 1, you completed your quest to {}! I'm so proud of you\n""").format(player.quest))
        time.sleep(2)
        game.end()

def no_use():
    sass = ["You cannot use that item, dummy", "Much like you, that item is useless", "What's the point?", "What if I just don't let you? HA.", "Meh.", 
    "It's all about consumption with this generation", "I'd let you use it, but it'd just be another of earth's precious resources wasted.", "Another time perhaps.",
    "Find something better to do with your life."]
    print(sass[random.randrange(0, len(sass))])
    time.sleep(1.3)

def use_potion():
    import player
    print("\nYou drink the potion and it restores 1HP, it's expired, do you not even read expiry dates? You barbarian!")
    time.sleep(2)
    print("You drop the empty bottle and it lands on your toe. You lose 1HP")
    time.sleep(2)
    player.inventory.remove(item_potion)

def use_sword():
    import player
    import game
    if player.current_room["name"].lower() == "boss room":
        if player.current_room["boss_alive"] == True:
            print(""""\
                You attack the troll with a mighty swing of your sword. Mum would be proud.""")
            time.sleep(1.2)
            print("""\t
            Unfortunately, you aren't trained in swordfighting, and the troll now knows 
            this thanks to your god awful swing.
            The troll crushes your head in one blow and swings your body around the room, 
            painting the room in blood. Who knew trolls liked to decorate? """)
            time.sleep(3)
            game.end()
        else:
            print("\nYou stab the troll with the sword. Feels gross and altogether rather pointless.")
    else:
        no_use()

    

item_key = {
    "id": "key",

    "name": "a key",

    "description":
    """
    A key, artfully shaped into the likeness of a majestic dragon. It appears to be made of gold, well, at least you got some
    kind of wealth out of this.""",

    "use": "removeable", 

    "use_func": use_key # Don't put brackets here!
}

item_sword = {
    "id": "sword",

    "name": "a sword",

    "description":
    """
    The steel sword is adorned with the head of a wyvern with runes etched all along the blade. It must have been 
    beautiful in its time. It's not now, it's rusted so badly you've probaly already got tetanus, Congratulations!""",

    "use": "nope",

    "use_func": use_sword

}

item_potion = {
    "id": "potion",

    "name": "a health potion",

    "description":
    """
    The label reads this potion can restore 150hp, you also notice the expiry
    date is from 2 years ago.""",

    "use": "nope",

    #"gone" : 0, # Not sure if needed?
    #this key will be one or zero depending on if the item has been used up/ if out of the game yet

    "use_func": use_potion
}

item_book = {
    "id": "book",

    "name": "a python for dummies book",

    "description":
    """
    A dog eared papered back version for the key to success in python. The developers probably should have used this when they made this 
    game . . .""",

    "use": "nope",

    "use_func": no_use
}

item_laptop = {
    "id": "laptop",

    "name": "a laptop",

    "description":
    """
    The wallpaper is of a generic landscape. Inspiring.
    Displayed on the laptop screen is a file containing the answers for python lab 3, a recycling bin, and a folder marked... nevermind.""",

    "use": "nope",

    "use_func": no_use
}

item_prospectus = {
    "id": "prospectus",

    "name": "a prospectus",

    "description":
    """
    In bold writing on the cover of this prospectus reads "Thinking of studying computer science in cardiff university?" then in smaller writing below "why?" 
    You notice the stock photo of students on the front looks particularly painful. It's hard to tell if they are smiling or grimacing.""",
    #too much? or... - dervla

    "use": "nope",

    "use_func": no_use
}

item_armour = {
    "id": "armour",

    "name": "some chest armour",

    "description":
    """
    The rusted chestpiece is almost useless,
    the weight of the armour is too much for you and you fall to the ground.
    The rusted armour breaks on impact. You get a splinter in your finger.""",

    "use": "nope",

    "use_func": no_use


}

item_helmet = {
    "id": "helmet",

    "name": "a Warrior's helmet",

    "description":
    """
    Next to the chest armour you see a magnificent helmet carved out of ancient metal. It is calling for you.
    You put it on but your head is too small for it. That's suprising. I took you for the big headed type.""",

    "use": "nope",

    "use_func": no_use
}

item_note = {
    "id": "note",

    "name": "some crushed paper",

    "description":
    """
    You pick up the crushed piece of paper, there are notes left on the paper which reads.. i saw a bright light
    coming from the north east in the corridor, could it be something more?""",

    "use": "nope",

    "use_func": no_use
}

item_crown = {
    "id": "crown",

    "name": "a crown",

    "description":
    """
    You put the crown on, you look fabulous. Haha just kiding you look as stupid as ever. Take it off before 
    I laugh myself to death.""",

    "use": "nope",

    "use_func": no_use
}

item_coins = {
    "id": "coins",

    "name": "some gold coins",

    "description":
    """
    Modern currency doesn't allow for gold coins, these are useless.""",

    "use": "nope",

    "use_func": no_use
}

item_orb = {
    "id":"orb",

    "name": "a celestial sphere",

    "description":
    """
    A shiny looking orblike object. There are ancient carvings on it and illustrations to show how it can used""",
    
    "use": "nope",
    
    "use_func": no_use
    
}
