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
REFRESH_RATE = 40 # denominator of FPS, 5 * max_moves per animation

curr_location = TEST_LOCATION

player_trainer = TEST_TRAINER

BOARD = GameBoard(TEST_LOCATION, TEST_LOCATION.width//2, TEST_LOCATION.height//2, player_trainer)


window = pg.window.Window(width=24*TILE_WIDTH, height=16*TILE_HEIGHT, caption="Berkeleymon")

##### HANDLERS #####
@window.event
def on_draw():
    """Main render loop for all frames."""
    window.clear()
    # dispatch loadscreen here where appropriate
    if BOARD.in_overworld:
        BOARD.render_board()
    else:
        BOARD.current_encounter.render()

@window.event
def on_key_press(symbol, modifiers):
    """Event handler for ongoing movement: process player input."""
    if BOARD.in_overworld:
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

    elif BOARD.current_encounter.player_may_take_action:
        # TODO: Legal key presses within encounter live here
        return

@window.event
def on_key_release(symbol, modifiers):
    """Event handler for ending ongooing movement: process end of player input."""
    """Event handler; process player input."""
    if BOARD.in_overworld:
        if (symbol == pg.window.key.W or symbol == pg.window.key.UP) and BOARD.player_heading == 0:
            # set to travel up
            BOARD.player_last_facing = BOARD.player_heading
            BOARD.player_heading = -1
        elif (symbol == pg.window.key.D or symbol == pg.window.key.RIGHT) and BOARD.player_heading == 1:
            BOARD.player_last_facing = BOARD.player_heading
            BOARD.player_heading = -1
        elif (symbol == pg.window.key.S or symbol == pg.window.key.DOWN) and BOARD.player_heading == 2:
            BOARD.player_last_facing = BOARD.player_heading
            BOARD.player_heading = -1
        elif (symbol == pg.window.key.A or symbol == pg.window.key.LEFT) and BOARD.player_heading == 3:
            BOARD.player_last_facing = BOARD.player_heading
            BOARD.player_heading = -1
        elif symbol == pg.window.key.SPACE:
            # set sprint modifier
            BOARD.player_sprinting = False
        BOARD.update_player_icon()

    elif BOARD.current_encounter.player_may_take_action:
        # TODO: Legal key presses within encounter live here
        return

@window.event
def on_mouse_release(x, y, button, modifiers):
    # if in_encounter OR is
    if not BOARD.in_overworld and BOARD.current_encounter.player_may_take_action:
        # Keep track of the bottom left and top right corner
        BOARD.current_encounter.dispatch_mouse_click(x, y)
    # Dispatch the correct actions within the Encounter, using the GUI loaded from encounter
    return

##### EXECUTE GAME #####

pg.clock.schedule_interval(BOARD.update_state, 1/REFRESH_RATE)
pg.app.run()