"""Executable: The Game."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
import pyglet.gl as gl
from game_utils.GameBoard import *
from game_utils.Cutscene import *
from game_utils.Encounter import *
from game_utils.Characters import *

##### INITIALIZATION #####
REFRESH_RATE = 5 # denominator of FPS

is_loadscreen = False #True OVERRIDDEN FOR TESTING

curr_location = TEST_LOCATION

BOARD = GameBoard(TEST_LOCATION, TEST_LOCATION.width//2, TEST_LOCATION.height//2)


window = pg.window.Window(width=24*TILE_WIDTH, height=16*TILE_HEIGHT, caption="Berkeleymon")

##### HANDLERS #####
@window.event
def on_draw():
    if is_loadscreen:
        return
        # dispatch loadscreen
    """Main render loop for all frames."""
    if not BOARD.in_encounter:
        BOARD.render_board()
        # etc.
    # else:
        # ENCOUNTER.render()
        # etc.
    return

@window.event
def on_key_press(symbol, modifiers):
    """Event handler for ongoing movement: process player input."""
    # if not in_encounter
    if symbol == pg.window.key.W or symbol == pg.window.key.UP:
        # set to travel up
        BOARD.player_heading = 0

    elif symbol == pg.window.key.D or symbol == pg.window.key.RIGHT:
        # set to travel right
        BOARD.player_heading = 1

    elif symbol == pg.window.key.S or symbol == pg.window.key.DOWN:
        # set to travel down
        BOARD.player_heading = 2

    elif symbol == pg.window.key.A or symbol == pg.window.key.LEFT:
        # set to travel left
        BOARD.player_heading = 3

    elif symbol == pg.window.key.SPACE:
        # set sprint modifier
        BOARD.player_sprinting = True

    BOARD.update_player_icon()

    # if in_encounter:

@window.event
def on_key_release(symbol, modifiers):
    """Event handler for ending ongooing movement: process end of player input."""
    """Event handler; process player input."""
    # if not in_encounter
    if (symbol == pg.window.key.W or symbol == pg.window.key.UP) and BOARD.player_heading == 0:
        # set to travel up
        #BOARD.move(BOARD.player_heading)
        BOARD.player_heading = -1
    elif (symbol == pg.window.key.D or symbol == pg.window.key.RIGHT) and BOARD.player_heading == 1:
        #BOARD.move(BOARD.player_heading)
        BOARD.player_heading = -1
    elif (symbol == pg.window.key.S or symbol == pg.window.key.DOWN) and BOARD.player_heading == 2:
        #BOARD.move(BOARD.player_heading)
        BOARD.player_heading = -1
    elif (symbol == pg.window.key.A or symbol == pg.window.key.LEFT) and BOARD.player_heading == 3:
        #BOARD.move(BOARD.player_heading)
        BOARD.player_heading = -1
    elif symbol == pg.window.key.SPACE:
        # set sprint modifier
        BOARD.player_sprinting = False
    BOARD.update_player_icon()


def on_mouse_release(x, y, button, modifiers):
    # if in_encounter OR is
    # Dispatch the correct actions within the Encounter, using the GUI loaded from encounter
    return

##### EXECUTE GAME #####

pg.clock.schedule_interval(BOARD.update_state, 1/REFRESH_RATE)
pg.app.run()