"""
game_loop.py: Main REPL loop, command dispatch, and game flow.
"""
import sys

from parser import parse
from utils import print_colored, show_help
from save_load import save_game, load_game

def run(world, player):
    """
    Run the main game loop until player quits or game ends.
    """
    # Intro and initial room description
    current = world.get_room(player.current_room_id)
    print_colored('Welcome to *The Old Hollow Mansion*.', 'cyan')
    if current:
        print_colored(current.get('description', ''), 'cyan')

    while True:
        try:
            inp = input('> ')
        except (EOFError, KeyboardInterrupt):
            print()
            break
        action, args = parse(inp)
        if not action:
            continue
        # Command dispatch
        if action == 'look':
            room = world.get_room(player.current_room_id)
            if room:
                print_colored(room.get('description', ''), 'cyan')
        elif action == 'move':
            if not args:
                print_colored('Move where?', 'yellow')
            else:
                direction = args[0]
                room = world.get_room(player.current_room_id)
                exits = room.get('exits', {})
                if direction in exits:
                    player.current_room_id = exits[direction]
                    next_room = world.get_room(player.current_room_id)
                    print_colored(next_room.get('description', ''), 'cyan')
                else:
                    print_colored("You can't go that way.", 'yellow')
        elif action == 'inventory':
            if player.inventory:
                print_colored('You have: ' + ', '.join(player.inventory), 'green')
            else:
                print_colored('Your inventory is empty.', 'green')
        elif action == 'status':
            print_colored(f'Health: {player.health}, Sanity: {player.sanity}', 'green')
        elif action == 'take':
            if not args:
                print_colored('Take what?', 'yellow')
            else:
                item_id = args[0]
                room = world.get_room(player.current_room_id)
                if item_id in room.get('items', []):
                    player.inventory.append(item_id)
                    room['items'].remove(item_id)
                    print_colored(f'You take the {item_id}.', 'green')
                else:
                    print_colored("You don't see that here.", 'yellow')
        elif action == 'drop':
            if not args:
                print_colored('Drop what?', 'yellow')
            else:
                item_id = args[0]
                if item_id in player.inventory:
                    player.inventory.remove(item_id)
                    room = world.get_room(player.current_room_id)
                    room.setdefault('items', []).append(item_id)
                    print_colored(f'You drop the {item_id}.', 'green')
                else:
                    print_colored("You don't have that.", 'yellow')
        elif action == 'inspect':
            if not args:
                print_colored('Inspect what?', 'yellow')
            else:
                obj = args[0]
                # Check inventory first
                if obj in player.inventory:
                    item = world.get_item(obj)
                    if item:
                        print_colored(item.get('description', ''), 'cyan')
                        continue
                # Then room
                room = world.get_room(player.current_room_id)
                if obj in room.get('items', []):
                    item = world.get_item(obj)
                    if item:
                        print_colored(item.get('description', ''), 'cyan')
                        continue
                print_colored("You don't see that here.", 'yellow')
        elif action == 'use':
            # Placeholder for use logic
            print_colored('Nothing happens.', 'yellow')
        elif action == 'save':
            filename = args[0] if args else 'savegame.json'
            try:
                save_game(filename, player, world)
                print_colored(f'Game saved to {filename}.', 'green')
            except Exception as e:
                print_colored(f'Failed to save game: {e}', 'red')
        elif action == 'load':
            filename = args[0] if args else 'savegame.json'
            try:
                load_game(filename, player, world)
                print_colored(f'Game loaded from {filename}.', 'green')
            except Exception as e:
                print_colored(f'Failed to load game: {e}', 'red')
        elif action == 'help':
            cmd = args[0] if args else None
            show_help(cmd)
        elif action in ('quit', 'exit'):
            print_colored('Goodbye!', 'cyan')
            break
        else:
            print_colored("I don't understand that command.", 'yellow')
    # End of game loop
    print_colored('Thanks for playing!', 'cyan')