"""Screen and Visible World."""

from world.Location import *
import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
import pyglet.gl as gl

TILE_WIDTH = 32
TILE_HEIGHT = 32

class GameBoard:
    """The Visible Area."""

    def __init__(self, location : Location, player_x : int, player_y : int):
        self.width = 24
        self.height = 16
        self.in_encounter = False
        self._board = []
        for i in range(self.height):
            self._board.append([None for i in range(self.width)])

        self.batch = graphics.Batch()

        ### relationship to given location ###
        self.location = location
        # Player is centered relative to the screen
        self.bottom_left = (player_x - self.width // 2, player_y - self.height // 2)

        ### player params ###
        self.player_loc = (player_x, player_y)
        self.player_facing = 2
        self.player_heading = -1
        self.player_sprinting = False
        self.player_icon = FACING_FORWARD

        self.populate_board()

    def get(self, x: int, y: int):
        """Get sprite at board (x,y)."""
        return self._board[y][x]

    def set(self, x: int, y: int, sprite: pg.sprite.Sprite):
        """Set board (x,y) as sprite."""
        self._board[y][x] = sprite

    def populate_board(self):
        """Grabs the w x h tiles from Location necessary to fill screen."""
        self.batch = graphics.Batch()
        for j in range(self.height):
            for i in range(self.width):
                # Convert from screen space to location space
                loc_x = self.bottom_left[0] + i
                loc_y = self.bottom_left[1] + j
                self.set(i, j, self.location.get(loc_x, loc_y))

                # Tell tile's sprite where it is
                tile = self.get(i, j)
                if tile is not None:
                    tile.update_pos(i * TILE_WIDTH, j * TILE_HEIGHT)
                    tile.set_batch(self.batch)

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
            if that tile is a door, enter new area.
            if not, update player location, update screen location and repopulate board tiles.
        """

        # case up
        if direction==0:
            if self.can_move(self.player_loc[0], self.player_loc[1]+1, direction):
                self.player_facing = direction
                if self.can_enter(self.player_loc[0], self.player_loc[1]+1, direction):
                    self.get(self.player_loc[0], self.player_loc[1]+1).enter()
                self.player_loc = (self.player_loc[0], self.player_loc[1]+1)
                self.bottom_left = (self.bottom_left[0], self.bottom_left[1]+1)
                self.populate_board()
        # case left
        elif direction==1:
            if self.can_move(self.player_loc[0]+1, self.player_loc[1], direction):
                self.player_facing = direction
                if self.can_enter(self.player_loc[0]+1, self.player_loc[1], direction):
                    self.get(self.player_loc[0]+1, self.player_loc[1]).enter()
                self.player_loc = (self.player_loc[0]+1, self.player_loc[1])
                self.bottom_left = (self.bottom_left[0]+1, self.bottom_left[1])
                self.populate_board()
        # case down
        if direction==2:
            if self.can_move(self.player_loc[0], self.player_loc[1]-1, direction):
                self.player_facing = direction
                if self.can_enter(self.player_loc[0], self.player_loc[1]-1, direction):
                    self.get(self.player_loc[0], self.player_loc[1]-1).enter()
                self.player_loc = (self.player_loc[0], self.player_loc[1]-1)
                self.bottom_left = (self.bottom_left[0], self.bottom_left[1]-1)
                self.populate_board()
        # case right
        if direction==3:
            if self.can_move(self.player_loc[0] - 1, self.player_loc[1], direction):
                self.player_facing = direction
                if self.can_enter(self.player_loc[0]-1, self.player_loc[1], direction):
                    self.get(self.player_loc[0]-1, self.player_loc[1]).enter()
                self.player_loc = (self.player_loc[0]-1, self.player_loc[1])
                self.bottom_left = (self.bottom_left[0]-1, self.bottom_left[1])
                self.populate_board()


    def render_board(self):
        self.batch.draw()

        self.player_icon.x = self.width//2 *TILE_WIDTH
        self.player_icon.y =self.height//2 *TILE_HEIGHT
        self.player_icon.draw()

        ### for debugging, check on sprites ###
        # for j in range(self.height):
        #     for i in range(self.width):
        #         print(self.get(i, j).sprite, self.get(i, j).sprite.x, self.get(i, j).sprite.y)

    def update_state(self, dt):
        if self.player_heading > -1:
            self.move(self.player_heading)
        if self.player_sprinting:
            self.move(self.player_heading)


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


