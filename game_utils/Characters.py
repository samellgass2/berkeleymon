"""Pokemon and Trainers."""
from game_utils.Encounter import *
from data.Constants import *

##### ALL MONS #####
class Turtwig(Pokemon):
    """Turtwig."""
    name = "TURTWIG"
    hp = 55
    attack = 68
    special_attack = 45
    defense = 64
    special_defense = 55
    speed = 31
    tier = 'F'
    number = 1
    exp_yield = 64


    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            18: Grotle
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=[11], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/turtwig_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/turtwig_back.png")),
                         exp_yield=self.exp_yield, evolutions=evolutions)

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
                         types=[12], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
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
                         types=[12], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/luxio_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/luxio_back.png")),
                         exp_yield=117, evolutions=evolutions)

        self.tier = 'E'
        self.number = 18

class Luxray(Pokemon):
    """Luxray."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("LUXRAY", nickname=nickname,
                         hp=80, attack=120,special_attack=95, defense=79, special_defense=79, speed=70,
                         types=[12], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/luxray_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/luxray_back.png")),
                         exp_yield=194, evolutions=evolutions)

        self.tier = 'B'
        self.number = 19

class Abra(Pokemon):
    """Abra."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            16:Kadabra
        }

        super().__init__("ABRA", nickname=nickname,
                         hp=25, attack=20,special_attack=105, defense=15, special_defense=55, speed=90,
                         types=[13], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/abra_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/abra_back.png")),
                         exp_yield=75, evolutions=evolutions)

        self.tier = 'F'
        self.number = 20

class Kadabra(Pokemon):
    """Kadabra."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36:Alakazam
        }

        super().__init__("KADABRA", nickname=nickname,
                         hp=40, attack=35,special_attack=120, defense=30, special_defense=70, speed=105,
                         types=[13], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/kadabra_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/kadabra_back.png")),
                         exp_yield=145, evolutions=evolutions)

        self.tier = 'D'
        self.number = 21

class Alakazam(Pokemon):
    """Alakazam."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("ALAKAZAM", nickname=nickname,
                         hp=55, attack=50,special_attack=135, defense=45, special_defense=95, speed=120,
                         types=[13], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/alakazam_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/alakazam_back.png")),
                         exp_yield=186, evolutions=evolutions)

        self.tier = 'B'
        self.number = 22

class Magikarp(Pokemon):
    """Magikarp."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Splash
        }
        evolutions = {
            20: Gyarados
        }

        super().__init__("MAGIKARP", nickname=nickname,
                         hp=20, attack=10,special_attack=15, defense=55, special_defense=20, speed=80,
                         types=[10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/magikarp_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/magikarp_back.png")),
                         exp_yield=20, evolutions=evolutions)

        self.tier = 'F'
        self.number = 23

class Gyarados(Pokemon):
    """Gyarados."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Splash
        }
        evolutions = {
        }

        super().__init__("GYARADOS", nickname=nickname,
                         hp=95, attack=125,special_attack=60, defense=79, special_defense=100, speed=81,
                         types=[10,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/gyarados_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/gyarados_back.png")),
                         exp_yield=214, evolutions=evolutions)

        self.tier = 'A'
        self.number = 24

class Budew(Pokemon):
    """Budew."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            16: Roselia
        }

        super().__init__("BUDEW", nickname=nickname,
                         hp=40, attack=30,special_attack=50, defense=35, special_defense=70, speed=55,
                         types=[11,3], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/budew_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/budew_back.png")),
                         exp_yield=68, evolutions=evolutions)

        self.tier = 'F'
        self.number = 25

class Roselia(Pokemon):
    """Roselia."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: evolves with friendship
        evolutions = {
            32: Roserade
        }

        super().__init__("ROSELIA", nickname=nickname,
                         hp=50, attack=60,special_attack=100, defense=45, special_defense=80, speed=65,
                         types=[11,3], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/roselia_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/roselia_back.png")),
                         exp_yield=152, evolutions=evolutions)

        self.tier = 'D'
        self.number = 26

class Roserade(Pokemon):
    """Roserade."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: evolves with shiny stone
        evolutions = {
        }

        super().__init__("ROSERADE", nickname=nickname,
                         hp=60, attack=70,special_attack=125, defense=65, special_defense=105, speed=90,
                         types=[11,3], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/roserade_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/roserade_back.png")),
                         exp_yield=204, evolutions=evolutions)

        self.tier = 'B'
        self.number = 27

class Zubat(Pokemon):
    """Zubat."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            22: Golbat
        }

        super().__init__("ZUBAT", nickname=nickname,
                         hp=40, attack=45,special_attack=30, defense=35, special_defense=40, speed=55,
                         types=[3,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/zubat_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/zubat_back.png")),
                         exp_yield=54, evolutions=evolutions)

        self.tier = 'F'
        self.number = 28

class Golbat(Pokemon):
    """Golbat."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            34: Crobat
        }

        super().__init__("GOLBAT", nickname=nickname,
                         hp=75, attack=80,special_attack=65, defense=70, special_defense=75, speed=90,
                         types=[3,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/golbat_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/golbat_back.png")),
                         exp_yield=171, evolutions=evolutions)

        self.tier = 'C'
        self.number = 29

class Crobat(Pokemon):
    """Crobat."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("CROBAT", nickname=nickname,
                         hp=85, attack=90,special_attack=70, defense=80, special_defense=80, speed=130,
                         types=[3,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/crobat_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/crobat_back.png")),
                         exp_yield=204, evolutions=evolutions)

        self.tier = 'A'
        self.number = 30

class Geodude(Pokemon):
    """Geodude."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            24: Graveler
        }

        super().__init__("GEODUDE", nickname=nickname,
                         hp=40, attack=80,special_attack=30, defense=100, special_defense=30, speed=20,
                         types=[5,4], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/geodude_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/geodude_back.png")),
                         exp_yield=73, evolutions=evolutions)

        self.tier = 'F'
        self.number = 31

class Graveler(Pokemon):
    """Graveler."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36: Golem
        }

        super().__init__("GRAVELER", nickname=nickname,
                         hp=55, attack=95,special_attack=45, defense=115, special_defense=45, speed=35,
                         types=[5,4], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/graveler_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/graveler_back.png")),
                         exp_yield=134, evolutions=evolutions)

        self.tier = 'E'
        self.number = 32

class Golem(Pokemon):
    """Golem."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("GOLEM", nickname=nickname,
                         hp=80, attack=120,special_attack=55, defense=130, special_defense=65, speed=45,
                         types=[5,4], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/golem_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/golem_back.png")),
                         exp_yield=177, evolutions=evolutions)

        self.tier = 'C'
        self.number = 33

class Onix(Pokemon):
    """Onix."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: some evolution
        evolutions = {
            25: Steelix
        }

        super().__init__("ONIX", nickname=nickname,
                         hp=35, attack=45,special_attack=30, defense=160, special_defense=45, speed=70,
                         types=[5,4], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/onix_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/onix_back.png")),
                         exp_yield=108, evolutions=evolutions)

        self.tier = 'E'
        self.number = 34

class Steelix(Pokemon):
    """Steelix."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("STEELIX", nickname=nickname,
                         hp=75, attack=85,special_attack=55, defense=200, special_defense=65, speed=30,
                         types=[8,4], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/steelix_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/steelix_back.png")),
                         exp_yield=196, evolutions=evolutions)

        self.tier = 'B'
        self.number = 35

class Cranidos(Pokemon):
    """Cranidos."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Rampardos
        }

        super().__init__("CRANIDOS", nickname=nickname,
                         hp=67, attack=125,special_attack=30, defense=40, special_defense=30, speed=58,
                         types=[5], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/cranidos_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/cranidos_back.png")),
                         exp_yield=99, evolutions=evolutions)

        self.tier = 'E'
        self.number = 36

class Rampardos(Pokemon):
    """Cranidos."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("RAMPARDOS", nickname=nickname,
                         hp=97, attack=165,special_attack=65, defense=60, special_defense=50, speed=58,
                         types=[5], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/rampardos_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/rampardos_back.png")),
                         exp_yield=199, evolutions=evolutions)

        self.tier = 'C'
        self.number = 37

class Shieldon(Pokemon):
    """Cranidos."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Bastiodon
        }

        super().__init__("SHIELDON", nickname=nickname,
                         hp=30, attack=42,special_attack=42, defense=118, special_defense=88, speed=30,
                         types=[5, 8], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/shieldon_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/shieldon_back.png")),
                         exp_yield=99, evolutions=evolutions)

        self.tier = 'E'
        self.number = 38

class Bastiodon(Pokemon):
    """Bastiodon."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("BASTIODON", nickname=nickname,
                         hp=60, attack=52,special_attack=47, defense=168, special_defense=138, speed=30,
                         types=[5, 8], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/bastiodon_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/bastiodon_back.png")),
                         exp_yield=199, evolutions=evolutions)

        self.tier = 'C'
        self.number = 39

class Machop(Pokemon):
    """Machop."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            28: Machoke
        }

        super().__init__("MACHOP", nickname=nickname,
                         hp=70, attack=80,special_attack=35, defense=50, special_defense=35, speed=35,
                         types=[1], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/machop_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/machop_back.png")),
                         exp_yield=75, evolutions=evolutions)

        self.tier = 'F'
        self.number = 40

class Machoke(Pokemon):
    """Machoke."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            40: Machamp
        }

        super().__init__("MACHOKE", nickname=nickname,
                         hp=80, attack=100,special_attack=50, defense=70, special_defense=60, speed=45,
                         types=[1], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/machoke_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/machoke_back.png")),
                         exp_yield=146, evolutions=evolutions)

        self.tier = 'D'
        self.number = 41

class Machamp(Pokemon):
    """Machamp."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("MACHAMP", nickname=nickname,
                         hp=90, attack=130,special_attack=65, defense=80, special_defense=80, speed=85,
                         types=[1], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/machamp_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/machamp_back.png")),
                         exp_yield=193, evolutions=evolutions)

        self.tier = 'B'
        self.number = 42

class Psyduck(Pokemon):
    """Psyduck."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            33: Golduck
        }

        super().__init__("PSYDUCK", nickname=nickname,
                         hp=50, attack=52,special_attack=65, defense=48, special_defense=50, speed=55,
                         types=[10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/psyduck_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/psyduck_back.png")),
                         exp_yield=80, evolutions=evolutions)

        self.tier = 'F'
        self.number = 43

class Golduck(Pokemon):
    """Golduck."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("GOLDUCK", nickname=nickname,
                         hp=80, attack=82,special_attack=95, defense=78, special_defense=80, speed=85,
                         types=[10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/golduck_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/golduck_back.png")),
                         exp_yield=174, evolutions=evolutions)

        self.tier = 'B'
        self.number = 44

class Burmy(Pokemon):
    """Burmy."""
    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }

        if gender is None:
            gender = np.random.choice(range(2))

        if gender == 0:
            evolutions = {
                20: Mothim
            }
        else:
            evolutions = {
                20: Wormadam
            }

        super().__init__("BURMY", nickname=nickname,
                         hp=40, attack=29,special_attack=29, defense=45, special_defense=45, speed=36,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/burmy_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/burmy_back.png")),
                         exp_yield=61, evolutions=evolutions)

        self.tier = 'F'
        self.number = 45


class Wormadam(Pokemon):
    """Wormadam."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("WORMADAM", nickname=nickname,
                         hp=60, attack=59, special_attack=79, defense=85, special_defense=105, speed=36,
                         types=[6,11], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/wormadam_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/wormadam_back.png")),
                         exp_yield=159, evolutions=evolutions)

        self.tier = 'D'
        self.number = 46

class Mothim(Pokemon):
    """Mothim."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("MOTHIM", nickname=nickname,
                         hp=70, attack=94, special_attack=94, defense=50, special_defense=50, speed=66,
                         types=[6,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/mothim_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/mothim_back.png")),
                         exp_yield=159, evolutions=evolutions)

        self.tier = 'D'
        self.number = 47

class Wurmple(Pokemon):
    """Wurmple."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            7: np.random.choice([Silcoon, Cascoon])
        }

        super().__init__("WURMPLE", nickname=nickname,
                         hp=45, attack=45, special_attack=20, defense=35, special_defense=30, speed=20,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/wurmple_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/wurmple_back.png")),
                         exp_yield=54, evolutions=evolutions)

        self.tier = 'F'
        self.number = 48

class Silcoon(Pokemon):
    """Silcoon."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Beautifly
        }

        super().__init__("SILCOON", nickname=nickname,
                         hp=50, attack=35, special_attack=25, defense=55, special_defense=25, speed=15,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/silcoon_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/silcoon_back.png")),
                         exp_yield=72, evolutions=evolutions)

        self.tier = 'F'
        self.number = 49

class Beautifly(Pokemon):
    """Beautifly."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("BEAUTIFLY", nickname=nickname,
                         hp=60, attack=70, special_attack=100, defense=50, special_defense=50, speed=65,
                         types=[6,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/beautifly_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/beautifly_back.png")),
                         exp_yield=161, evolutions=evolutions)

        self.tier = 'D'
        self.number = 50

class Cascoon(Pokemon):
    """Cascoon."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Dustox
        }

        super().__init__("CASCOON", nickname=nickname,
                         hp=50, attack=35, special_attack=25, defense=55, special_defense=25, speed=15,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/cascoon_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/cascoon_back.png")),
                         exp_yield=72, evolutions=evolutions)

        self.tier = 'F'
        self.number = 51

class Dustox(Pokemon):
    """Dustox."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("DUSTOX", nickname=nickname,
                         hp=60, attack=50, special_attack=50, defense=70, special_defense=90, speed=65,
                         types=[6,3], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/dustox_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/dustox_back.png")),
                         exp_yield=161, evolutions=evolutions)

        self.tier = 'E'
        self.number = 52

class Combee(Pokemon):
    """Combee."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        if gender is None:
            gender = np.random.choice(range(2))

        if gender == 0:
            evolutions = {
            }
        else:
            evolutions = {
                21: Vespiquen
            }

        super().__init__("COMBEE", nickname=nickname,
                         hp=30, attack=30, special_attack=30, defense=42, special_defense=42, speed=70,
                         types=[6], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/combee_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/combee_back.png")),
                         exp_yield=63, evolutions=evolutions)

        self.tier = 'F'
        self.number = 53

class Vespiquen(Pokemon):
    """Vespiquen."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("VESPIQUEN", nickname=nickname,
                         hp=70, attack=80, special_attack=80, defense=102, special_defense=102, speed=40,
                         types=[6,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/vespiquen_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/vespiquen_back.png")),
                         exp_yield=188, evolutions=evolutions)

        self.tier = 'C'
        self.number = 54

class Pachirisu(Pokemon):
    """Pachirisu."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("PACHIRISU", nickname=nickname,
                         hp=60, attack=45, special_attack=45, defense=70, special_defense=90, speed=95,
                         types=[12], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/pachirisu_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/pachirisu_back.png")),
                         exp_yield=120, evolutions=evolutions)

        self.tier = 'D'
        self.number = 55

class Buizel(Pokemon):
    """Buizel."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            26: Floatzel
        }

        super().__init__("BUIZEL", nickname=nickname,
                         hp=55, attack=65, special_attack=60, defense=35, special_defense=30, speed=85,
                         types=[10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/buizel_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/buizel_back.png")),
                         exp_yield=75, evolutions=evolutions)

        self.tier = 'F'
        self.number = 56

class Floatzel(Pokemon):
    """Floatzel."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("FLOATZEL", nickname=nickname,
                         hp=85, attack=105, special_attack=85, defense=55, special_defense=50, speed=115,
                         types=[10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/floatzel_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/floatzel_back.png")),
                         exp_yield=178, evolutions=evolutions)

        self.tier = 'C'
        self.number = 57

class Cherubi(Pokemon):
    """Cherubi."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            25: Cherrim
        }

        super().__init__("CHERUBI", nickname=nickname,
                         hp=45, attack=35, special_attack=62, defense=45, special_defense=53, speed=35,
                         types=[11], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/cherubi_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/cherubi_back.png")),
                         exp_yield=68, evolutions=evolutions)

        self.tier = 'F'
        self.number = 58

class Cherrim(Pokemon):
    """Cherubi."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("CHERRIM", nickname=nickname,
                         hp=70, attack=60, special_attack=87, defense=70, special_defense=78, speed=85,
                         types=[11], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/cherrim_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/cherrim_back.png")),
                         exp_yield=133, evolutions=evolutions)

        self.tier = 'C'
        self.number = 59

class Shellos(Pokemon):
    """Shellos."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Gastrodon
        }

        super().__init__("SHELLOS", nickname=nickname,
                         hp=76, attack=48, special_attack=57, defense=48, special_defense=62, speed=34,
                         types=[10], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/shellos_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/shellos_back.png")),
                         exp_yield=73, evolutions=evolutions)

        self.tier = 'F'
        self.number = 60

class Gastrodon(Pokemon):
    """Gastrodon."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("GASTRODON", nickname=nickname,
                         hp=111, attack=83, special_attack=92, defense=68, special_defense=82, speed=39,
                         types=[10,4], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/gastrodon_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/gastrodon_back.png")),
                         exp_yield=176, evolutions=evolutions)

        self.tier = 'C'
        self.number = 61

class Heracross(Pokemon):
    """Heracross."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("HERACROSS", nickname=nickname,
                         hp=80, attack=125, special_attack=40, defense=75, special_defense=95, speed=85,
                         types=[6,1], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/heracross_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/heracross_back.png")),
                         exp_yield=200, evolutions=evolutions)

        self.tier = 'B'
        self.number = 62

class Aipom(Pokemon):
    """Aipom."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("AIPOM", nickname=nickname,
                         hp=55, attack=70, special_attack=40, defense=55, special_defense=55, speed=85,
                         types=[0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/aipom_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/aipom_back.png")),
                         exp_yield=94, evolutions=evolutions)

        self.tier = 'E'
        self.number = 63

class Ambipom(Pokemon):
    """Ambipom."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("AMBIPOM", nickname=nickname,
                         hp=75, attack=100, special_attack=60, defense=66, special_defense=66, speed=115,
                         types=[0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/ambipom_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/ambipom_back.png")),
                         exp_yield=186, evolutions=evolutions)

        self.tier = 'C'
        self.number = 64

class Drifloon(Pokemon):
    """Drifloon."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            28: Drifblim
        }

        super().__init__("DRIFLOON", nickname=nickname,
                         hp=90, attack=50, special_attack=60, defense=34, special_defense=44, speed=70,
                         types=[7,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/drifloon_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/drifloon_back.png")),
                         exp_yield=127, evolutions=evolutions)

        self.tier = 'E'
        self.number = 65

class Drifblim(Pokemon):
    """Drifblim."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("DRIFBLIM", nickname=nickname,
                         hp=150, attack=80, special_attack=90, defense=44, special_defense=54, speed=80,
                         types=[7,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/drifblim_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/drifblim_back.png")),
                         exp_yield=204, evolutions=evolutions)

        self.tier = 'C'
        self.number = 66

class Buneary(Pokemon):
    """Buneary."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: friendship evolve
        evolutions = {
            18: Lopunny
        }

        super().__init__("BUNEARY", nickname=nickname,
                         hp=55, attack=66, special_attack=44, defense=44, special_defense=56, speed=85,
                         types=[0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/buneary_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/buneary_back.png")),
                         exp_yield=84, evolutions=evolutions)

        self.tier = 'E'
        self.number = 67

class Lopunny(Pokemon):
    """Lopunny."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("LOPUNNY", nickname=nickname,
                         hp=65, attack=76, special_attack=54, defense=84, special_defense=96, speed=105,
                         types=[0], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/lopunny_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/lopunny_back.png")),
                         exp_yield=178, evolutions=evolutions)

        self.tier = 'C'
        self.number = 68

class Gastly(Pokemon):
    """Gastly."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            25: Haunter
        }

        super().__init__("GASTLY", nickname=nickname,
                         hp=30, attack=35, special_attack=100, defense=30, special_defense=35, speed=80,
                         types=[7,3], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/gastly_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/gastly_back.png")),
                         exp_yield=95, evolutions=evolutions)

        self.tier = 'F'
        self.number = 69

class Haunter(Pokemon):
    """Haunter."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            38: Gengar
        }

        super().__init__("HAUNTER", nickname=nickname,
                         hp=45, attack=50, special_attack=115, defense=45, special_defense=55, speed=95,
                         types=[7,3], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/haunter_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/haunter_back.png")),
                         exp_yield=126, evolutions=evolutions)

        self.tier = 'D'
        self.number = 70

class Gengar(Pokemon):
    """Gengar."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("GENGAR", nickname=nickname,
                         hp=60, attack=65, special_attack=130, defense=60, special_defense=75, speed=110,
                         types=[7,3], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/gengar_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/gengar_back.png")),
                         exp_yield=190, evolutions=evolutions)

        self.tier = 'B'
        self.number = 71

class Misdreavus(Pokemon):
    """Misdreavus."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: dusk stone
        evolutions = {
            30: Mismagius
        }

        super().__init__("MISDREAVUS", nickname=nickname,
                         hp=60, attack=60, special_attack=85, defense=60, special_defense=85, speed=85,
                         types=[7], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/misdreavus_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/misdreavus_back.png")),
                         exp_yield=147, evolutions=evolutions)

        self.tier = 'D'
        self.number = 72

class Mismagius(Pokemon):
    """Mismagius."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("MISMAGIUS", nickname=nickname,
                         hp=60, attack=60, special_attack=105, defense=60, special_defense=105, speed=105,
                         types=[7], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/mismagius_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/mismagius_back.png")),
                         exp_yield=187, evolutions=evolutions)

        self.tier = 'C'
        self.number = 73

class Murkrow(Pokemon):
    """Murkrow."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: dusk stone
        evolutions = {
            30: Honchkrow
        }

        super().__init__("MURKROW", nickname=nickname,
                         hp=60, attack=85, special_attack=85, defense=42, special_defense=42, speed=91,
                         types=[16,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/murkrow_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/murkrow_back.png")),
                         exp_yield=107, evolutions=evolutions)

        self.tier = 'D'
        self.number = 74

class Honchkrow(Pokemon):
    """Honchkrow."""

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__("HONCHCROW", nickname=nickname,
                         hp=100, attack=125, special_attack=105, defense=52, special_defense=52, speed=71,
                         types=[16,2], gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon front/honchkrow_front.png")),
                         back_sprite=pg.sprite.Sprite(pg.image.load("sprites/pokemon back/honchkrow_back.png")),
                         exp_yield=187, evolutions=evolutions)

        self.tier = 'B'
        self.number = 75


##### ALL MOVES #####
class Splash(PokemonMove):
    def __init__(self):
        super().__init__(type=10, name="Splash", power=0, physical=True, accuracy=100,pp=35, is_status=True)

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
        super().__init__(type=10, name="Water Sport", power=0, physical=False, accuracy=100, pp=15, is_status=True)

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
        super().__init__(type=14, name="Mist", power=0, physical=False, accuracy=100, pp=30, is_status=True)

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
    16: Kricketune,
    17: Shinx,
    18: Luxio,
    19: Luxray,
    20: Abra,
    21: Kadabra,
    22: Alakazam,
    23: Magikarp,
    24: Gyarados,
    25: Budew,
    26: Roselia,
    27: Roserade,
    28: Zubat,
    29: Golbat,
    30: Crobat,
    31: Geodude,
    32: Graveler,
    33: Golem,
    34: Onix,
    35: Steelix,
    36: Cranidos,
    37: Rampardos,
    38: Shieldon,
    39: Bastiodon,
    40: Machop,
    41: Machoke,
    42: Machamp,
    43: Psyduck,
    44: Golduck,
    45: Burmy,
    46: Wormadam,
    47: Mothim,
    48: Wurmple,
    49: Silcoon,
    50: Beautifly,
    51: Cascoon,
    52: Dustox,
    53: Combee,
    54: Vespiquen,
    55: Pachirisu,
    56: Buizel,
    57: Floatzel,
    58: Cherubi,
    59: Cherrim,
    60: Shellos,
    61: Gastrodon,
    62: Heracross,
    63: Aipom,
    64: Ambipom,
    65: Drifloon,
    66: Drifblim,
    67: Buneary,
    68: Lopunny,
    69: Gastly,
    70: Haunter,
    71: Gengar,
    72: Misdreavus,
    73: Mismagius,
    74: Murkrow,
    75: Honchkrow
}



TEST_TRAINER = PokemonTrainer(pokemon=[Piplup(level=100), Drifblim(level=50), Machamp(level=100), Gyarados(level=50), Crobat(level=50), Staraptor(level=50)],
                              items={Item(0, 0, None, name="Empty"): 1, KeyItem(None, name="Empty"): 1},
                              money=0)

