import os
import time
from map import rooms
import player
from items import * # Not sure if needed?
from gameparser import *
from deaths import *
from ascii_dragon import *
from interactions import *
import random

# win_condition has been moved to items.py
#moved all item interactions (take drop use etc etc) to interaction.py

def fail_conditions(current_room):

    # This function checks against all fail conditions and then after printing the fail condition quits the game.
    #global player.gibberish
    if player.gibberish >= 5: # checks for how many times people type in gibberish.
        print("""\
        Your continued presence within the dungeon has clearly addled your mind.
        In your newfound state of madness you begin to see what appear to be orderlys and a charming doctor melting into being from the walls.
        They approach carrying what appears to be a straight jacket whilst making calming sounds.""")
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
                The beast gives chases with an all-mighty roar! Unfortunately as he runs he fails to notice the recently deposited sword.
                He trips and stumbles over the blade, after a moments consideration about his new found ability to defy gravity the beast
                slams head first into the wall.
                as he falls you hear the sound of a metallic object skittering accross the floor.""")
                player.current_room["items"].append(item_key)
                rooms["boss"]["boss_alive"] = False
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
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

    if (room["items"] != []):
        print_room_items(room)

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):

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

    return chosen_exit in exits



def menu(exits, room_items, inv_items):


    # Display menu
    print_menu(exits, room_items, inv_items)
    #print (current_room)
    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):


    # Next room to go to
    return rooms[exits[direction]]

# This is the entry point of our program
def main():
    #try:
    # Main game loop
    while True:
        #Could we make the game fullscreen by default so the ascii art will work out and things?
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

def end():
    now = input("GAME OVER \n\n\n enter R to restart, Q to quit or H for help")
    if now == "Q":
        print(................EXITING...............)
        time.sleep(3)
        exit()
    elif now =="H":
        print("First, watch more monty python, then complete the hitchhikers guide to the galaxy text adventure. Come back and you will understand so much more."
            "\n\nSorry, that's about as much help as a game this sarcastic is really going to give.")
    elif now == "R":
        #restore game and restart somehow
def options(now):
    if now == "Q":
        print(................EXITING...............)
        time.sleep(3)
        exit()
    elif now =="H":
        print("First, watch more monty python, then complete the hitchhikers guide to the galaxy text adventure. Come back and you will understand so much more."
            "\n\nSorry, that's about as much help as a game this sarcastic is really going to give.")
    elif now == "R":
        #restore game and restart somehow

