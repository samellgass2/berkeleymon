"""Loading screen and cutscenes."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
import pyglet.gl as gl
from data.Constants import *

class TextBox():
    def __init__(self, text: str, overworld: bool=True):
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

    def render(self):
        if not self.complete and len(self.text_buffer):
            self.text_so_far += self.text_buffer.pop()
        else:
            self.complete = True

        if self.overworld:
            self.text_object = pg.text.Label(text=self.text_so_far, font_size=12, x = 0.1 * TILE_WIDTH, y = 1.8 * TILE_HEIGHT,
                                             width = 24 * TILE_WIDTH, multiline=True, color=(0,0,0,255))
        else:
            self.text_object = pg.text.Label(text=self.text_so_far, font_size=12, x = 0.1 * TILE_WIDTH, y = 5.3 * TILE_HEIGHT,
                                             width = 24 * TILE_WIDTH, multiline=True, color=(0,0,0,255))

        for batch in self.batches:
            batch.draw()
        self.text_object.draw()



