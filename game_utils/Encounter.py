"""Battle Interface, dispatched by GameBoard."""

import numpy as np

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

