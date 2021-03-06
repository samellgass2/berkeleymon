"""Executable: The Game."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
import pyglet.gl as gl
from game_utils.GameBoard import *
from game_utils.Cutscene import *
from game_utils.Encounter import *
from game_utils.Characters import *
from agents.Pokemon_Agents import *

##### INITIALIZATION #####

curr_location = TEST_LOCATION

player_trainer = TEST_TRAINER

BOARD = GameBoard(TEST_LOCATION, TEST_LOCATION.width//2, TEST_LOCATION.height//2, player_trainer)

# For now, only implemented agent is 'easy' random agent
# BOARD.set_agents(RandomLegalAgent(BOARD))
# Testing 'hard' rollout / particle filtering agent
BOARD.set_agents(NStepRolloutDamageAgent(n=5, x=3, board=BOARD))
TEST_TRAINER.set_board(BOARD)

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

    if BOARD.displaying_text:
        BOARD.current_text.render()

@window.event
def on_key_press(symbol, modifiers):
    """Event handler for ongoing movement: process player input."""
    # Case text box is being displayed
    if BOARD.displaying_text:
        return

    # Case in overworld, no menus
    elif BOARD.in_overworld:
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

    # Case in battle
    elif BOARD.current_encounter.player_may_take_action:
        # TODO: Legal key presses within encounter live here
        # TODO: key press implementation within encounter
        return

@window.event
def on_key_release(symbol, modifiers):
    """Event handler for ending ongooing movement: process end of player input."""
    # Case text may be dismissed
    # TODO: make system s.t. while turn is in play, text may not be skipped
    if BOARD.displaying_text and not BOARD.current_text.interactive:
        if BOARD.text_timer <= 0:
            if symbol == pg.window.key.SPACE or symbol == pg.window.key.A \
                    or symbol == pg.window.key.S or symbol == pg.window.key.W or symbol == pg.window.key.D:
                BOARD.end_text()
    # Case text requires interaction
    elif BOARD.displaying_text and BOARD.current_text.interactive and BOARD.current_text.complete:
        # Move cursor up
        if (symbol == pg.window.key.W or symbol == pg.window.key.UP):
            BOARD.current_text.increment_cursor()
        # Move cursor down
        elif (symbol == pg.window.key.S or symbol == pg.window.key.DOWN):
            BOARD.current_text.decrement_cursor()
        # Finalize choice
        elif (symbol == pg.window.key.SPACE or symbol == pg.window.key.ENTER):
            BOARD.current_text.choose_option()
            BOARD.end_text()
    elif BOARD.in_overworld:
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
        # TODO: key press implementation within encounter

        return

@window.event
def on_mouse_release(x, y, button, modifiers):
    # Case text may be dismissed
    # TODO: make system s.t. while turn is in play, text may not be skipped
    if BOARD.displaying_text and not BOARD.current_text.interactive:
        if BOARD.text_timer <= 0:
            BOARD.end_text()
    elif not BOARD.in_overworld and BOARD.current_encounter.player_may_take_action:
        # Keep track of the bottom left and top right corner
        BOARD.current_encounter.dispatch_mouse_click(x, y)
    # Dispatch the correct actions within the Encounter, using the GUI loaded from encounter
    return

##### EXECUTE GAME #####
#BOARD.display_text(DialogueBox(" On a scale of 1 to 10 how attractive is it to literally code pokemon all day?", options=["a long one to start us off just to see what breaks", "0", "-10", "bro r u ok", "refuse to answer because that's a terrible question you fucking frog"]))

pg.clock.schedule_interval(BOARD.update_state, 1/REFRESH_RATE)
pg.app.run()