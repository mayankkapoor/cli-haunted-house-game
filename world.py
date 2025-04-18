"""
world.py: Loads and manages game world definitions (rooms, items, monsters) and state flags.
"""
import json
import os

class World:
    """
    Represents the game world, including rooms, items, monsters, and story flags.
    """
    def __init__(self,
                 rooms_file='rooms.json',
                 items_file='items.json',
                 monsters_file='monsters.json'):
        self.flags = {}
        self.rooms = {}
        self.items = {}
        self.monsters = {}
        self.starting_room_id = None
        self.load_rooms(rooms_file)
        self.load_items(items_file)
        self.load_monsters(monsters_file)

    def load_rooms(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Rooms file not found: {filepath}')
        with open(filepath, 'r') as f:
            data = json.load(f)
        for room in data:
            self.rooms[room['id']] = room
        if data:
            # First room in file is starting location
            self.starting_room_id = data[0]['id']

    def load_items(self, filepath):
        if not os.path.exists(filepath):
            return
        with open(filepath, 'r') as f:
            data = json.load(f)
        for item in data:
            self.items[item['id']] = item

    def load_monsters(self, filepath):
        if not os.path.exists(filepath):
            return
        with open(filepath, 'r') as f:
            data = json.load(f)
        for m in data:
            self.monsters[m['id']] = m

    def get_room(self, room_id):
        return self.rooms.get(room_id)

    def get_item(self, item_id):
        return self.items.get(item_id)