"""
save_load.py: Handles serialization and deserialization of game state.
"""
import json

def save_game(filename, player, world):
    """
    Save the current game state to a JSON file.
    """
    state = {
        'player': {
            'current_room_id': player.current_room_id,
            'inventory': player.inventory,
            'health': player.health,
            'sanity': player.sanity,
        },
        'flags': world.flags,
    }
    with open(filename, 'w') as f:
        json.dump(state, f)

def load_game(filename, player, world):
    """
    Load game state from a JSON file into player and world.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    pdata = data.get('player', {})
    player.current_room_id = pdata.get('current_room_id', player.current_room_id)
    player.inventory = pdata.get('inventory', [])
    player.health = pdata.get('health', player.health)
    player.sanity = pdata.get('sanity', player.sanity)
    world.flags = data.get('flags', world.flags)