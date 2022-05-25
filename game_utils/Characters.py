"""Pokemon and Trainers."""
from game_utils.Encounter import *
from data.Constants import *

##### ALL MONS #####

class Piplup(Pokemon):
    """Piplup."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        movetable = {
            1: Pound,
            4: Growl,
            8: Bubble,
            11: WaterSport,
            15: Peck,
            18: Bide,
            22: BubbleBeam,
            25: FuryAttack,
            29: Brine,
            32: Whirlpool,
            36: Mist,
            39: DrillPeck,
            43: HydroPump
        }

        super().__init__("PIPLUP", nickname=nickname,
                         defense=53, attack=51, special_defense=56, special_attack=61, speed=40, hp=53,
                         types=[10],gender=gender,level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/piplup_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/piplup_back.webp")))

##### ALL MOVES #####
class Pound(PokemonMove):
    """Pound."""
    def __init__(self):
        super().__init__(type=10, name="POUND", power=40, physical=True, accuracy=100, pp=35)

class Growl(PokemonMove):
    """Growl."""
    def __init__(self):
        super().__init__(type=0, name="GROWL", power=0, physical=False, accuracy=100, pp=40)

    # TODO: override attack for STATUS move type

class Bubble(PokemonMove):
    """Bubble."""
    def __init__(self):
        super().__init__(type=10, name="BUBBLE", power=20, physical=True, accuracy=100, pp=30)

class WaterSport(PokemonMove):
    """Water Sport."""
    def __init__(self):
        super().__init__(type=10, name="BUBBLE", power=0, physical=False, accuracy=100, pp=15)

class Peck(PokemonMove):
    """Peck."""
    def __init__(self):
        super().__init__(type=2, name="PECK", power=35, physical=True, accuracy=100, pp=35)

class Bide(PokemonMove):
    """Bide."""
    def __init__(self):
        super().__init__(type=0, name="BIDE", power=50, physical=True, accuracy=100, pp=10)

    # TODO: override behavior for counting turns and forcing move to be bide

class BubbleBeam(PokemonMove):
    """BubbleBeam."""
    def __init__(self):
        super().__init__(type=10, name="BUBBLEBEAM", power=65, physical=False, accuracy=100, pp=20)

class FuryAttack(PokemonMove):
    """Fury Attack."""
    def __init__(self):
        super().__init__(type=0, name="FURY ATTACK", power=15, physical=True, accuracy=85, pp=20)

    # TODO: make multi-hit moves random

class Brine(PokemonMove):
    """Brine."""
    def __init__(self):
        super().__init__(type=10, name="BRINE", power=65, physical=False, accuracy=100, pp=10)

class Whirlpool(PokemonMove):
    """Whirlpool."""
    def __init__(self):
        super().__init__(type=10, name="WHIRLPOOL", power=15, physical=False, accuracy=85, pp=15)

    # TODO: make lingering moves

class Mist(PokemonMove):
    """Mist."""
    def __init__(self):
        super().__init__(type=14, name="MIST", power=0, physical=False, accuracy=100, pp=30)

    # TODO: do MIST

class DrillPeck(PokemonMove):
    """Drill Peck."""
    def __init__(self):
        super().__init__(type=2, name="DRILL PECK", power=80, physical=True, accuracy=100, pp=20)

class HydroPump(PokemonMove):
    """Hydro Pump."""
    def __init__(self):
        super().__init__(type=10, name="HYDRO PUMP", power=120, physical=False, accuracy=80, pp=5)


TEST_TRAINER = PokemonTrainer(pokemon=[Piplup(level=100)],
                              items={Item(0, 0, None): 1, KeyItem(None): 1},
                              money=0)

