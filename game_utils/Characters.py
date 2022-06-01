"""Pokemon and Trainers."""
from game_utils.Encounter import *
from data.Constants import *

##### ALL MONS #####
class Turtwig(Pokemon):
    """Turtwig."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            18: Grotle
        }

        super().__init__("TURTWIG", nickname=nickname,
                         hp=55, attack=68,special_attack=45, defense=64, special_defense=55, speed=31,
                         types=[11], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/turtwig_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/turtwig_back.png")),
                         exp_yield=64, evolutions=evolutions)

        self.tier = 'F'
        self.number = 1

class Grotle(Pokemon):
    """Grotle."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36: Torterra
        }

        super().__init__("GROTLE", nickname=nickname,
                         hp=75, attack=89,special_attack=55, defense=85, special_defense=65, speed=36,
                         types=[11], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/grotle_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/grotle_back.png")),
                         exp_yield=141, evolutions=evolutions)

        self.tier = 'D'
        self.number = 2

class Torterra(Pokemon):
    """Torterra."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("TORTERRA", nickname=nickname,
                         hp=95, attack=109,special_attack=75, defense=105, special_defense=85, speed=56,
                         types=[4, 11], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/torterra_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/torterra_back.png")),
                         exp_yield=208, evolutions=evolutions)

        self.tier = 'B'
        self.number = 3

class Chimchar(Pokemon):
    """Chimchar."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            14: Monferno
        }

        super().__init__("CHIMCHAR", nickname=nickname,
                         hp=44, attack=58,special_attack=58, defense=44, special_defense=44, speed=61,
                         types=[9], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/chimchar_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/chimchar_back.png")),
                         exp_yield=65, evolutions=evolutions)

        self.tier = 'F'
        self.number = 4

class Monferno(Pokemon):
    """Monferno."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36: Infernape
        }

        super().__init__("MONFERNO", nickname=nickname,
                         hp=64, attack=78,special_attack=78, defense=52, special_defense=52, speed=81,
                         types=[9], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/monferno_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/monferno_back.png")),
                         exp_yield=142, evolutions=evolutions)

        self.tier = 'D'
        self.number = 5

class Infernape(Pokemon):
    """Infernape."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("INFERNAPE", nickname=nickname,
                         hp=76, attack=104,special_attack=104, defense=71, special_defense=71, speed=108,
                         types=[9], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/infernape_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/infernape_back.png")),
                         exp_yield=142, evolutions=evolutions)

        self.tier = 'D'
        self.number = 5

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

        evolutions = {16: Prinplup}

        super().__init__("PIPLUP", nickname=nickname,
                         defense=53, attack=51, special_defense=56, special_attack=61, speed=40, hp=53,
                         types=[10],gender=gender,level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/piplup_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/piplup_back.webp")),
                         exp_yield=66, evolutions=evolutions)

        self.tier = 'F'
        self.number = 7

class Prinplup(Pokemon):
    """Prinplup."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {36: Empoleon}

        super().__init__("PRINPLUP", nickname=nickname,
                         hp=64, attack=66, defense=68,special_attack=81, special_defense=76, speed=50,
                         types=[10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/prinplup_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/prinplup_back.png")),
                         exp_yield=143, evolutions=evolutions)

        self.tier = 'D'
        self.number = 8

class Empoleon(Pokemon):
    """Empoleon."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {

        }

        super().__init__("EMPOLEON", nickname=nickname,
                         hp=84, attack=86,special_attack=111, defense=88, special_defense=101, speed=60,
                         types=[10, 8], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/empoleon_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/empoleon_back.png")),
                         exp_yield=210, evolutions=evolutions)

        self.tier = 'A'
        self.number = 9

class Starly(Pokemon):
    """Starly."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            14: Staravia
        }

        super().__init__("STARLY", nickname=nickname,
                         hp=40, attack=55,special_attack=30, defense=30, special_defense=30, speed=60,
                         types=[2,0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/starly_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/starly_back.png")),
                         exp_yield=56, evolutions=evolutions)

        self.tier = 'F'
        self.number = 10

class Staravia(Pokemon):
    """Staravia."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            34: Staraptor
        }

        super().__init__("STARAVIA", nickname=nickname,
                         hp=55, attack=75,special_attack=40, defense=50, special_defense=40, speed=80,
                         types=[2,0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/staravia_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/staravia_back.png")),
                         exp_yield=113, evolutions=evolutions)

        self.tier = 'E'
        self.number = 11

class Staraptor(Pokemon):
    """Staraptor."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("STARAPTOR", nickname=nickname,
                         hp=55, attack=75,special_attack=40, defense=50, special_defense=40, speed=80,
                         types=[2,0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/staraptor_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/staraptor_back.png")),
                         exp_yield=172, evolutions=evolutions)

        self.tier = 'C'
        self.number = 12

class Bidoof(Pokemon):
    """Bidoof."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            15: Bibarel
        }

        super().__init__("BIDOOF", nickname=nickname,
                         hp=59, attack=45,special_attack=35, defense=40, special_defense=40, speed=31,
                         types=[0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/bidoof_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/bidoof_back.png")),
                         exp_yield=58, evolutions=evolutions)

        self.tier = 'F'
        self.number = 13

class Bibarel(Pokemon):
    """Bibarel."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("BIBAREL", nickname=nickname,
                         hp=79, attack=85,special_attack=55, defense=60, special_defense=60, speed=71,
                         types=[0,10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/bibarel_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/bibarel_back.png")),
                         exp_yield=116, evolutions=evolutions)

        self.tier = 'D'
        self.number = 14

class Kricketot(Pokemon):
    """Kricketot."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Kricketune
        }

        super().__init__("KRICKETOT", nickname=nickname,
                         hp=37, attack=25,special_attack=25, defense=41, special_defense=41, speed=25,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/kricketot_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/kricketot_back.png")),
                         exp_yield=54, evolutions=evolutions)

        self.tier = 'F'
        self.number = 15

class Kricketune(Pokemon):
    """Kricketune."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Kricketune
        }

        super().__init__("KRICKETUNE", nickname=nickname,
                         hp=77, attack=85,special_attack=55, defense=51, special_defense=51, speed=65,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/kricketune_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/kricketune_back.png")),
                         exp_yield=159, evolutions=evolutions)

        self.tier = 'F'
        self.number = 16

class Shinx(Pokemon):
    """Shinx."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            15: Luxio
        }

        super().__init__("SHINX", nickname=nickname,
                         hp=45, attack=65,special_attack=40, defense=34, special_defense=34, speed=45,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/shinx_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/shinx_back.png")),
                         exp_yield=60, evolutions=evolutions)

        self.tier = 'F'
        self.number = 17

class Luxio(Pokemon):
    """Luxio."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: "Luxray"
        }

        super().__init__("LUXIO", nickname=nickname,
                         hp=60, attack=85,special_attack=60, defense=49, special_defense=49, speed=60,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/luxio_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/luxio_back.png")),
                         exp_yield=159, evolutions=evolutions)

        self.tier = 'E'
        self.number = 18

##### ALL MOVES #####
class Pound(PokemonMove):
    """Pound."""
    def __init__(self):
        super().__init__(type=0, name="Pound", power=40, physical=True, accuracy=100, pp=35)

class Growl(PokemonMove):
    """Growl."""
    def __init__(self):
        super().__init__(type=0, name="Growl", power=0, physical=False, accuracy=100, pp=40, is_status=True)

    def use(self, opponent):
        return False, 0, True, 0

    # TODO: override attack for STATUS move type

class Bubble(PokemonMove):
    """Bubble."""
    def __init__(self):
        super().__init__(type=10, name="Bubble", power=20, physical=True, accuracy=100, pp=30)

class WaterSport(PokemonMove):
    """Water Sport."""
    def __init__(self):
        super().__init__(type=10, name="Water Sport", power=0, physical=False, accuracy=100, pp=15)

class Peck(PokemonMove):
    """Peck."""
    def __init__(self):
        super().__init__(type=2, name="Peck", power=35, physical=True, accuracy=100, pp=35)

class Bide(PokemonMove):
    """Bide."""
    def __init__(self):
        super().__init__(type=0, name="Bide", power=50, physical=True, accuracy=100, pp=10)

    # TODO: override behavior for counting turns and forcing move to be bide

class BubbleBeam(PokemonMove):
    """BubbleBeam."""
    def __init__(self):
        super().__init__(type=10, name="Bubblebeam", power=65, physical=False, accuracy=100, pp=20)

class FuryAttack(PokemonMove):
    """Fury Attack."""
    def __init__(self):
        super().__init__(type=0, name="Fury Attack", power=15, physical=True, accuracy=85, pp=20)

    # TODO: make multi-hit moves random

class Brine(PokemonMove):
    """Brine."""
    def __init__(self):
        super().__init__(type=10, name="Brine", power=65, physical=False, accuracy=100, pp=10)

class Whirlpool(PokemonMove):
    """Whirlpool."""
    def __init__(self):
        super().__init__(type=10, name="Whirlpool", power=15, physical=False, accuracy=85, pp=15)

    # TODO: make lingering moves

class Mist(PokemonMove):
    """Mist."""
    def __init__(self):
        super().__init__(type=14, name="Mist", power=0, physical=False, accuracy=100, pp=30)

    # TODO: do MIST

class DrillPeck(PokemonMove):
    """Drill Peck."""
    def __init__(self):
        super().__init__(type=2, name="Drill Peck", power=80, physical=True, accuracy=100, pp=20)

class HydroPump(PokemonMove):
    """Hydro Pump."""
    def __init__(self):
        super().__init__(type=10, name="Hydro Pump", power=120, physical=False, accuracy=80, pp=5)

POKEDEX_MAP = {
    1: Turtwig,
    2: Grotle,
    3: Torterra,
    4: Chimchar,
    5: Monferno,
    6: Infernape,
    7: Piplup,
    8: Prinplup,
    9: Empoleon,
    10: Starly,
    11: Staravia,
    12: Staraptor,
    13: Bidoof,
    14: Bibarel,
    15: Kricketot,
    16: Kricketune
}



TEST_TRAINER = PokemonTrainer(pokemon=[Empoleon(level=40), Infernape(level=50), Torterra(level=60), Staraptor(level=10), Piplup(level=100), Monferno(level=1)],
                              items={Item(0, 0, None, name="Empty"): 1, KeyItem(None, name="Empty"): 1},
                              money=0)

