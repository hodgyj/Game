#split game file for clarification
#this file will contain all users interactions with items
#game.py will contain everything else


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
            choice = str(input("You have no items.\nWould you like to enter the boss room empty handed?\n> ")).lower()
            if choice == "y" or choice == "yes":
                print("""You bravely challenge the beast to a duel. The troll crushes your head in one blow and swings your body around the room, 
                    paining the room in blood. Who knew trolls liked to decorate?""")
                time.sleep(3)
                exit()
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
        user_input = input("Are you sure you want to give up and exit like a total failure?? YES or NO")
        user_input = normalise_input(user_input)
        if input == "yes" or "y":
            print("Just so you know, we are all angry AND dissapointed in you. tsk tsk. \n\n GAME EXITING NOW")
            options("Q")
        else:
            print("Good answer. Let's keep questing xD")
    elif command[0] == "jump":
        print("Wasn't that fun?")
    elif command[0] == "cry":
        print("You cannot see through your tears and stumble into your death.")
        time.sleep(4)

    elif command[0] == "shout":
        print("Good job, now the beast knows you're here. (This means you're definitely dead)")
        exit()
    else:
        print("This makes no sense.")
        player.gibberish += 1