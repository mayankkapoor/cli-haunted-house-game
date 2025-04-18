#!/usr/bin/env python3
"""
Entry point for the Haunted House CLI game.
"""
import argparse

from utils import init_console, print_colored
from world import World
from player import Player
from save_load import load_game
from game_loop import run as game_loop_run


def main():
    parser = argparse.ArgumentParser(
        description='Haunted House Adventure'
    )
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('--load', type=str, help='Load saved game file')
    args = parser.parse_args()

    init_console(debug=args.debug)

    # Load world and player
    world = World()
    player = Player(starting_room=world.starting_room_id)

    # Load saved game if requested
    if args.load:
        try:
            load_game(args.load, player, world)
            print_colored(f'Loaded game from {args.load}', 'green')
        except Exception as e:
            print_colored(f'Failed to load game: {e}', 'red')

    # Start game loop
    game_loop_run(world, player)


if __name__ == '__main__':
    main()