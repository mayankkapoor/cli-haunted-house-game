"""
entities.py: Defines game entity classes like Item and Monster.
"""

class Item:
    """
    Represents an item in the game world.
    """
    def __init__(self, id, name, description, portable=True, usable_in=None, on_use=None):
        self.id = id
        self.name = name
        self.description = description
        self.portable = portable
        self.usable_in = usable_in or []
        self.on_use = on_use or {}

class Monster:
    """
    Represents a monster or NPC encounter.
    """
    def __init__(self, id, name, health, attack, encounter_chance, drops=None):
        self.id = id
        self.name = name
        self.health = health
        self.attack = attack
        self.encounter_chance = encounter_chance
        self.drops = drops or []