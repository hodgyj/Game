#!/usr/bin/python3

import os
import time
from map import rooms
import player
from items import *
from gameparser import *
from deaths import *
from ascii_dragon import *
import random
from credits import *

# win_condition has been moved to items.py
#moved all item interactions (take drop use etc etc) to interaction.py - Why? 

def fail_conditions(current_room):

    # This function checks against all fail conditions and then after printing the fail condition quits the game.
    #global player.gibberish
    if player.gibberish >= 5: # checks for how many times people type in gibberish.
        print("""\
        Your continued presence within the dungeon has clearly addled your mind.
        In your newfound state of madness you begin to see what appears to be orderlys and a charming doctor melting into being from the walls.
        They approach carrying what appears to be a straight jacket whilst making calming sounds.""")
        choice = str(input("Would you like to accept the nice doctors sanity pills?: ")).lower()
        if choice == "yes" or choice == "y":
            player.gibberish = 0
            print("The pills slowly kick in and you feel a sense of euphoria. Time almost seems to reverse as the doctor disappears back into the wall.")
            main() # resets the game
        else:
            print("I guess those padded walls are fairly appealing. . .and comfy. . .")
            end() # quits the game



def boss_battle_drop():
    if player.current_room == rooms["boss"] and rooms["boss"]["boss_alive"]:
        for item in player.current_room["items"]:
            if item == item_sword:
                print("""\
                You drop the weapon and then bravely run away.
                The beast gives chases with an all-mighty roar! Unfortunately as he runs he fails to notice the recently deposited sword.
                He trips and stumbles over the blade, after a moments consideration about his new found ability to defy gravity the beast
                slams head first into a wall.
                As he falls you hear the sound of a metallic object skittering accross the floor.""")
                print("""
                Congratulations """ + player.name[:3] + ".. er.. I mean Player 1! You defeated the troll! And it needed so much skill from you.")
                player.current_room["items"].append(item_key)
                rooms["boss"]["boss_alive"] = False
                rooms["boss"]["description"] = """
                The room is slightly flooded with the slippery liquid you have found throughout, and across from you is a giant throne.
                The troll which was once sitting on the throne is now lying on the floor, after an unfortunate encounter with a wall."""
                item["name"] = "a bent sword"
                item["description"] = """
                The sword is even more damaged now, you just can't stop yourself breaking things, can you?"""
                # Maybe add description of damaged sword?
                time.sleep(3)
                break

def list_of_items(items):

    return ", ".join([i['name']for i in items]) #returns list of items by iterating over dictionary values

def print_room_items(room):

    if room["items"]: #checks if items list has any values
        print("There is " + list_of_items(room["items"]) + " here. \n") #if there are items then summon list function and prints each item

def print_inventory_items(items):
    
    if items: #if value true then
        print("You have " + list_of_items(player.inventory) + ".\n") #prints inventory list

def print_room(room):

    # Display room name
    print("\n" + room["name"].upper() + "\n")
    # Display room description
    print(room["description"] + "\n")

    if (room["items"] != []):
        print_room_items(room)

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
    # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        # Print the items in the room
        print("TAKE " + item["id"].upper() + " to take " + item["name"])


    for item in inv_items:
        print("DROP or USE " + item["id"].upper() + " to drop or use " + item["name"])
    print("You also might want to INSPECT stuff")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):

    return chosen_exit in exits

def execute_inspect(item_id):
    item_found = False
    if item_id == "floor":
        print(player.current_room["floor"])
    elif item_id == "ceiling":
        print(player.current_room["ceiling"])
    else:
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
    time.sleep(2) # Delay before prompting for next command
def execute_use(item_id):
    #This function is so that the player can use items for various functions
    if not (player.inventory):
        print("You have nothing in your inventory to use, perhaps your memory is failing you?")
    else:
        for item in player.inventory:
            if item['id'] == item_id:
                if item['use_func']():
                    if (item['use']) == "removeable":
                        player.inventory.remove(item)
                    break

        if item_id not in (item["id"]):
            print("You cannot use that.")

def execute_go(direction):

    if direction in player.current_room["exits"]:
        if player.current_room == rooms["dragon room"] and direction == "south":
            if not rooms["boss"]["boss_alive"] and not item_key in player.inventory:
                print("""
                    You missed the key. Oh come on, how the hell do you miss the ONLY thing you had to get? How incompetent can one person be?""") # Make harsher
                time.sleep(1)
            else:
                if item_key in player.inventory:
                    item_key["use_func"]()

                player.attempts += 1

                if player.attempts >= 7:
                    print("Alright fine! I'm done with you and I'm done with my clearly useless existence!")
                    time.sleep(2)
                    exit()
                else:
                    print(player.attempt_exit[player.attempts -1])
                    time.sleep(1)

        # Player asked if they want to enter boss room if they have no items
        elif player.current_room == rooms["corridor"] and direction == "north" and len(player.inventory) == 0 and rooms["boss"]["boss_alive"]:
            choice = str(input("You have no items.\nWould you like to enter the boss room empty handed?\n> ")).lower()
            if choice == "y" or choice == "yes":
                print("""You bravely challenge the beast to a duel. The troll crushes your head in one blow and swings your body around the room, 
                    painting the room in blood. Who knew trolls liked to decorate?""")
                time.sleep(3)
                end()
        elif player.current_room == rooms["boss"] and item_sword in player.inventory and rooms["boss"]["boss_alive"]:
            print("How do expect to run with that sword?")
            time.sleep(1.3)
        else:
            player.current_room = move(player.current_room["exits"], direction)
    else:
        print("You cannot go there. Do you SEE that in the options? Should have gone to specsavers.")

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
                if item["name"] == "a bent sword":
                    print("This sword is clearly damaged, why on earth would you want this?")
                    time.sleep(1)
                player.current_room["items"].remove(item) #removes from the room
                player.inventory.append(item) #adds to player inventory
                print("Took " + item["name"] + ".\n")
                time.sleep(0.5)
                break

        if item_id not in (item["id"]): #if item isn't found in list of takable items
            print("You cannot take that.")

def execute_drop(item_id):

    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
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

def options(now):
    if now == "Q":
        time.sleep(3)
        exit()
    elif now =="H":
        print("First, watch more monty python, then complete the hitchhikers guide to the galaxy text adventure. Come back and you will understand so much more."
            "\n\nSorry, that's about as much help as a game this sarcastic is really going to give.")

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] != "go" and player.current_room == rooms["treasure"]:
        import deaths
        kill_player()
        end()

    if command[0] == "go":
        if len(command) > 1:
            # Correct the player's input if they enter "north east" instead of "northeast"
            # in the corridor, or "south west" instead of "southwest" in the treasure room
            if player.current_room == rooms["corridor"] and len(command) == 3:
                if command[1] == "north" and command[2] == "east":
                    command[1] = "northeast"
            elif player.current_room == rooms["treasure"] and len(command) == 3:
                if command[1] == "south" and command[2] == "west":
                    command[1] = "southwest"
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
        user_input = str(input("Are you sure you want to give up and exit like a total failure?? YES or NO: ")).lower()
        if user_input == "yes" or user_input == "y":
            print("Just so you know, we are all angry AND dissapointed in you. tsk tsk.")
            options("Q")
        else:
            print("Good answer. Let's keep questing xD")
    elif command[0] == "jump":
        print("Wasn't that fun?")
    elif command[0] == "lick":
        print("...You are pretty weird aren't you. Anyway you've just been poisoned. Well done kid.")
        time.sleep(3)
        end()
    elif command[0] == "cry":
        print("You cannot see through your tears and stumble into your death.")
        time.sleep(3)
        end()
    elif command[0] == "shout":
        print("Good job, now the beast knows you're here. (This means you're definitely dead)")
        time.sleep(3)
        end()
    else:
        print("This makes no sense.")
        player.gibberish += 1

def menu(exits, room_items, inv_items):


    # Display menu
    print_menu(exits, room_items, inv_items)
    
    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):


    # Next room to go to
    return rooms[exits[direction]]

def end():
    now = input("""\
    _________ _______  __   __  _______    _______  __   __  _______  ______    __
    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  |  | 
    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  |  | 
    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ |  | 
    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  ||__| 
    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | | __  
    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_||__|
                                        


                                Q to quit or H for help """).upper()
    if now == "Q":
        roll_credits()
        print("\n\n................EXITING...............")
        exit()
    elif now =="H":
        print("First, watch more monty python, then complete the hitchhikers guide to the galaxy text adventure. Come back and you will understand so much more."
            "\n\nSorry, that's about as much help as a game this sarcastic is really going to give.")
        roll_credits()
        exit()
    else:
        roll_credits()
        exit()


# This is the entry point of our program
def main():
    try:
        rooms["armoury"]["ceiling"] = rooms["armoury"]["ceiling"].format(player.name)
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
    except KeyboardInterrupt:
        # When exception is keyboard interrupt, quit gracefully
        print("I'd have thought you'd put more effort in than that...")
        print("Exited game.")
        exit()
    except SystemExit:
        exit()
    except:
        names = ["James", "Luca", "Alastair", "Dervla", "Natalie", "Sam"]
        print("Ah, an error. " + names[random.randrange(0, len(names))] + " didn't code that bit properly.")
        exit()

if __name__ == "__main__":
    import os
    # Resizes the command window. Doesn't work on Linux but ah well
    # Commented as it breaks VSCode. Make sure it's uncommented for the final version
    #os.system('mode con: cols=180 lines=80')
    print_intro()
    main()

