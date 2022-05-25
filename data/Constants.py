"""Key constants across the game."""

TILE_WIDTH = 32
TILE_HEIGHT = 32

WILD_PKMN_CHANCE = 1 #0.15

TYPES = {
    0: "NORMAL",
    1: "FIGHTING",
    2: "FLYING",
    3: "POISON",
    4: "GROUND",
    5: "ROCK",
    6: "BUG",
    7: "GHOST",
    8: "STEEL",
    9: "FIRE",
    10: "WATER",
    11: "GRASS",
    12: "ELECTRIC",
    13: "PSYCHIC",
    14: "ICE",
    15: "DRAGON",
    16: "DARK"
}

# TODO: create dictionaries of stat tables as
    # move_table[pokemon] = dict[level, dict["stat", value]]
    # so that you can look up move_table[pokemon][level] to get the stat table

    # And same for learned moves at every level