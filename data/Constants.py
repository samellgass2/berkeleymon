"""Key constants across the game."""

REFRESH_RATE = 40 # denominator of FPS, 5 * max_moves per animation

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

# Effectiveness of type x on type y given as (x,y)
def EFFECTIVENESS(x, y):
    eff = 1
    # Normal type
    if x == 0:
        if y in (5,8):
            eff = 0.5
        elif y == 7:
            eff = 0
    # Fighting type
    elif x == 1:
        if y in (2,3,6,13):
            eff = 0.5
        elif y == 7:
            eff = 0
        elif y in (0, 5, 8, 14, 16):
            eff = 2
    # Flying type
    elif x == 2:
        if y in (5, 8, 12):
            eff = 0.5
        elif y in (1, 6, 11):
            eff = 2
    # Poison type
    elif x == 3:
        if y in (3,4,5,7):
            eff = 0.5
        elif y == 8:
            eff = 0
        elif y == 11:
            eff = 2
    # Ground type
    elif x == 4:
        if y in (6, 11):
            eff = 0.5
        elif y == 2:
            eff = 0
        elif y in (3, 5, 8, 9, 12):
            eff = 2
    # Rock type
    elif x == 5:
        if y in (1, 4, 8):
            eff = 0.5
        elif y in (2, 6, 9, 14):
            eff = 2
    # Bug type
    elif x == 6:
        if y in (1,2,3,7,8,9):
            eff = 0.5
        elif y in (11, 13, 16):
            eff = 2
    # Ghost type
    elif x == 7:
        if y == 0:
            eff = 0
        elif y == 16:
            eff = 0.5
        elif y in (7,13):
            eff = 2
    # Steel type
    elif x == 8:
        if y in (8,9,10,12):
            eff = 0.5
        elif y in (5, 14):
            eff = 2
    # Fire type
    elif x == 9:
        if y in (5, 9, 10, 15):
            eff = 0.5
        elif y in (6, 8, 11, 14):
            eff = 2
    # Water type
    elif x == 10:
        if y in (10, 11, 15):
            eff = 0.5
        elif y in (4,5,9):
            eff = 2
    # Grass type
    elif x == 11:
        if y in (2,3,6,8,9,11,15):
            eff = 0.5
        elif y in (4,5,10):
            eff = 2
    # Electric type
    elif x == 12:
        if y == 4:
            eff = 0
        elif y in (11, 12, 15):
            eff = 0.5
        elif y in (2, 10):
            eff = 2
    # Psychic type
    elif x == 13:
        if y == 16:
            eff = 0
        elif y == 13:
            eff = 0.5
        elif y in (0,3):
            eff = 2
    # Ice type
    elif x == 14:
        if y in (8,9,10,14):
            eff = 0.5
        elif y in (2,4,11,15):
            eff = 2
    # Dragon type
    elif x == 15:
        if y == 8:
            eff = 0.5
        if y == 15:
            eff = 2
    # Dark type
    elif x == 16:
        if y in (1,16):
            eff = 0.5
        elif y in (7,13):
            eff = 2

    return eff

STAT_MULTIPLIERS = {
    -6: -.25,
    -5: 2/7,
    -4: 1/3,
    -3: 2/5,
    -1: 2/3,
    0: 1,
    1: 3/2,
    2: 2,
    3: 5/2,
    4: 3,
    5: 3.5,
    6: 4
}
    # move_table[pokemon] = dict[level, dict["stat", value]]
    # so that you can look up move_table[pokemon][level] to get the stat table

    # And same for learned moves at every level