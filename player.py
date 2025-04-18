"""
player.py: Defines the Player class for tracking player state.
"""

class Player:
    """
    Represents the player, including current location, inventory, and stats.
    """
    def __init__(self, starting_room):
        self.current_room_id = starting_room
        self.inventory = []
        self.health = 100
        self.sanity = 100