"""Screen and Visible World."""

from world.Location import *
import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
import pyglet.gl as gl
from data.Constants import *

class GameBoard:
    """The Visible Area."""

    def __init__(self, location : Location, player_x : int, player_y : int, player_trainer: PokemonTrainer = None):
        self.width = 24
        self.height = 16
        self._board = []
        for i in range(self.height):
            self._board.append([None for i in range(self.width)])

        self.batches = []
        self.back_batch = graphics.Batch()
        self.front_batch = graphics.Batch()
        self.batches.extend([self.back_batch, self.front_batch])

        ### relationship to given location ###
        self.location = location
        self.location.board = self
        # Player is centered relative to the screen
        self.bottom_left = (player_x - self.width // 2, player_y - self.height // 2)

        ### player params ###
        self.player_loc = (player_x, player_y)
        self.player_last_facing = 2
        self.player_facing = 2
        self.player_heading = -1
        self.player_sprinting = False
        self.player_icon = FACING_FORWARD
        self.player_trainer = player_trainer

        ### animation params ###
        self.move_offset = 0
        self.max_moves = 8

        # TODO: dispatch battle UI, keep track of player's mons as the TRAINER class

        ### render mode boolean flags ###
        self.in_overworld = True
        self.current_encounter = None

        self.populate_board()

    ### DISPATCH ENCOUNTER ###
    def enter_wild_encounter(self, wild_pokemon: Pokemon):
        """Enters an encounter with a wild pokemon"""
        self.in_overworld = False
        self.current_encounter = Battle(self.player_trainer, [wild_pokemon], self)

    def enter_trainer_encounter(self, trainer: PokemonTrainer):
        """Enters an encounter with a trainer"""
        self.in_overworld = False
        self.current_encounter = Battle(self.player_trainer, trainer, self)

    def exit_encounter(self):
        """Exits an encounter of either type"""
        self.location.board.in_overworld = True
        self.current_encounter = None


    def get(self, x: int, y: int):
        """Get sprite at board (x,y)."""
        return self._board[y][x]

    def set(self, x: int, y: int, sprite: pg.sprite.Sprite):
        """Set board (x,y) as sprite."""
        self._board[y][x] = sprite

    def populate_board(self):
        """Grabs the w x h tiles from Location necessary to fill screen."""

        # Else render environment dynamically
        self.batches = [graphics.Batch() for i in range(len(self.batches))]
        for j in range(self.height):
            for i in range(self.width):
                # Convert from screen space to location space
                loc_x = self.bottom_left[0] + i
                loc_y = self.bottom_left[1] + j
                self.set(i, j, self.location.get(loc_x, loc_y))

                # Tell tile's sprite where it is
                tile = self.get(i, j)
                tile.update_pos(i * TILE_WIDTH, j * TILE_HEIGHT)
                tile.set_batch(self.batches)

    def transition_board(self, offset: float):
        """Moves all tiles by offset parts of a tile."""
        # Do not move environment if indoors
        if self.location.is_indoors:
            return
        # Else transition tiles
        offset_tup = (0,0)
        extra_tiles = []
        if self.player_heading == 0 and self.can_move(self.player_loc[0], self.player_loc[1]+1, 0):
            offset_tup = (0, -offset*TILE_HEIGHT)

            for x in range(self.bottom_left[0],self.bottom_left[0] + self.width):
                new_tile = self.location.get(x, self.bottom_left[1]+self.height)
                sister_tile = self.get((x-self.bottom_left[0]), self.height-1)
                new_tile.update_pos(sister_tile.x, sister_tile.y + TILE_HEIGHT)

                new_tile.set_batch(self.batches)
                extra_tiles.append(new_tile)

        elif self.player_heading == 1 and self.can_move(self.player_loc[0]+1, self.player_loc[1], 1):
            offset_tup = (-offset*TILE_WIDTH, 0)

            for y in range(self.bottom_left[1],self.bottom_left[1] + self.height):
                new_tile = self.location.get(self.bottom_left[0]+self.width, y)
                sister_tile = self.get(self.width - 1, (y-self.bottom_left[1]))
                new_tile.update_pos(sister_tile.x + TILE_WIDTH, sister_tile.y)

                new_tile.set_batch(self.batches)
                extra_tiles.append(new_tile)

        elif self.player_heading == 2 and self.can_move(self.player_loc[0], self.player_loc[1]-1, 2):
            offset_tup = (0, offset*TILE_HEIGHT)

            for x in range(self.bottom_left[0],self.bottom_left[0] + self.width):
                new_tile = self.location.get(x, self.bottom_left[1]-1)
                sister_tile = self.get((x - self.bottom_left[0]), 0)
                new_tile.update_pos(sister_tile.x, sister_tile.y - TILE_HEIGHT)
                new_tile.set_batch(self.batches)
                extra_tiles.append(new_tile)

        elif self.player_heading == 3 and self.can_move(self.player_loc[0]-1, self.player_loc[1], 3):
            offset_tup = (offset*TILE_WIDTH, 0)

            for y in range(self.bottom_left[1],self.bottom_left[1] + self.height):
                new_tile = self.location.get(self.bottom_left[0]-1, y)
                sister_tile = self.get(0, y - self.bottom_left[1])
                new_tile.update_pos(sister_tile.x - TILE_WIDTH, sister_tile.y)

                new_tile.set_batch(self.batches)
                extra_tiles.append(new_tile)

        for j in range(self.height):
            for i in range(self.width):
                # Tell tile's sprite where it is
                tile = self.get(i, j)
                tile.offset_pos(offset_tup[0], offset_tup[1])

        for tile in extra_tiles:
            tile.offset_pos(offset_tup[0], offset_tup[1])

        for batch in self.batches:
            batch.draw()

    def in_bounds(self, direction):
        """Bool, (x,y) in bounds of location."""
        if direction == 0:
            return self.location.in_bounds(self.bottom_left[0], self.bottom_left[1]+1+self.height)
        elif direction == 1:
            return self.location.in_bounds(self.bottom_left[0]+1+self.width, self.bottom_left[1])
        elif direction == 2:
            return self.location.in_bounds(self.bottom_left[0], self.bottom_left[1]-1)
        elif direction == 3:
            return self.location.in_bounds(self.bottom_left[0]-1, self.bottom_left[1])

    def can_move(self, x: int, y: int, direction):
        """Bool, player may move to (x,y)."""
        if self.location.in_bounds(x, y):
            tile = self.location.get(x,y)
            return tile is not None and tile.traversable
        return False

    def can_enter(self, x: int, y: int, direction: int):
        """Bool, player may enter (x,y)."""
        if self.location.in_bounds(x,y):
            tile = self.location.get(x,y)
            return tile is not None and tile.enterable[direction]
        return False


    def move(self, direction: int):
        """Given a direction, moves the player in that direction.

        Skeleton:
        for all directions:
            if moving there is a legal move,
            set player to face that way
            if that tile is a door, enter new area
            trigger any action corresponding to that tile
            if outdoors:
                Update player location, update screen location and repopulate board tiles, moving environment.
            if indoors:
                Update player location, do NOT update screen and repopulate, moving player.
        """

        # case up
        if direction==0:
            if self.can_move(self.player_loc[0], self.player_loc[1]+1, direction):

                self.player_facing = direction
                # Entering logic
                if self.can_enter(self.player_loc[0], self.player_loc[1]+1, direction):
                    self.location.get(self.player_loc[0], self.player_loc[1]+1).enter()
                self.player_loc = (self.player_loc[0], self.player_loc[1]+1)
                # If outdoors, move screen, else keep static
                if not self.location.is_indoors:
                    self.bottom_left = (self.bottom_left[0], self.bottom_left[1]+1)
                # Trigger any events relative to that tile
                self.location.get(self.player_loc[0], self.player_loc[1]).trigger()
                # Re-render
                self.populate_board()
        # case left
        elif direction==1:
            if self.can_move(self.player_loc[0]+1, self.player_loc[1], direction):

                self.player_facing = direction
                if self.can_enter(self.player_loc[0]+1, self.player_loc[1], direction):
                    self.location.get(self.player_loc[0]+1, self.player_loc[1]).enter()
                self.player_loc = (self.player_loc[0]+1, self.player_loc[1])
                if not self.location.is_indoors:
                    self.bottom_left = (self.bottom_left[0]+1, self.bottom_left[1])
                self.location.get(self.player_loc[0], self.player_loc[1]).trigger()
                self.populate_board()
        # case down
        if direction==2:
            if self.can_move(self.player_loc[0], self.player_loc[1]-1, direction):

                self.player_facing = direction
                if self.can_enter(self.player_loc[0], self.player_loc[1]-1, direction):
                    self.location.get(self.player_loc[0], self.player_loc[1]-1).enter()
                self.player_loc = (self.player_loc[0], self.player_loc[1]-1)
                if not self.location.is_indoors:
                    self.bottom_left = (self.bottom_left[0], self.bottom_left[1]-1)
                self.location.get(self.player_loc[0], self.player_loc[1]).trigger()
                self.populate_board()
        # case right
        if direction==3:
            if self.can_move(self.player_loc[0] - 1, self.player_loc[1], direction):

                self.player_facing = direction
                if self.can_enter(self.player_loc[0]-1, self.player_loc[1], direction):
                    self.location.get(self.player_loc[0]-1, self.player_loc[1]).enter()
                self.player_loc = (self.player_loc[0]-1, self.player_loc[1])
                if not self.location.is_indoors:
                    self.bottom_left = (self.bottom_left[0]-1, self.bottom_left[1])
                self.location.get(self.player_loc[0], self.player_loc[1]).trigger()
                self.populate_board()


    def render_board(self, dt=None):
        """Draws the board's tiles to the screen"""
        for batch in self.batches:
            batch.draw()

        if self.location.is_indoors:
            self.player_icon.x = (self.player_loc[0] - self.bottom_left[0]) * TILE_WIDTH
            self.player_icon.y = (self.player_loc[1] - self.bottom_left[1]) * TILE_HEIGHT
        else:
            self.player_icon.x = self.width//2 *TILE_WIDTH
            self.player_icon.y =self.height//2 *TILE_HEIGHT
        self.player_icon.draw()

        ### for debugging, check on sprites ###
        # for j in range(self.height):
        #     for i in range(self.width):
        #         print(self.get(i, j).sprite, self.get(i, j).sprite.x, self.get(i, j).sprite.y)


    def render_indoors(self, dt=None):
        for batch in self.batches:
            batch.draw()


    def update_state(self, dt):
       if self.in_overworld:
           self.overworld_update()
       else:
           self.current_encounter.update()


    def overworld_update(self):
        # Case currently moving
        if self.player_heading > -1:
            if self.move_offset < self.max_moves:
                self.transition_board(1 / self.max_moves)
                self.move_offset += 1
            else:
                self.move(self.player_heading)
                self.move_offset = 0

            # Case sprinting: move twice as much
            if self.player_sprinting:
                if self.move_offset < self.max_moves:
                    self.transition_board(1 / self.max_moves)
                    self.move_offset += 1
                else:
                    self.move(self.player_heading)
                    self.move_offset = 0

        # Case movement ended, lock to next square
        elif self.move_offset > 0:
            while self.move_offset < self.max_moves:
                self.transition_board(1 / self.max_moves)
                self.move_offset += 1
            self.move_offset = 0
            self.move(self.player_last_facing)


    def update_player_icon(self, dt=None):
        # No movement, statics
        if self.player_heading < 0:
            if self.player_facing == 0:
                self.player_icon = FACING_BACKWARD
            elif self.player_facing == 1:
                self.player_icon = FACING_RIGHT
            elif self.player_facing == 2:
                self.player_icon = FACING_FORWARD
            elif self.player_facing == 3:
                self.player_icon = FACING_LEFT
        # Sprinting animations
        if self.player_sprinting:
            if self.player_heading == 0:
                self.player_icon = SPRINT_BACKWARD_ANI
            elif self.player_heading == 1:
                self.player_icon = SPRINT_RIGHT_ANI
            elif self.player_heading == 2:
                self.player_icon = SPRINT_FORWARD_ANI
            elif self.player_heading == 3:
                self.player_icon = SPRINT_LEFT_ANI
        # Walking animations
        elif self.player_heading == 0:
            self.player_icon = WALK_BACKWARD_ANI
        elif self.player_heading == 1:
            self.player_icon = WALK_RIGHT_ANI
        elif self.player_heading == 2:
            self.player_icon = WALK_FORWARD_ANI
        elif self.player_heading == 3:
            self.player_icon = WALK_LEFT_ANI


