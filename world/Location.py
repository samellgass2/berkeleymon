"""Container to hold all of the elements of a particular location."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
import pyglet.gl as gl
from game_utils.Encounter import *
from data.Constants import *
from game_utils.Characters import *

#TODO: tune wild mons odd

class BoardTile:
    def __init__(self, sprite: pg.sprite.Sprite, enterable : list[bool], traversable : bool=False):
        """Initialize a board tile."""
        self.sprite = [sprite]
        self.traversable = traversable
        # a list of length 4 representing enterable from all directions [up, left, down, right]
        self.enterable = enterable
        self.x = sprite.x
        self.y = sprite.y

        self.location = None

    def update_pos(self, x, y):
        """Update the tiles position by updating the underlying sprites."""
        for icon in self.sprite:
            icon.x = x
            icon.y = y
        self.x = x
        self.y = y

    def offset_pos(self, x, y):
        """Offset the screen-space position of the sprites by (x,y)."""
        for icon in self.sprite:
            icon.x += x
            icon.y += y
        self.x += x
        self.y += y

    def set_batch(self, batches: list[graphics.Batch]):
        """Sets the batch of all sprites in ascending order of priority."""
        # Set it so that each sprite gets a higher priority batch up to the max number of batches.
        for i in range(len(self.sprite)):
            self.sprite[i].batch = batches[min(i, len(batches)-1)]

    def enter(self, direction: int):
        """Attempt to enter the tile's area from direction"""
        if self.enterable[direction]:
            # dispatch to game board that a new area has been entered, call to Location
            return

    def add_sprite(self, sprite: pg.sprite.Sprite):
        """Adds a sprite to the TOP layer by default."""
        self.sprite.append(sprite)

    def trigger(self):
        """Triggers the interaction related to stepping on the given tile."""
        # If in view of trainer, trigger that behavior.
        return

class WildTile(BoardTile):
    """A BoardTile that may trigger wild pokemon encounters."""
    def __init__(self, sprite: pg.sprite.Sprite, enterable : list[bool], traversable : bool=False):
        super().__init__(sprite, enterable, traversable)

    def trigger(self):
        if np.random.random() <= WILD_PKMN_CHANCE:
            print("Wild pokemon found!")
            wild_pokemon = self.location.encounter()
            print(wild_pokemon.name)
            # TODO: implement battle to feed from HERE
            self.location.board.enter_wild_encounter(wild_pokemon)



class Location:
    """A representation of the entire location to be given to a GameBoard."""
    def __init__(self, width: int, height: int, indoors: bool=False, pkmn_generator: PokemonGenerator=None):
        """Initialize a game world location."""
        self.width = width
        self.height = height
        self.is_indoors = indoors
        self._area = []
        for i in range(self.height):
            self._area.append([None for i in range(self.width)])

        self.pkmn_generator = pkmn_generator
        self.board = None

    def set(self, x: int, y: int, tile: BoardTile):
        """Set the tile at (x,y) to be tile."""
        self._area[y][x] = tile
        tile.location = self

    def get(self, x : int, y : int):
        """SAFELY retrieve tile at (x,y) or EmptyTile if None."""
        if self.in_bounds(x,y):
            return self._area[y][x]
        else:
            return BoardTile(pg.sprite.Sprite(empty_space_img), enterable=[False, False, False, False], traversable=False)

    def in_bounds(self, x: int, y: int):
        """If some (x,y) is within the location-space."""
        return (x >= 0) and (x < self.width) and (y >= 0) and (y < self.height)

    def encounter(self):
        """Encounter a wild pokemon and triggers a battle."""
        if self.pkmn_generator is not None:
            wild_pkmn = self.pkmn_generator.encounter()
            return wild_pkmn


####### PLAYER ANIMATIONS IMPORT #######
walking_forward_1_img = pg.resource.image("sprites/lucas/lucas_walking_forward_1.png")
walking_forward_2_img = pg.resource.image("sprites/lucas/lucas_walking_forward_2.png")
walking_forward_3_img = pg.resource.image("sprites/lucas/lucas_walking_forward_3.png")
walking_forward_4_img = pg.resource.image("sprites/lucas/lucas_walking_forward_4.png")
WALK_FORWARD_ANI = pg.sprite.Sprite(pg.image.Animation.from_image_sequence([walking_forward_1_img,
                                                           walking_forward_2_img,
                                                           walking_forward_3_img,
                                                           walking_forward_4_img], duration=0.2, loop=True))

walking_left_1_img = pg.resource.image("sprites/lucas/lucas_walking_left_1.png")
walking_left_2_img = pg.resource.image("sprites/lucas/lucas_walking_left_2.png")
walking_left_3_img = pg.resource.image("sprites/lucas/lucas_walking_left_3.png")
walking_left_4_img = pg.resource.image("sprites/lucas/lucas_walking_left_4.png")
WALK_LEFT_ANI = pg.sprite.Sprite(pg.image.Animation.from_image_sequence([walking_left_1_img,
                                                           walking_left_2_img,
                                                           walking_left_3_img,
                                                           walking_left_4_img], duration=0.2, loop=True))

walking_right_1_img = pg.resource.image("sprites/lucas/lucas_walking_right_1.png")
walking_right_2_img = pg.resource.image("sprites/lucas/lucas_walking_right_2.png")
walking_right_3_img = pg.resource.image("sprites/lucas/lucas_walking_right_3.png")
walking_right_4_img = pg.resource.image("sprites/lucas/lucas_walking_right_4.png")
WALK_RIGHT_ANI = pg.sprite.Sprite(pg.image.Animation.from_image_sequence([walking_right_1_img,
                                                           walking_right_2_img,
                                                           walking_right_3_img,
                                                           walking_right_4_img], duration=0.2, loop=True))

walking_backward_1_img = pg.resource.image("sprites/lucas/lucas_walking_backward_1.png")
walking_backward_2_img = pg.resource.image("sprites/lucas/lucas_walking_backward_2.png")
walking_backward_3_img = pg.resource.image("sprites/lucas/lucas_walking_backward_3.png")
walking_backward_4_img = pg.resource.image("sprites/lucas/lucas_walking_backward_4.png")
WALK_BACKWARD_ANI =pg.sprite.Sprite(pg.image.Animation.from_image_sequence([walking_backward_1_img,
                                                           walking_backward_2_img,
                                                           walking_backward_3_img,
                                                           walking_backward_4_img], duration=0.2, loop=True))

sprint_forward_1_img = pg.resource.image("sprites/lucas/lucas_sprint_forward_1.png")
sprint_forward_2_img = pg.resource.image("sprites/lucas/lucas_sprint_forward_2.png")
sprint_forward_3_img = pg.resource.image("sprites/lucas/lucas_sprint_forward_3.png")
sprint_forward_4_img = pg.resource.image("sprites/lucas/lucas_sprint_forward_4.png")
SPRINT_FORWARD_ANI = pg.sprite.Sprite(pg.image.Animation.from_image_sequence([sprint_forward_1_img,
                                                           sprint_forward_2_img,
                                                           sprint_forward_3_img,
                                                           sprint_forward_4_img], duration=0.15, loop=True))

sprint_left_1_img = pg.resource.image("sprites/lucas/lucas_sprint_left_1.png")
sprint_left_2_img = pg.resource.image("sprites/lucas/lucas_sprint_left_2.png")
sprint_left_3_img = pg.resource.image("sprites/lucas/lucas_sprint_left_3.png")
sprint_left_4_img = pg.resource.image("sprites/lucas/lucas_sprint_left_4.png")
SPRINT_LEFT_ANI = pg.sprite.Sprite(pg.image.Animation.from_image_sequence([sprint_left_1_img,
                                                           sprint_left_2_img,
                                                           sprint_left_3_img,
                                                           sprint_left_4_img], duration=0.15, loop=True))

sprint_right_1_img = pg.resource.image("sprites/lucas/lucas_sprint_right_1.png")
sprint_right_2_img = pg.resource.image("sprites/lucas/lucas_sprint_right_2.png")
sprint_right_3_img = pg.resource.image("sprites/lucas/lucas_sprint_right_3.png")
sprint_right_4_img = pg.resource.image("sprites/lucas/lucas_sprint_right_4.png")
SPRINT_RIGHT_ANI = pg.sprite.Sprite(pg.image.Animation.from_image_sequence([sprint_right_1_img,
                                                           sprint_right_2_img,
                                                           sprint_right_3_img,
                                                           sprint_right_4_img], duration=0.15, loop=True))

sprint_backward_1_img = pg.resource.image("sprites/lucas/lucas_sprint_backward_1.png")
sprint_backward_2_img = pg.resource.image("sprites/lucas/lucas_sprint_backward_2.png")
sprint_backward_3_img = pg.resource.image("sprites/lucas/lucas_sprint_backward_3.png")
sprint_backward_4_img = pg.resource.image("sprites/lucas/lucas_sprint_backward_4.png")
SPRINT_BACKWARD_ANI =pg.sprite.Sprite(pg.image.Animation.from_image_sequence([sprint_backward_1_img,
                                                           sprint_backward_2_img,
                                                           sprint_backward_3_img,
                                                           sprint_backward_4_img], duration=0.15, loop=True))



FACING_FORWARD = pg.sprite.Sprite(pg.image.load("sprites/lucas/lucas_walking_forward_1.png"))
FACING_LEFT = pg.sprite.Sprite(pg.image.load("sprites/lucas/lucas_walking_left_1.png"))
FACING_RIGHT = pg.sprite.Sprite(pg.image.load("sprites/lucas/lucas_walking_right_1.png"))
FACING_BACKWARD = pg.sprite.Sprite(pg.image.load("sprites/lucas/lucas_walking_backward_1.png"))






####### LOCATION SPRITES IMPORT #######

### GRASS PATH ###
top_left_gp_img = pg.image.load("sprites/grass_path_top_left.png")
grass_path_top_left = pg.sprite.Sprite(top_left_gp_img)

top_middle_gp_img = pg.image.load("sprites/grass_path_top_middle.png")
grass_path_top_middle = pg.sprite.Sprite(top_middle_gp_img)

top_right_gp_img = pg.image.load("sprites/grass_path_top_right.png")
grass_path_top_right = pg.sprite.Sprite(top_right_gp_img)

gp_middle_left_img = pg.image.load("sprites/grass_path_middle_left.png")
grass_path_middle_left = pg.sprite.Sprite(gp_middle_left_img)

gp_middle_middle_img = pg.image.load("sprites/grass_path_middle_middle.png")
grass_path_middle_middle = pg.sprite.Sprite(gp_middle_middle_img)

gp_middle_right_img = pg.image.load("sprites/grass_path_middle_right.png")
grass_path_middle_right = pg.sprite.Sprite(gp_middle_right_img)

gp_bottom_left_img = pg.image.load("sprites/grass_path_bottom_left.png")
grass_path_bottom_left = pg.sprite.Sprite(gp_bottom_left_img)

gp_bottom_middle_img = pg.image.load("sprites/grass_path_bottom_middle.png")
grass_path_bottom_middle = pg.sprite.Sprite(gp_bottom_middle_img)

gp_bottom_right_img = pg.image.load("sprites/grass_path_bottom_right.png")
grass_path_bottom_right = pg.sprite.Sprite(gp_bottom_right_img)

wild_grass_img = pg.image.load("sprites/wild_grass.png")
wild_grass = pg.sprite.Sprite(wild_grass_img)

empty_space_img = pg.image.load("sprites/black.jpeg")
empty = pg.sprite.Sprite(empty_space_img)

####### HARD CODED LOCATIONS #######

### TEST LOC ###
# TODO: the test location is a 50 x 50 grass patch with appropriate edges.

# TODO: implement a few mons to test encounter behavior
flying_types = [mon for mon in POKEDEX_MAP.values() if mon.tier == 'S']
print([mon.name for mon in flying_types])
mon_odd = 1 / len(flying_types)
TEST_PKMN_AND_ODDS = [(mon, mon_odd) for mon in flying_types]
TEST_GENERATOR = PokemonGenerator(TEST_PKMN_AND_ODDS, 40, 50)

TEST_LOCATION = Location(50, 50, False, TEST_GENERATOR)

# Define edges appropriately
for i in range(1, 49):
    TEST_LOCATION.set(i, 0, BoardTile(pg.sprite.Sprite(gp_bottom_middle_img), enterable=[False, False, False, False], traversable=True))
    TEST_LOCATION.set(i, 49, BoardTile(pg.sprite.Sprite(top_middle_gp_img), enterable=[False, False, False, False], traversable=True))
    TEST_LOCATION.set(0, i, BoardTile(pg.sprite.Sprite(gp_middle_left_img), enterable=[False, False, False, False], traversable=True))
    TEST_LOCATION.set(49, i, BoardTile(pg.sprite.Sprite(gp_middle_right_img), enterable=[False, False, False, False], traversable=True))

# Define corners appropriately
TEST_LOCATION.set(0, 0, BoardTile(pg.sprite.Sprite(gp_bottom_left_img), enterable=[False, False, False, False], traversable=True))
TEST_LOCATION.set(49, 0, BoardTile(pg.sprite.Sprite(gp_bottom_right_img), enterable=[False, False, False, False], traversable=True))
TEST_LOCATION.set(49, 49, BoardTile(pg.sprite.Sprite(top_right_gp_img), enterable=[False, False, False, False], traversable=True))
TEST_LOCATION.set(0, 49, BoardTile(pg.sprite.Sprite(top_left_gp_img), enterable=[False, False, False, False], traversable=True))

# Define rest of space as middle
for i in range(1, 49):
    for j in range(1, 49):
        TEST_LOCATION.set(i, j,
                          BoardTile(pg.sprite.Sprite(gp_middle_middle_img),
                                    enterable=[False, False, False, False],
                                    traversable=True))
        if (i+j)>7 and (i + j) % 7 == 3 and i % 2 == 0 :
            TEST_LOCATION.set(i, j,
                              WildTile(pg.sprite.Sprite(gp_middle_middle_img),
                                        enterable=[False, False, False, False],
                                        traversable=True))
            TEST_LOCATION.get(i, j).add_sprite(pg.sprite.Sprite(wild_grass_img))

### TEST LOC ###

