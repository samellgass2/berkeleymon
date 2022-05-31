"""Loading screen and cutscenes."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
import pyglet.gl as gl
from data.Constants import *

class TextBox():
    def __init__(self, text: str, overworld: bool=True, unskippable: bool=False):
        # text_buffer is a STACK of all letters, s.t. pop() will return the next char.
        self.text_buffer = [text[i] for i in range(len(text))]
        self.text_buffer.reverse()
        self.text_so_far = ""
        self.complete = False
        self.overworld = overworld
        self.board = None
        self.batches = [graphics.Batch() for i in range(3)]

        self.text_object = None
        self.box = None
        self.menu_cover = None

        ### Carrot params ###
        self.max_offset = 0.075 * TILE_HEIGHT
        self.carrot_dir = -1
        self.carrot_offset = - self.max_offset
        self.unskippable = unskippable

        self.define_box()

    def define_box(self):
        # Case overworld, box starts from bottom
        if self.overworld:
            self.box = pg.shapes.BorderedRectangle(x= 0, y= 0,
                                     width= TILE_WIDTH * 24,
                                     height= TILE_HEIGHT * 2.5,
                                     color=(255, 255, 255), border_color=(0, 0, 0), batch = self.batches[0], border=4)
        # Case in encounter, box starts from top of battle menu and
        else:
            self.box = pg.shapes.BorderedRectangle(x= 0, y= 3.5 * TILE_HEIGHT,
                                     width= TILE_WIDTH * 24,
                                     height= TILE_HEIGHT * 2.5,
                                     color=(255, 255, 255), border_color=(0, 0, 0), batch = self.batches[1], border=4)
            self.menu_cover = pg.shapes.Rectangle(0, 0, width=24 * TILE_WIDTH, height=6 * TILE_HEIGHT, color=(255, 255, 255),
                                       batch=self.batches[0])

    def update_carrot(self):
        """When text is done, update carrot prompt within a range."""
        if abs(self.carrot_offset) >= self.max_offset:
            self.carrot_dir = -1 * self.carrot_dir

        self.carrot_offset += 2 * (self.carrot_dir * self.max_offset) / REFRESH_RATE


    def render(self):
        """Rendering loop for the text box."""
        if not self.complete and len(self.text_buffer):
            self.text_so_far += self.text_buffer.pop()
        else:
            self.complete = True

        self.update_carrot()

        if self.overworld:
            self.text_object = pg.text.Label(text=self.text_so_far, font_size=12, x = 0.1 * TILE_WIDTH, y = 1.8 * TILE_HEIGHT,
                                             width = 24 * TILE_WIDTH, multiline=True, color=(0,0,0,255))
            carrot_prompt = pg.shapes.Triangle(x = 23 * TILE_WIDTH, y = 1 * TILE_HEIGHT + self.carrot_offset,
                                               x2 = 23.5 * TILE_WIDTH, y2 = 1 * TILE_HEIGHT + self.carrot_offset,
                                               x3 = 23.25 * TILE_WIDTH, y3 = 0.75 * TILE_HEIGHT + self.carrot_offset,
                                               color=(220,220,220))
        else:
            self.text_object = pg.text.Label(text=self.text_so_far, font_size=12, x = 0.1 * TILE_WIDTH, y = 5.3 * TILE_HEIGHT,
                                             width = 24 * TILE_WIDTH, multiline=True, color=(0,0,0,255))
            carrot_prompt = pg.shapes.Triangle(x=23 * TILE_WIDTH, y=4.5 * TILE_HEIGHT + self.carrot_offset,
                                               x2=23.5 * TILE_WIDTH, y2=4.5 * TILE_HEIGHT + self.carrot_offset,
                                               x3=23.25 * TILE_WIDTH, y3=4.25 * TILE_HEIGHT + self.carrot_offset,
                                               color=(220,220,220))



        for batch in self.batches:
            batch.draw()
        self.text_object.draw()
        # Carrot prompt to end text box
        if self.board.text_timer == 0 and not self.unskippable:
            carrot_prompt.draw()

        # Handle timer in container
        if self.board.text_timer > 0:
            self.board.text_timer -= 1



