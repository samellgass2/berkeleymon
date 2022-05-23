"""Battle Interface, dispatched by GameBoard."""

import numpy as np
import pyglet as pg
import pyglet.graphics as graphics

class PokemonMove:
    def __init__(self, type: int, name: str, power: int, priority: bool=False):
        """Initialize a pokemon move archetype."""
        self.user = None
        self.type = type
        self.name = name
        self.power = power
        self.priority = priority

    def use(self, opponent):
        """Dispatches the given move on opponent from user."""
        multiplier = 1
        # Do type math, multiply multiplier
        return

    def set_user(self, pkmn):
        """Sets user for use to know typing and speed."""
        self.user = pkmn

    # TODO: implement as object that can be dispatched accurately in battle

class Pokemon:
    """The general, archetypal Pokemon class to create most of the skeleton for actions."""
    def __init__(self, name: str, nickname: str, types: list[int], level: int, xp: float, movetable: list[PokemonMove], moveset: list[PokemonMove],
                 defense: int, attack: int, special_defense: int, special_attack: int, hp: int, speed: int, gender: int):
        self.name = name
        if nickname:
            self.display_name = nickname
        else:
            self.display_name = name

        self.types = types
        self.level = level
        self.xp = xp
        self.gender = gender

        self.learnable_moves = movetable
        self.moveset = moveset

        self.stats = {}
        self.stats["defense"] = defense
        self.stats["attack"] = attack
        self.stats["special_defense"] = special_defense
        self.stats["special_attack"] = special_attack
        self.stats["max_hp"] = hp
        self.stats["speed"] = speed
        self.hp = hp

        # TODO: Implement archetype for attacking, taking damage

        # TODO: implement archetype for leveling, displaying moves, learning new moves

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
        return pokemon



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
    def __init__(self, trainer: PokemonTrainer, opponent):
        self.trainer = trainer
        self.opponent = opponent
        self.player_may_take_action = False
        self.batch = graphics.Batch()

    def intro_animation(self):
        """Should start an intro animation that is unskippable and begins the battle."""
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
        self.batch.draw()

    def update(self):
        """Main update loop to process player actions"""
        return
