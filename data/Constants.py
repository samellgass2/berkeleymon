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

TYPE_TO_COLOR = {
    0: (168, 167, 122),
    1: (194, 46, 40),
    2: (169, 143, 243),
    3: (163, 62, 161),
    4: (226, 191, 101),
    5: (182, 161, 54),
    6: (166, 185, 26),
    7: (115, 87, 151),
    8: (183, 183, 206),
    9: (238, 129, 48),
    10: (99, 144, 240),
    11: (122, 199, 76),
    12: (247, 208, 44),
    13: (249, 85, 135),
    14: (150, 217, 214),
    15: (111, 53, 252),
    16: (112, 87, 70)
}

# TODO: create dictionaries of stat tables as
    # move_table[pokemon] = dict[level, dict["stat", value]]
    # so that you can look up move_table[pokemon][level] to get the stat table

    # And same for learned moves at every level