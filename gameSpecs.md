## 1. Purpose & Scope

- **Objective**: Define detailed requirements for a command‑line haunted house adventure game. These requirements will serve as input to an LLM for automated code generation.
- **Audience**: Developers or LLMs producing the game code.
- **Platform**: Cross‑platform CLI (Windows, macOS, Linux).

## 2. Non‑Functional Requirements

1. **Language**: Python 3.8+ (or specify another mainstream language).
2. **Dependencies**: Only standard library modules (e.g., `json`, `os`, `random`, `sys`), plus optional `colorama` for colored output.
3. **Performance**: Instant response (<100 ms) for user commands.
4. **Extensibility**: Data‑driven design using external JSON/YAML for rooms, items, and events.
5. **Error Handling**: Graceful handling of invalid commands with user‑friendly messages.
6. **Logging**: Verbose debug logging toggle via command‑line flag.

## 3. Game Concept & Story

- **Setting**: A decrepit, multi‑room haunted mansion at midnight.
- **Goal**: Escape the house before dawn by solving puzzles and avoiding supernatural dangers.
- **Narrative Hooks**:
  - Mysterious whispers lead to clues.
  - Flashback notes reveal backstory of a missing family.
  - Multiple endings based on items found and choices made.

## 4. Game World & Layout

- **Topology**: Graph of rooms interconnected by named exits (e.g., `north`, `east`, `secret hatch`).
- **Room Attributes**:
  - `id`: unique key
  - `name`
  - `description`
  - `exits`: mapping of direction strings to target room IDs
  - `items`: list of item IDs present
  - `features`: optional triggers (e.g., trapdoor, painting)

## 5. Game Mechanics

### 5.1 Player State
- **Attributes**:
  - `current_room_id`
  - `inventory`: list of item IDs
  - `health`: integer (e.g., 100 max)
  - `sanity`: integer (0–100)
  - `flags`: key‑value store for story triggers

### 5.2 Items & Puzzles
- **Item Schema**:
  - `id`, `name`, `description`, `portable`: bool, `usable_in`: list of room or feature IDs, optional `on_use` effect
- **Puzzles**: Defined by feature triggers that check player flags or inventory, unlocking new exits or revealing items.

### 5.3 Encounters & Random Events
- **Monsters/NPCs**:
  - Schema: `id`, `name`, `health`, `attack`, `encounter_chance`, `drops`
  - Behavior: Either combat (simple turn‑based) or stealth avoidance (random check + sanity penalty)
- **Random Events**:
  - Occur on room entry: e.g., flickering lights, sudden cold spots (adjust sanity).

## 6. CLI Interface & Commands

- **Command Parser**: Split input by whitespace, support synonyms (e.g., `n`/`north`).
- **Basic Commands**:
  - `look` (or `l`): redisplay room description
  - `move <direction>` (or single‑letter alias)
  - `inspect <object>`: show detailed description
  - `take <item>` / `drop <item>`
  - `use <item> [on <target>]`
  - `inventory` (or `i`)
  - `status`: show health & sanity
  - `save [filename]`, `load [filename]`
  - `help [command]`
  - `quit` / `exit`

- **Feedback**: Colorized text (e.g., red for danger, green for success).

## 7. Data Structures & File Formats

- **World Definition**: JSON file `rooms.json` containing room objects.
- **Items Definition**: JSON file `items.json`.
- **Monsters Definition**: JSON file `monsters.json`.
- **Save File**: JSON representing player state and current world flags.

## 8. Core Modules

- `main.py`: entry point; initializes game, handles save/load flags.
- `game_loop.py`: runs REPL, dispatches commands, advances game state.
- `parser.py`: tokenizes and interprets user input into actions.
- `world.py`: loads and manages rooms, items, and events.
- `player.py`: defines player class, stats, inventory methods.
- `entities.py`: defines item, monster, and puzzle feature classes.
- `combat.py`: handles encounter resolution and random events.
- `save_load.py`: serializes/deserializes game state.
- `utils.py`: helper functions (e.g., colored output, logging).

## 9. Game Loop & Flow

1. **Startup**: Load definitions, parse CLI flags, load saved game if requested.
2. **Intro**: Display prologue text.
3. **REPL**:
   - Prompt: `> `
   - Read command → parse → execute → update state → print result → check win/lose conditions.
4. **Termination**: On exit or game over, display epilogue and exit.

## 10. Example Interaction

```text
Welcome to *The Old Hollow Mansion*.
You stand in the dusty foyer. Exits: north, east.
> n
You enter the grand hall… (random cold spot chills you! Sanity -5)
> inspect painting
A portrait of a stern matron. Her eyes seem to follow you.
> use key on painting
You hear a click; a secret door opens to the west.
```

## 11. Extensibility & Customization

- Support loading alternate world/data packs.
- Plugin system for new puzzles, items, or NPC scripts.

## 12. Testing & Validation

- Unit tests for parser, save/load, and core mechanics.
- Sample game scripts for integration testing.

## 13. Deliverables

- Fully functional codebase matching above modules.
- Sample JSON data for rooms, items, monsters.
- README with setup and play instructions.

