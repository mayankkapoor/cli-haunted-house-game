"""
parser.py: Tokenizes and interprets user input into actions.
"""
# Mapping of input synonyms to standardized actions and arguments
SYNONYMS = {
    'n': ['move', 'north'],
    's': ['move', 'south'],
    'e': ['move', 'east'],
    'w': ['move', 'west'],
    'north': ['move', 'north'],
    'south': ['move', 'south'],
    'east': ['move', 'east'],
    'west': ['move', 'west'],
    'l': ['look'],
    'look': ['look'],
    'i': ['inventory'],
    'inventory': ['inventory'],
}

def parse(command_str):
    """
    Parse a raw command string into an action and list of arguments.
    Returns (action, args).
    """
    tokens = command_str.strip().split()
    if not tokens:
        return None, []
    key = tokens[0].lower()
    if key in SYNONYMS:
        mapping = SYNONYMS[key]
        action = mapping[0]
        args = mapping[1:] + tokens[1:]
    else:
        action = key
        args = tokens[1:]
    return action, args