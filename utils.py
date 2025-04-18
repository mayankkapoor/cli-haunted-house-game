"""
utils.py: Helper functions for colored output and logging.
"""
import logging

try:
    from colorama import init as _colorama_init, Fore, Style
    _colorama_init(autoreset=True)
    COLORS = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
    }
except ImportError:
    COLORS = {}

def init_console(debug=False):
    """
    Initialize console logging and color support.
    """
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(message)s')

def print_colored(text, color=None):
    """
    Print text with optional color.
    """
    if color and color in COLORS:
        print(COLORS[color] + text + Style.RESET_ALL)
    else:
        print(text)

def show_help(command=None):
    """
    Display help text for commands.
    """
    commands = {
        'look': 'look (l): redisplay room description',
        'move': 'move <direction> (n,s,e,w): move between rooms',
        'inspect': 'inspect <object>: show detailed description',
        'take': 'take <item>: pick up an item',
        'drop': 'drop <item>: drop an item',
        'use': 'use <item> [on <target>]: use an item',
        'inventory': 'inventory (i): list items',
        'status': 'status: show health & sanity',
        'save': 'save [filename]: save game',
        'load': 'load [filename]: load game',
        'help': 'help [command]: show help',
        'quit': 'quit: exit game',
        'exit': 'exit: exit game',
    }
    if not command:
        print('Available commands:')
        for desc in commands.values():
            print(f'  {desc}')
    else:
        desc = commands.get(command, f'No help available for "{command}"')
        print(desc)