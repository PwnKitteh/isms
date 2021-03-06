from collections import OrderedDict
from player import Player
import world


def play():
    print("Welcome to the AP Lang philosophies text based adventure game!\n This is a program written by Jacob Bokor as an AP Lang final project. Your current options will be provided to you when in game. You play as a time traveling explorer, trekking through America across the ages. Good Luck!")
    world.load_tiles()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("Your journey has come to an early end!")


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
        
    if isinstance(room, world.church):  #need to add individual dialogue options for each location where dialogue is availible
        action_adder(actions, 'd', player.dialogueChurch, "Talk to child")
    if isinstance(room, world.benFranklin): 
        action_adder(actions, 'd', player.dialogueBen, "Talk to Ben Franklin")    
    if isinstance(room, world.romanticism):  
        action_adder(actions, 'd', player.dialogueIrving, "Talk to Washington Irving") 
        
    if isinstance(room, world.smallCafe):  
        action_adder(actions, 'd', player.dialogueTwain, "Talk to Mark Twain (Samuel Clemens)")
        
    if isinstance(room, world.westEgg):  
        action_adder(actions, 'd', player.dialogueFitzgerald, "Talk to F. Scott Fitzgerald") 
        
    if isinstance(room, world.museum):  
        action_adder(actions, 'd', player.dialogueCaulfield, "Talk to Holden Caulfield")      

    if world.tile_at(room.x, room.y - 1):
        action_adder(actions, 'n', player.move_north, "Go north")
    if world.tile_at(room.x, room.y + 1):
        action_adder(actions, 's', player.move_south, "Go south")
    if world.tile_at(room.x + 1, room.y):
        action_adder(actions, 'e', player.move_east, "Go east")
    if world.tile_at(room.x - 1, room.y):
        action_adder(actions, 'w', player.move_west, "Go west")
    if player.hp < 100:
        action_adder(actions, 'h', player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


play()
