"""Battle Interface, dispatched by GameBoard."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics
from data.Constants import *
import math

class PokemonMove:
    def __init__(self, type: int, name: str, power: int, physical: bool, accuracy: int, priority: bool=False):
        """Initialize a pokemon move archetype."""
        self.user = None
        self.type = type
        self.name = name
        self.power = power
        self.priority = priority
        self.physical = physical
        self.accuracy = accuracy

    def use(self, opponent):
        """Dispatches the given move on opponent from user."""
        multiplier = 1
        # Do type math, multiply multiplier and physical + user stats
        return

    def set_user(self, pkmn):
        """Sets user for use to know typing and speed."""
        self.user = pkmn

    # TODO: implement as object that can be dispatched accurately in battle

class Pokemon:
    """The general, archetypal Pokemon class to create most of the skeleton for actions."""
    def __init__(self, name: str, nickname: str, types: list[int], level: int, xp: float, movetable: dict[int, PokemonMove], moveset: list[PokemonMove],
                 defense: int, attack: int, special_defense: int, special_attack: int, hp: int, speed: int, gender: int,
                 front_sprite: pg.sprite.Sprite, back_sprite: pg.sprite.Sprite):

        # To allow for generation of a mon by either total xp OR level, the other is filled in if not provided.
        if level is None:
            self.xp = xp
            self.level = self.xp_to_level()
        if xp is None:
            self.level = level
            self.xp = self.level_to_xp()
        if gender is None:
            gender = np.random.choice(range(2))

        self.movetable = movetable
        self.moveset = moveset
        if moveset is None:
            self.moveset = []
            self.get_most_recent_moves()

        self.name = name
        if nickname:
            self.display_name = nickname
        else:
            self.display_name = name

        self.types = types
        self.gender = gender


        self.base_stats = {}
        self.base_stats["defense"] = defense
        self.base_stats["attack"] = attack
        self.base_stats["special_defense"] = special_defense
        self.base_stats["special_attack"] = special_attack
        self.base_stats["max_hp"] = hp
        self.base_stats["speed"] = speed

        self.front_sprite = front_sprite
        self.back_sprite = back_sprite

        self.stats = {}
        self.calculate_stats()
        self.hp = self.stats["max_hp"]

    def get_most_recent_moves(self):
        """Retrieves the up to 4 most recent moves a Pokemon would have learned."""
        level = self.level
        while level > 0 and len(self.moveset) < 4:
            if self.movetable.get(level) is not None:
                self.moveset.append(self.movetable.get(level))
            level -= 1

    def calculate_stats(self):
        """Calculate a pokemon's functional stats at a given level."""
        self.stats["max_hp"] = math.floor(0.01 * (2 * self.base_stats["max_hp"] * self.level)) + self.level + 10

        for stat in self.base_stats:
            self.stats[stat] = math.floor(0.01 * (2 * self.base_stats[stat]) * self.level) + 5

    def attack(self, move: PokemonMove, opponent):
        return

        # TODO: Implement archetype for attacking, taking damage

    def take_damage(self, move: PokemonMove, opponent):
        return

    def level_up(self):
        self.level += 1
        self.calculate_stats()

    def new_move(self, move: PokemonMove):
        return
        # TODO: implement archetype for leveling, displaying moves, learning new moves

    ##### TODO: NOTE ONLY THE FAST EXPERIENCE FAMILY IS IMPLEMENTED #####
    def xp_to_level(self, xp: int=None):
        """Calculates the level of a pokemon with some total XP."""
        if xp is None:
            return math.floor((5 * self.xp / 4) ** (1/3))
        else:
            return math.floor((5 * xp / 4) ** (1 / 3))


    def level_to_xp(self, level: int=None):
        """Calculates the total XP a pokemon has earned to reach exactly their current level"""
        if level is None:
            return math.floor(4 * (self.level ** 3) / 5)
        else:
            return math.floor(4 * (level ** 3) / 5)

class PokemonGenerator:
    def __init__(self, pkmn_and_odds: list, min_level: int, max_level: int):
        self.encounter_table = pkmn_and_odds
        self.min_level = min_level
        self.max_level = max_level

    def encounter(self):
        """Generate a wild pokemon to pass out to Location --> tile --> Board to fight."""
        print("Debugging for now: a wild pokemon was encountered!")

        pokemon = self.choose_wild_pkmn()
        # Then, from this, choose an appropriate level based on distribution
        level = np.random.choice(np.arange(self.min_level, self.max_level+1))
        # Then, generate the pokemon's correct stats by keeping a big lookup table
        return pokemon(level = level)



    def choose_wild_pkmn(self):
        """Randomly generate a pokemon to encounter based on encounter rates."""
        roll = np.random.random() - self.encounter_table[0][1]
        i = 0
        while roll > 0:
            roll -= self.encounter_table[i+1][1]
            i += 1
        return self.encounter_table[i][0]

class Item:
    """A usable in-game item."""
    def __init__(self, kind: int, value: int, owner):
        self.kind = kind
        self.owner = owner

    def use(self, target: Pokemon):
        return

    def sell(self):
        self.owner.items.remove(self)



# TODO: implement all items in subclasses of Item
class KeyItem(Item):
    def __init__(self, owner):
        """A key item is type 0, has no value, and an owner."""
        super().__init__(0, 0, owner)

    def sell(self):
        """A key item may not be sold"""
        return

class PokeballItem(Item):
    def __init__(self, value, owner):
        super().__init__(1, value, owner)

    def use(self, target: Pokemon):
        # Do self.owner.battle.catch() --> attempt catch
        return


# TODO: implement the TRAINER class, make it agnostic for use by an AGENT or by a PLAYER
class PokemonTrainer:
    """A container to keep track of a trainer's pokemon and items."""
    def __init__(self, pokemon: list[Pokemon], items: dict[Item, int], money: int):
        self.team = pokemon
        self.items = items
        self.money = money


# TODO: implement the BATTLE class, figure out how to flag in main render loop --> do encounter UI
class Battle:
    """The renderer and logic for pokemon battles"""
    def __init__(self, trainer: PokemonTrainer, opponent, board):
        self.trainer = trainer
        self.opponent = opponent
        self.player_may_take_action = False
        self.layers = 5
        self.batches = [graphics.Batch() for i in range(self.layers)]
        self.board = board
        self.user_current_pkmn = trainer.team[0]
        self.foe_current_pkmn = opponent[0]

        self.battle_button_bottom_left = (9*TILE_WIDTH, 2*TILE_HEIGHT)
        self.battle_button_top_right = (15*TILE_WIDTH, 5*TILE_WIDTH)

        self.run_button_bottom_left = (9.5 * TILE_WIDTH, 0.5 * TILE_HEIGHT)
        self.run_button_top_right = (14.5 * TILE_WIDTH, 1.5 * TILE_WIDTH)

        self.items_button_bottom_left = (2 * TILE_WIDTH, 2 * TILE_HEIGHT)
        self.items_button_top_right = (7 * TILE_WIDTH, 4 * TILE_HEIGHT)

        self.pokemon_button_bottom_left = (17 * TILE_WIDTH, 2 * TILE_HEIGHT)
        self.pokemon_button_top_right = (22 * TILE_WIDTH, 4 * TILE_HEIGHT)

        self.curr_menu = 0

        self.shapes = []

        self.initialize()

    def intro_animation(self):
        """Should start an intro animation that is unskippable and begins the battle."""
        return

    def outro_animation(self):
        """Should execute an outro animation that is unskippable and ends the battle."""
        return

    def initialize(self):
        """Should set up all objects and important pointers as attributes of the Battle."""
        # Set up HP bars

        # Set up player action buttons

        # Set up pokemon stage

        # Set up pokemon themselves

        # animate stuff
        self.intro_animation()

        # Allow player to move
        self.player_may_take_action = True
        return

    def render(self):
        self.shapes = []
        self.batches = [graphics.Batch() for i in range(self.layers)]
        background = pg.shapes.Rectangle(0,0, width=24*TILE_WIDTH, height=16*TILE_HEIGHT, color=(255,255,255), batch=self.batches[0])
        menu = pg.shapes.Rectangle(0,0, width=24*TILE_WIDTH, height=6*TILE_HEIGHT, color=(255,255,255), batch=self.batches[2])
        menu_divider = pg.shapes.Line(x=0, y=6*TILE_HEIGHT, x2=24*TILE_WIDTH, y2=6*TILE_HEIGHT, width=4, color=(0,0,0), batch=self.batches[2])

        self.render_pkmn_plates()
        self.render_hp_bars()
        self.render_sprites()
        self.render_buttons()

        if self.curr_menu == 1:
            self.render_items_menu()

        for batch in self.batches:
            batch.draw()

    def render_pkmn_plates(self):
        # TODO: fill the plates
        plate = pg.shapes.Ellipse(x=16.5*TILE_WIDTH, y=12*TILE_HEIGHT,
                                  a=4*TILE_WIDTH, b=1.5*TILE_HEIGHT, color=(0,0,0), batch=self.batches[1])

        friendly_plate = pg.shapes.Ellipse(x=6*TILE_WIDTH, y=5*TILE_HEIGHT,
                                           a=6.5*TILE_WIDTH, b=3*TILE_HEIGHT, color=(0,0,0), batch=self.batches[1])
        self.shapes.extend([plate, friendly_plate])

    def render_hp_bars(self):
        main_bar = pg.shapes.Rectangle(x=0, y=13*TILE_HEIGHT, width=7*TILE_WIDTH, height=2*TILE_HEIGHT,
                                       batch=self.batches[1], color=(200,200,200))
        f_triangle = pg.shapes.Triangle(x=7*TILE_WIDTH, y=13*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=15*TILE_HEIGHT, x3=8*TILE_WIDTH, y3=15*TILE_HEIGHT,
                                        batch=self.batches[1], color=(200,200,200))

        health_bar1 = pg.shapes.Line(x=16.5*TILE_WIDTH, y=7.5*TILE_HEIGHT, x2=23*TILE_WIDTH, y2=7.5*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        health_bar2 = pg.shapes.Line(x=16.5*TILE_WIDTH, y=8*TILE_HEIGHT, x2=23*TILE_WIDTH, y2=8*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        health_bar3 = pg.shapes.Line(x=16.5*TILE_WIDTH, y=7.5*TILE_HEIGHT, x2=16.5*TILE_WIDTH, y2=8*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        health_bar4 = pg.shapes.Line(x=23*TILE_WIDTH, y=7.5*TILE_HEIGHT, x2=23*TILE_WIDTH, y2=8*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        pkmn_name = pg.text.Label(text=self.user_current_pkmn.display_name, font_size=10, x=16.5*TILE_WIDTH, y=8.3*TILE_HEIGHT,
                                  color=(0,0,0,255), batch=self.batches[2])

        friendly_mon_percent = self.user_current_pkmn.hp / self.user_current_pkmn.stats["max_hp"]
        healthbarfill = pg.shapes.Rectangle(x=16.5*TILE_WIDTH, y=7.5*TILE_HEIGHT, height=0.5*TILE_HEIGHT, width=6.5*TILE_WIDTH*friendly_mon_percent,
                                            color=(0, 255, 0), batch=self.batches[3])

        friendly_level = pg.text.Label(text="Lv. "+str(self.user_current_pkmn.level), font_size=10, x=21.5*TILE_WIDTH, y=8.3*TILE_HEIGHT,
                                  color=(0,0,0,255), batch=self.batches[2])

        health_counter = pg.text.Label(text=str(self.user_current_pkmn.hp) + " / "+str(self.user_current_pkmn.stats["max_hp"]), font_size=10, x=19*TILE_WIDTH, y=7.08*TILE_HEIGHT,
                                  color=(0,0,0,255), batch=self.batches[2])

        enemy_health_bar1 = pg.shapes.Line(x=0.5*TILE_WIDTH, y=13.5*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=13.5*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        enemy_health_bar2 = pg.shapes.Line(x=0.5*TILE_WIDTH, y=14*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=14*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        enemy_health_bar3 = pg.shapes.Line(x=0.5*TILE_WIDTH, y=13.5*TILE_HEIGHT, x2=0.5*TILE_WIDTH, y2=14*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        enemy_health_bar4 = pg.shapes.Line(x=7*TILE_WIDTH, y=13.5*TILE_HEIGHT, x2=7*TILE_WIDTH, y2=14*TILE_HEIGHT, width=2,
                                     color=(0,0,0), batch=self.batches[2])
        enemy_pkmn_name = pg.text.Label(text=self.foe_current_pkmn.display_name, font_size=10, x=0.5*TILE_WIDTH, y=14.3*TILE_HEIGHT,
                                  color=(0,0,0,255), batch=self.batches[2])

        enemy_mon_percent = self.foe_current_pkmn.hp / self.foe_current_pkmn.stats["max_hp"]
        enemy_healthbarfill = pg.shapes.Rectangle(x=0.5*TILE_WIDTH, y=13.5*TILE_HEIGHT, height=0.5*TILE_HEIGHT, width=6.5*TILE_WIDTH*enemy_mon_percent,
                                            color=(0, 255, 0), batch=self.batches[3])

        enemy_level = pg.text.Label(text="Lv. " + str(self.foe_current_pkmn.level), font_size=10, x=6 * TILE_WIDTH,
                                       y=14.3 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[2])



        enemy_bar = pg.shapes.Rectangle(x=16*TILE_WIDTH, y=7 * TILE_HEIGHT, width=8 * TILE_WIDTH, height=2 * TILE_HEIGHT,
                                       batch=self.batches[1], color=(200,200,200))
        enemy_triangle = pg.shapes.Triangle(x=16 * TILE_WIDTH, y=7 * TILE_HEIGHT, x2=16 * TILE_WIDTH, y2=9 * TILE_HEIGHT,
                                        x3=15 * TILE_WIDTH, y3=9 * TILE_HEIGHT,
                                        batch=self.batches[1], color=(200,200,200))

        self.shapes.extend([main_bar, f_triangle, enemy_bar, enemy_triangle,
                            health_bar1, health_bar2, health_bar3, health_bar4,
                            pkmn_name, healthbarfill, enemy_health_bar1, enemy_health_bar2,
                            enemy_health_bar3, enemy_health_bar4, enemy_pkmn_name, enemy_healthbarfill,
                            friendly_level, enemy_level, health_counter])

    def render_sprites(self):
        friendly_mon = self.user_current_pkmn.back_sprite
        friendly_mon.batch = self.batches[2]
        friendly_mon.x = 4*TILE_WIDTH
        friendly_mon.y = 6*TILE_HEIGHT

        foe_mon = self.foe_current_pkmn.front_sprite
        foe_mon.batch = self.batches[2]
        foe_mon.x = 15*TILE_WIDTH
        foe_mon.y = 11*TILE_HEIGHT

    def render_buttons(self):
        battle_button = pg.shapes.BorderedRectangle(x= self.battle_button_bottom_left[0], y=self.battle_button_bottom_left[1],
                                     width=self.battle_button_top_right[0] - self.battle_button_bottom_left[0],
                                     height=self.battle_button_top_right[1] - self.battle_button_bottom_left[1],
                                     color=(243, 103, 89), border_color=(173, 24, 10), batch = self.batches[3], border=3)

        battle_button_label = pg.text.Label(text="BATTLE", font_size=24, x= self.battle_button_bottom_left[0] + 1 * TILE_WIDTH,
                                       y= self.battle_button_bottom_left[1] + 1 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        run_button = pg.shapes.BorderedRectangle(x= self.run_button_bottom_left[0], y=self.run_button_bottom_left[1],
                                     width=self.run_button_top_right[0] - self.run_button_bottom_left[0],
                                     height=self.run_button_top_right[1] - self.run_button_bottom_left[1],
                                     color=(128, 237, 68), border_color=(64, 161, 10), batch = self.batches[3], border=3)

        run_button_label = pg.text.Label(text="RUN", font_size=18, x= self.run_button_bottom_left[0] + 1.33 * TILE_WIDTH,
                                       y= self.run_button_bottom_left[1] + 0.25 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        items_button = pg.shapes.BorderedRectangle(x= self.items_button_bottom_left[0], y=self.items_button_bottom_left[1],
                                     width=self.items_button_top_right[0] - self.items_button_bottom_left[0],
                                     height=self.items_button_top_right[1] - self.items_button_bottom_left[1],
                                     color=(50, 175, 244), border_color=(16, 80, 200), batch = self.batches[3], border=3)

        items_button_label = pg.text.Label(text="ITEMS", font_size=20, x= self.items_button_bottom_left[0] + 1 * TILE_WIDTH,
                                       y= self.items_button_bottom_left[1] + 0.5 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        pokemon_button = pg.shapes.BorderedRectangle(x= self.pokemon_button_bottom_left[0], y=self.pokemon_button_bottom_left[1],
                                     width=self.pokemon_button_top_right[0] - self.pokemon_button_bottom_left[0],
                                     height=self.pokemon_button_top_right[1] - self.pokemon_button_bottom_left[1],
                                     color=(50, 175, 244), border_color=(16, 80, 200), batch = self.batches[3], border=3)

        pokemon_button_label = pg.text.Label(text="POKEMON", font_size=20, x= self.pokemon_button_bottom_left[0] + 0.25 * TILE_WIDTH,
                                       y= self.pokemon_button_bottom_left[1] + 0.5 * TILE_HEIGHT,
                                       color=(0, 0, 0, 255), batch=self.batches[4])

        self.shapes.extend([battle_button, battle_button_label,
                            run_button, run_button_label,
                            items_button, items_button_label,
                            pokemon_button, pokemon_button_label])


    def update(self):
        """Main update loop to process player actions"""
        return

    def dispatch_mouse_click(self, x, y):
        # Case in main menu
        if self.curr_menu == 0:
            # Case clicked ITEMS
            if self.items_button_bottom_left[0] <= x <= self.items_button_top_right[0] \
                    and self.items_button_bottom_left[1] <= y <= self.items_button_top_right[1]:
                print("ITEMS CLICKED")
                self.curr_menu = 1
                self.items_action()
            # Case clicked RUN
            elif self.run_button_bottom_left[0] <= x <= self.run_button_top_right[0] \
                    and self.run_button_bottom_left[1] <= y <= self.run_button_top_right[1]:
                print("RUN CLICKED")
                self.run_action()
            # Case clicked BATTLE
            elif self.battle_button_bottom_left[0] <= x <= self.battle_button_top_right[0] \
                    and self.battle_button_bottom_left[1] <= y <= self.battle_button_top_right[1]:
                print("BATTLE CLICKED")
                self.curr_menu = 2
                self.battle_action()
            # Case clicked POKEMON
            elif self.pokemon_button_bottom_left[0] <= x <= self.pokemon_button_top_right[0] \
                    and self.pokemon_button_bottom_left[1] <= y <= self.pokemon_button_top_right[1]:
                print("POKEMON CLICKED")
                self.curr_menu = 3
                self.pokemon_action()
        # Case in items menu
        elif self.curr_menu == 1:
            return
        # Case in battle menu
        elif self.curr_menu == 2:
            return
        # Case in pokemon menu
        elif self.curr_menu == 3:
            return


    def run_action(self):
        """When run is pressed"""
        # if ... pokemon related conditions, for now just 1
        escape_prob = 0
        if np.random.random() >= escape_prob:
            # TODO: send some text to screen
            self.player_may_take_action = False
            self.outro_animation()
            self.board.exit_encounter()
            self.player_may_take_action = True

    def battle_action(self):
        """When battle is pressed, open move menu"""
        return

    def items_action(self):
        """When items is pressed, open items menu"""
        return

    def pokemon_action(self):
        """When pokemon is pressed, open pokemon menu"""
        return

    def render_items_menu(self):
        # TODO: make items menu and corresponding mouse parsing
        return

    def render_battle_menu(self):
        # TODO: make battle menu and corresponding mouse parsing
        return

    def render_pokemon_menu(self):
        # TODO: make pokemon menu and corresponding mouse parsing
        return




