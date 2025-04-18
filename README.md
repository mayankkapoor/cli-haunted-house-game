# Haunted House CLI Game

A text-based haunted house adventure game playable in the command line.

Escape *The Old Hollow Mansion* before dawn by exploring rooms, solving puzzles, and managing your sanity.

## Requirements
- Python 3.8+
- Optional: `colorama` for colored output (`pip install colorama`)

## Running
```sh
python main.py [--debug] [--load <savefile>]
```

## Controls
- `look` (`l`): redisplay room description
- `move <direction>` (`n`, `s`, `e`, `w`): move between rooms
- `inspect <object>`: show detailed description
- `take <item>`: pick up an item
- `drop <item>`: drop an item
- `use <item> [on <target>]`: use an item
- `inventory` (`i`): list items
- `status`: show health & sanity
- `save [filename]`: save game
- `load [filename]`: load game
- `help [command]`: show help
- `quit` / `exit`: exit game

## Data Files
- `rooms.json`: defines rooms
- `items.json`: defines items
- `monsters.json`: defines monsters

## Extending the Game
Customize the JSON files to add new rooms, items, monsters, and features to your haunted mansion.