"""A pseudorandom way to generate locations."""

# FOR ROUTES:
# Start with path:
    # path == width 2 / 3 dirt (or gravel, brick, etc.) road with some bias toward right/left and up
    # random walk w the distribution of the path, not allowing direct double back (always turning)
    # fill out a random amount to either side, maybe 5-15 tiles, add in trees, houses, water, etc.
    # fill in the path with trainers
    # fill in the sides with grass

# FOR CITIES:
# Start with layout:
    # generate a polygon grid or other shape ==> roads
    # populate roads EVENLY with houses and ONE pkmn center + store
    # populate ONE gym with random theme in (choices)
    # populate houses with random, deterministic innards with pointers from entryway tiles and back

