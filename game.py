import os
import time
from map import rooms
import player
from items import * # Not sure if needed?
from gameparser import *
from deaths import *
from ascii_dragon import *
import random

# win_condition has been moved to items.py

def fail_conditions(current_room):

    # This function checks against all fail conditions and then after printing the fail condition quits the game.
    #global player.gibberish
    if player.gibberish >= 5: # checks for how many times people type in gibberish. 
        print("""\
        Your continued presence within the dungeon has clearly addled your mind.
        In your newfound state of madness you begin to see what appear to be orderlys and a charming doctor melting into being from the walls. 
        They approach carrying what appears to be a straitjacket whilst making calming sounds.""")
        choice = str(input("Would you like to accept the nice doctors sanity pills?: ")).lower()
        if choice == "yes" or choice == "y":
            player.gibberish = 0
            print("The pills slowly kick in and you feel a sense of euphoria. Time almost seems to reverse as the doctor dissapears back into the wall.")
            main() # resets the game 
        else:
            print("I guess those padded walls are fairly appealing. . .and comfy. . .")
            exit() # quits the game



def boss_battle_drop():
    if player.current_room == rooms["boss"] and rooms["boss"]["boss_alive"]:
        for item in player.current_room["items"]:
            if item == item_sword:
                print("""\
                You drop the weapon and then bravely run away.
                The beast gives chases with an allmighty roar! Unfortunately as he runs he fails to notice the recently deposited sword.
                He trips and stumbles over the blade, after a moments consideration about his new found ability to defy gravity the beast
                slams head first into the wall.
                as he falls you hear the sound of a metallic object skittering accross the floor.""")
                player.current_room["items"].append(item_key)
                rooms["boss"]["boss_alive"].append(False)
                break

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    return ", ".join([i['name']for i in items]) #returns list of items by iterating over dictionary values

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if room["items"]: #checks if items list has any values
        print("There is " + list_of_items(room["items"]) + " here. \n") #if there are items then summon list function and prints each item

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
    if items: #if value true then
        print("You have " + list_of_items(player.inventory) + ".\n") #prints inventory list

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

    if (room["items"] != []):
        print_room_items(room)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    if player.current_room == rooms["boss"] and rooms["boss"]["boss_alive"] == False:
        for direction in exits:
            print_exit(direction, exit_leads_to(exits, direction))
        for item in room_items:
            print("TAKE " + item["id"].upper() + " to take " + item["name"])
        for item in inv_items:
            print("DROP or USE " + item["id"].upper() + " to drop or use " + item["name"])
        print("What do you want to do?")
    else:
        for direction in exits:
        # Print the exit name and where it leads to
            print_exit(direction, exit_leads_to(exits, direction))

        for item in room_items:
        # Print the items in the room 
            print("TAKE " + item["id"].upper() + " to take " + item["name"])


        for item in inv_items:
            print("DROP or USE " + item["id"].upper() + " to drop or use " + item["name"])

        print("What do you want to do?")
    

def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits

def execute_inspect(item_id):
    item_found = False
    for item in player.inventory:
        if item["id"] == item_id:
            print(item["description"])
            item_found = True
            break
    for item in player.current_room["items"]:
        if item["id"] == item_id:
            print(item["description"])
            item_found = True
            break
    if item_found == False:
        print("You try looking for " + item_id + " here, but alas it appears to be absent!.")

def execute_use(item_id):
    #This function is so that the player can use items for various functions
    if not (player.inventory):
        print("You have nothing in your inventory to use, perhaps your memory is failing you?")
    else:
        for item in player.inventory:
            if item['id'] == item_id:
                if item['use_func'](): # Swapped these if statements around, so the item doesnt get removed if it isnt used
                    if (item['use']) == "removeable":
                        player.inventory.remove(item)
                    break

        if item_id not in (item["id"]):
            print("You cannot use that.")

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    #global player.current_room
    if direction in player.current_room["exits"]:
        if player.current_room == rooms["dragon room"] and direction == "south": # Player cannot go to exit
            
            if item_key in player.inventory:
                item_key["use_func"]()
            
            player.attempts += 1
            #print(player.attempt_exit[random.randrange(0, len(player.attempt_exit))])
            
            if player.attempts >= 7:
                print("Alright fine! I'm done with you and I'm done with my clearly useless existance!")
                time.sleep(2)
                exit()
            else:
                print(player.attempt_exit[player.attempts -1])

        # Player can't enter room if they have no items
        elif player.current_room == rooms["corridor"] and direction == "north" and len(player.inventory) == 0 and rooms["boss"]["boss_alive"] == True:
            print("You have no items. Is it really a good idea to go into a boss room empty handed?")
        else:
            player.current_room = move(player.current_room["exits"], direction)
    else:
        print("You cannot go there.")

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    if not (player.current_room["items"]): #checks if there is a value 
        print("There is nothing here to take") #if no value 
    else:
        for item in player.current_room["items"]: #itterates over items and compares values
            if item["id"] == item_id:
                player.current_room["items"].remove(item) #removes from the room
                player.inventory.append(item) #adds to player inventory
                break

        if item_id not in (item["id"]): #if item isn't found in list of takable items
            print("You cannot take that.")

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    # has_item = False
    # for item in inventory:
    #     if item["id"] == item_id:
    #         has_item = True
    #         current_room["items"].append(item)
    #         inventory.remove(item)
    #         print ("Dropped " + item_id + ".")
    #         break
    # if has_item == False: 
    #     print ("You cannot drop that.")
    # I kept this to explain why I changed it, the if function returns a boolean value of true or fale
    # using it in this manner is like doubling down on the statement, the below corrects it.

    if not (player.inventory): # checks for any value in inventory
        print("You have nothing to drop.")
    else: 
        for item in player.inventory: #checks against all values in dictionary
            if item["id"] == item_id:
                player.inventory.remove(item)
                player.current_room["items"].append(item)
                print("Dropped " + item_id + ".") #this is a nice bit I kept, good idea!
                boss_battle_drop()
                break

    if item_id not in (item["id"]): #this is a catch for when an item is not in the dictionary but the dictionary still have values
        print("You cannot drop that.")

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    #global player.gibberish
    if 0 == len(command):
        return
    
    if command[0] != "go" and player.current_room == rooms["treasure"]:
        import deaths
        kill_player()
 
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")
    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")
    elif command[0] == "exit":
        exit()

    else:
        print("This makes no sense.")
        player.gibberish += 1

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)
    #print (current_room)
    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

# This is the entry point of our program
def main():
    #try:
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        fail_conditions(player.current_room)
        print_room(player.current_room)
        print_inventory_items(player.inventory)
        
        # Show the menu with possible actions and ask the player
        command = menu(player.current_room["exits"], player.current_room["items"], player.inventory)

        # Execute the player's command
        execute_command(command)
        #time.sleep(1) #Give them time to read output?
    #except:
        #names = ["James", "Luca", "Alastair", "Dervla", "Natalie", "Sam", "Louie"]
        #print("Ah, an error. " + names[random.randrange(0, len(names))] + " didn't code that bit properly.")
        #exit()

if __name__ == "__main__":
    print_intro() 
    main()