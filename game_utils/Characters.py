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
    types = [11]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")


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
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Grotle(Pokemon):
    """Grotle."""
    name = "GROTLE"
    hp = 75
    attack = 89
    special_attack = 55
    defense = 85
    special_defense = 65
    speed = 36
    tier = 'D'
    number = 2
    exp_yield = 141
    types = [11]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36: Torterra
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Torterra(Pokemon):
    """Torterra."""
    name = "TORTERRA"
    hp = 95
    attack = 109
    special_attack = 75
    defense = 105
    special_defense = 85
    speed = 56
    tier = 'B'
    number = 3
    exp_yield = 208
    types = [11,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Chimchar(Pokemon):
    """Chimchar."""
    name = "CHIMCHAR"
    hp = 44
    attack = 58
    special_attack = 58
    defense = 44
    special_defense = 44
    speed = 61
    tier = 'F'
    number = 4
    exp_yield = 65
    types = [9]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            14: Monferno
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Monferno(Pokemon):
    """Monferno."""
    name = "MONFERNO"
    hp = 64
    attack = 78
    special_attack = 78
    defense = 52
    special_defense = 52
    speed = 81
    tier = 'D'
    number = 5
    exp_yield = 142
    types = [9]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36: Infernape
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Infernape(Pokemon):
    """Infernape."""
    name = "INFERNAPE"
    hp = 76
    attack = 104
    special_attack = 104
    defense = 71
    special_defense = 71
    speed = 108
    tier = 'A'
    number = 6
    exp_yield = 209
    types = [9,1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Piplup(Pokemon):
    """Piplup."""
    name = "PIPLUP"
    hp = 53
    attack = 51
    special_attack = 61
    defense = 53
    special_defense = 56
    speed = 40
    tier = 'F'
    number = 7
    exp_yield = 66
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.webp")

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

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Prinplup(Pokemon):
    """Prinplup."""
    name = "PRINPLUP"
    hp = 64
    attack = 66
    special_attack = 81
    defense = 68
    special_defense = 76
    speed = 50
    tier = 'D'
    number = 8
    exp_yield = 143
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {36: Empoleon}

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Empoleon(Pokemon):
    """Empoleon."""
    name = "EMPOLEON"
    hp = 84
    attack = 86
    special_attack = 111
    defense = 88
    special_defense = 101
    speed = 60
    tier = 'A'
    number = 9
    exp_yield = 210
    types = [10,8]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {

        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Starly(Pokemon):
    """Starly."""
    name = "STARLY"
    hp = 40
    attack = 55
    special_attack = 30
    defense = 30
    special_defense = 30
    speed = 60
    tier = 'F'
    number = 10
    exp_yield = 56
    types = [2,0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            14: Staravia
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Staravia(Pokemon):
    """Staravia."""
    name = "STARAVIA"
    hp = 55
    attack = 75
    special_attack = 40
    defense = 50
    special_defense = 40
    speed = 80
    tier = 'E'
    number = 11
    exp_yield = 113
    types = [2,0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            34: Staraptor
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Staraptor(Pokemon):
    """Staraptor."""
    name = "STARAPTOR"
    hp = 85
    attack = 120
    special_attack = 50
    defense = 70
    special_defense = 60
    speed = 100
    tier = 'C'
    number = 12
    exp_yield = 172
    types = [2,0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Bidoof(Pokemon):
    """Bidoof."""
    name = "BIDOOF"
    hp = 59
    attack = 45
    special_attack = 35
    defense = 40
    special_defense = 40
    speed = 31
    tier = 'F'
    number = 13
    exp_yield = 58
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            15: Bibarel
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Bibarel(Pokemon):
    """Bibarel."""
    name = "BIBAREL"
    hp = 79
    attack = 85
    special_attack = 55
    defense = 60
    special_defense = 60
    speed = 71
    tier = 'D'
    number = 14
    exp_yield = 116
    types = [0,10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Kricketot(Pokemon):
    """Kricketot."""
    name = "KRICKETOT"
    hp = 37
    attack = 25
    special_attack = 25
    defense = 41
    special_defense = 41
    speed = 25
    tier = 'F'
    number = 15
    exp_yield = 54
    types = [6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Kricketune
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Kricketune(Pokemon):
    """Kricketune."""
    name = "KRICKETUNE"
    hp = 77
    attack = 85
    special_attack = 55
    defense = 51
    special_defense = 51
    speed = 65
    tier = 'E'
    number = 16
    exp_yield = 159
    types = [6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Kricketune
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Shinx(Pokemon):
    """Shinx."""
    name = "SHINX"
    hp = 45
    attack = 65
    special_attack = 40
    defense = 34
    special_defense = 34
    speed = 45
    tier = 'F'
    number = 17
    exp_yield = 60
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            15: Luxio
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Luxio(Pokemon):
    """Luxio."""
    name = "LUXIO"
    hp = 60
    attack = 85
    special_attack = 60
    defense = 49
    special_defense = 49
    speed = 60
    tier = 'E'
    number = 18
    exp_yield = 117
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: "Luxray"
        }
        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Luxray(Pokemon):
    """Luxray."""
    name = "LUXRAY"
    hp = 80
    attack = 120
    special_attack = 95
    defense = 79
    special_defense = 79
    speed = 70
    tier = 'B'
    number = 19
    exp_yield = 194
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }
        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Abra(Pokemon):
    """Abra."""
    name = "ABRA"
    hp = 25
    attack = 20
    special_attack = 105
    defense = 15
    special_defense = 55
    speed = 90
    tier = 'F'
    number = 20
    exp_yield = 75
    types = [13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            16:Kadabra
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Kadabra(Pokemon):
    """Kadabra."""
    name = "KADABRA"
    hp = 40
    attack = 35
    special_attack = 120
    defense = 30
    special_defense = 70
    speed = 105
    tier = 'D'
    number = 21
    exp_yield = 145
    types = [13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36:Alakazam
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Alakazam(Pokemon):
    """Alakazam."""
    name = "ALAKAZAM"
    hp = 55
    attack = 50
    special_attack = 135
    defense = 45
    special_defense = 95
    speed = 120
    tier = 'B'
    number = 22
    exp_yield = 186
    types = [13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Magikarp(Pokemon):
    """Magikarp."""
    name = "MAGIKARP"
    hp = 20
    attack = 10
    special_attack = 15
    defense = 55
    special_defense = 20
    speed = 80
    tier = 'F'
    number = 23
    exp_yield = 20
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Splash
        }
        evolutions = {
            20: Gyarados
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gyarados(Pokemon):
    """Gyarados."""
    name = "GYARADOS"
    hp = 95
    attack = 125
    special_attack = 60
    defense = 79
    special_defense = 100
    speed = 81
    tier = 'A'
    number = 24
    exp_yield = 214
    types = [10,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Splash
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Budew(Pokemon):
    """Budew."""
    name = "BUDEW"
    hp = 40
    attack = 30
    special_attack = 50
    defense = 35
    special_defense = 70
    speed = 55
    tier = 'F'
    number = 25
    exp_yield = 68
    types = [11,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            16: Roselia
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Roselia(Pokemon):
    """Roselia."""
    name = "ROSELIA"
    hp = 50
    attack = 60
    special_attack = 100
    defense = 45
    special_defense = 80
    speed = 65
    tier = 'D'
    number = 26
    exp_yield = 152
    types = [11,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: evolves with friendship
        evolutions = {
            32: Roserade
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Roserade(Pokemon):
    """Roserade."""
    name = "ROSERADE"
    hp = 60
    attack = 70
    special_attack = 125
    defense = 65
    special_defense = 105
    speed = 90
    tier = 'B'
    number = 27
    exp_yield = 204
    types = [11,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: evolves with shiny stone
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Zubat(Pokemon):
    """Zubat."""
    name = "ZUBAT"
    hp = 40
    attack = 45
    special_attack = 30
    defense = 35
    special_defense = 40
    speed = 55
    tier = 'F'
    number = 28
    exp_yield = 54
    types = [3,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            22: Golbat
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Golbat(Pokemon):
    """Golbat."""
    name = "GOLBAT"
    hp = 75
    attack = 80
    special_attack = 65
    defense = 70
    special_defense = 75
    speed = 90
    tier = 'C'
    number = 29
    exp_yield = 171
    types = [3,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            34: Crobat
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Crobat(Pokemon):
    """Crobat."""
    name = "CROBAT"
    hp = 85
    attack = 90
    special_attack = 70
    defense = 80
    special_defense = 80
    speed = 130
    tier = 'A'
    number = 30
    exp_yield = 204
    types = [3,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Geodude(Pokemon):
    """Geodude."""
    name = "GEODUDE"
    hp = 40
    attack = 80
    special_attack = 30
    defense = 100
    special_defense = 30
    speed = 20
    tier = 'F'
    number = 31
    exp_yield = 73
    types = [5,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            24: Graveler
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Graveler(Pokemon):
    """Graveler."""
    name = "GRAVELER"
    hp = 55
    attack = 95
    special_attack = 45
    defense = 115
    special_defense = 45
    speed = 35
    tier = 'E'
    number = 32
    exp_yield = 134
    types = [5,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            36: Golem
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Golem(Pokemon):
    """Golem."""
    name = "GOLEM"
    hp = 80
    attack = 120
    special_attack = 55
    defense = 130
    special_defense = 65
    speed = 45
    tier = 'C'
    number = 33
    exp_yield = 177
    types = [5,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Onix(Pokemon):
    """Onix."""
    name = "ONIX"
    hp = 35
    attack = 45
    special_attack = 30
    defense = 160
    special_defense = 45
    speed = 70
    tier = 'E'
    number = 34
    exp_yield = 108
    types = [5,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: some evolution
        evolutions = {
            25: Steelix
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Steelix(Pokemon):
    """Steelix."""
    name = "STEELIX"
    hp = 75
    attack = 85
    special_attack = 35
    defense = 200
    special_defense = 65
    speed = 30
    tier = 'B'
    number = 35
    exp_yield = 196
    types = [8,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Cranidos(Pokemon):
    """Cranidos."""
    name = "CRANIDOS"
    hp = 67
    attack = 125
    special_attack = 30
    defense = 40
    special_defense = 30
    speed = 58
    tier = 'E'
    number = 36
    exp_yield = 99
    types = [5]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Rampardos
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Rampardos(Pokemon):
    """Rampardos."""
    name = "RAMPARDOS"
    hp = 97
    attack = 165
    special_attack = 65
    defense = 60
    special_defense = 50
    speed = 58
    tier = 'C'
    number = 37
    exp_yield = 199
    types = [5]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Shieldon(Pokemon):
    """Shieldon."""
    name = "SHIELDON"
    hp = 30
    attack = 42
    special_attack = 42
    defense = 118
    special_defense = 88
    speed = 30
    tier = 'E'
    number = 38
    exp_yield = 99
    types = [5,8]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Bastiodon
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Bastiodon(Pokemon):
    """Bastiodon."""
    name = "BASTIODON"
    hp = 60
    attack = 52
    special_attack = 47
    defense = 168
    special_defense = 138
    speed = 30
    tier = 'C'
    number = 39
    exp_yield = 199
    types = [5,8]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Machop(Pokemon):
    """Machop."""
    name = "MACHOP"
    hp = 70
    attack = 80
    special_attack = 35
    defense = 50
    special_defense = 35
    speed = 35
    tier = 'F'
    number = 40
    exp_yield = 75
    types = [1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            28: Machoke
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Machoke(Pokemon):
    """Machoke."""
    name = "MACHOKE"
    hp = 80
    attack = 100
    special_attack = 50
    defense = 70
    special_defense = 60
    speed = 45
    tier = 'D'
    number = 41
    exp_yield = 146
    types = [1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            40: Machamp
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Machamp(Pokemon):
    """Machamp."""
    name = "MACHAMP"
    hp = 90
    attack = 130
    special_attack = 65
    defense = 80
    special_defense = 68
    speed = 85
    tier = 'B'
    number = 42
    exp_yield = 193
    types = [1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Psyduck(Pokemon):
    """Psyduck."""
    name = "PSYDUCK"
    hp = 50
    attack = 52
    special_attack = 65
    defense = 48
    special_defense = 50
    speed = 55
    tier = 'F'
    number = 43
    exp_yield = 80
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            33: Golduck
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Golduck(Pokemon):
    """Golduck."""
    name = "GOLDUCK"
    hp = 80
    attack = 82
    special_attack = 95
    defense = 78
    special_defense = 80
    speed = 85
    tier = 'B'
    number = 44
    exp_yield = 174
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Burmy(Pokemon):
    """Burmy."""
    name = "BURMY"
    hp = 40
    attack = 29
    special_attack = 29
    defense = 45
    special_defense = 45
    speed = 36
    tier = 'F'
    number = 45
    exp_yield = 61
    types = [6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

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

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Wormadam(Pokemon):
    """Wormadam."""
    name = "WORMADAM"
    hp = 60
    attack = 59
    special_attack = 79
    defense = 85
    special_defense = 105
    speed = 36
    tier = 'D'
    number = 46
    exp_yield = 159
    types = [6,11]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")


    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Mothim(Pokemon):
    """Mothim."""
    name = "MOTHIM"
    hp = 70
    attack = 94
    special_attack = 94
    defense = 50
    special_defense = 50
    speed = 66
    tier = 'D'
    number = 47
    exp_yield = 159
    types = [6,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Wurmple(Pokemon):
    """Wurmple."""
    name = "WURMPLE"
    hp = 45
    attack = 45
    special_attack = 20
    defense = 35
    special_defense = 30
    speed = 20
    tier = 'F'
    number = 48
    exp_yield = 54
    types = [6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            7: np.random.choice([Silcoon, Cascoon])
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Silcoon(Pokemon):
    """Silcoon."""
    name = "SILCOON"
    hp = 50
    attack = 35
    special_attack = 25
    defense = 55
    special_defense = 25
    speed = 15
    tier = 'F'
    number = 49
    exp_yield = 72
    types = [6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Beautifly
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Beautifly(Pokemon):
    """Beautifly."""
    name = "BEAUTIFLY"
    hp = 60
    attack = 70
    special_attack = 100
    defense = 50
    special_defense = 50
    speed = 65
    tier = 'D'
    number = 50
    exp_yield = 161
    types = [6,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Cascoon(Pokemon):
    """Cascoon."""
    name = "CASCOON"
    hp = 50
    attack = 35
    special_attack = 25
    defense = 55
    special_defense = 25
    speed = 15
    tier = 'F'
    number = 51
    exp_yield = 72
    types = [6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            10: Dustox
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Dustox(Pokemon):
    """Dustox."""
    name = "DUSTOX"
    hp = 60
    attack = 50
    special_attack = 50
    defense = 70
    special_defense = 90
    speed = 65
    tier = 'E'
    number = 52
    exp_yield = 161
    types = [6,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Combee(Pokemon):
    """Combee."""
    name = "COMBEE"
    hp = 30
    attack = 30
    special_attack = 30
    defense = 42
    special_defense = 42
    speed = 70
    tier = 'F'
    number = 53
    exp_yield = 63
    types = [6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

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

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Vespiquen(Pokemon):
    """Vespiquen."""
    name = "VESPIQUEN"
    hp = 70
    attack = 80
    special_attack = 80
    defense = 102
    special_defense = 102
    speed = 40
    tier = 'C'
    number = 54
    exp_yield = 188
    types = [6,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)


class Pachirisu(Pokemon):
    """Pachirisu."""
    name = "PACHIRISU"
    hp = 60
    attack = 45
    special_attack = 45
    defense = 70
    special_defense = 90
    speed = 95
    tier = 'D'
    number = 55
    exp_yield = 120
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Buizel(Pokemon):
    """Buizel."""
    name = "BUIZEL"
    hp = 55
    attack = 65
    special_attack = 60
    defense = 35
    special_defense = 30
    speed = 85
    tier = 'F'
    number = 56
    exp_yield = 75
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            26: Floatzel
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Floatzel(Pokemon):
    """Floatzel."""
    name = "FLOATZEL"
    hp = 85
    attack = 105
    special_attack = 85
    defense = 55
    special_defense = 50
    speed = 115
    tier = 'C'
    number = 57
    exp_yield = 178
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Cherubi(Pokemon):
    """Cherubi."""
    name = "CHERUBI"
    hp = 45
    attack = 35
    special_attack = 62
    defense = 45
    special_defense = 53
    speed = 35
    tier = 'F'
    number = 58
    exp_yield = 68
    types = [11]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            25: Cherrim
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Cherrim(Pokemon):
    """Cherrim."""
    name = "CHERRIM"
    hp = 70
    attack = 60
    special_attack = 87
    defense = 70
    special_defense = 78
    speed = 85
    tier = 'C'
    number = 59
    exp_yield = 133
    types = [11]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Shellos(Pokemon):
    """Shellos."""
    name = "SHELLOS"
    hp = 76
    attack = 48
    special_attack = 57
    defense = 48
    special_defense = 62
    speed = 34
    tier = 'F'
    number = 60
    exp_yield = 73
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Gastrodon
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gastrodon(Pokemon):
    """Gastrodon."""
    name = "GASTRODON"
    hp = 111
    attack = 83
    special_attack = 92
    defense = 68
    special_defense = 82
    speed = 39
    tier = 'C'
    number = 61
    exp_yield = 176
    types = [10,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Heracross(Pokemon):
    """Heracross."""
    name = "HERACROSS"
    hp = 80
    attack = 125
    special_attack = 40
    defense = 75
    special_defense = 95
    speed = 85
    tier = 'B'
    number = 62
    exp_yield = 200
    types = [6,1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Aipom(Pokemon):
    """Aipom."""
    name = "AIPOM"
    hp = 55
    attack = 70
    special_attack = 40
    defense = 55
    special_defense = 55
    speed = 85
    tier = 'E'
    number = 63
    exp_yield = 94
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Ambipom(Pokemon):
    """Ambipom."""
    name = "AMBIPOM"
    hp = 75
    attack = 100
    special_attack = 60
    defense = 66
    special_defense = 66
    speed = 115
    tier = 'C'
    number = 64
    exp_yield = 186
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Drifloon(Pokemon):
    """Drifloon."""
    name = "DRIFLOON"
    hp = 90
    attack = 50
    special_attack = 60
    defense = 34
    special_defense = 44
    speed = 70
    tier = 'E'
    number = 65
    exp_yield = 127
    types = [7,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            28: Drifblim
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Drifblim(Pokemon):
    """Drifblim."""
    name = "DRIFBLIM"
    hp = 150
    attack = 80
    special_attack = 90
    defense = 44
    special_defense = 54
    speed = 80
    tier = 'C'
    number = 66
    exp_yield = 204
    types = [7,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Buneary(Pokemon):
    """Buneary."""
    name = "BUNEARY"
    hp = 55
    attack = 66
    special_attack = 44
    defense = 44
    special_defense = 56
    speed = 85
    tier = 'E'
    number = 67
    exp_yield = 84
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: friendship evolve
        evolutions = {
            18: Lopunny
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Lopunny(Pokemon):
    """Lopunny."""
    name = "LOPUNNY"
    hp = 65
    attack = 76
    special_attack = 54
    defense = 84
    special_defense = 96
    speed = 105
    tier = 'C'
    number = 68
    exp_yield = 178
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gastly(Pokemon):
    """Gastly."""
    name = "GASTLY"
    hp = 30
    attack = 35
    special_attack = 100
    defense = 30
    special_defense = 35
    speed = 80
    tier = 'F'
    number = 69
    exp_yield = 95
    types = [7,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            25: Haunter
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Haunter(Pokemon):
    """Haunter."""
    name = "HAUNTER"
    hp = 45
    attack = 50
    special_attack = 115
    defense = 45
    special_defense = 55
    speed = 95
    tier = 'D'
    number = 70
    exp_yield = 126
    types = [7,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            38: Gengar
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gengar(Pokemon):
    """Gengar."""
    name = "GENGAR"
    hp = 60
    attack = 65
    special_attack = 130
    defense = 60
    special_defense = 75
    speed = 110
    tier = 'B'
    number = 71
    exp_yield = 190
    types = [7,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Misdreavus(Pokemon):
    """Misdreavus."""
    name = "MISDREAVUS"
    hp = 60
    attack = 60
    special_attack = 85
    defense = 60
    special_defense = 85
    speed = 85
    tier = 'D'
    number = 72
    exp_yield = 147
    types = [7]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: dusk stone
        evolutions = {
            30: Mismagius
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Mismagius(Pokemon):
    """Mismagius."""
    name = "MISMAGIUS"
    hp = 60
    attack = 60
    special_attack = 105
    defense = 60
    special_defense = 105
    speed = 105
    tier = 'C'
    number = 73
    exp_yield = 187
    types = [7]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Murkrow(Pokemon):
    """Murkrow."""
    name = "MURKROW"
    hp = 60
    attack = 85
    special_attack = 85
    defense = 42
    special_defense = 42
    speed = 91
    tier = 'D'
    number = 74
    exp_yield = 107
    types = [16,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: dusk stone
        evolutions = {
            30: Honchkrow
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Honchkrow(Pokemon):
    """Honchkrow."""
    name = "HONCHKROW"
    hp = 100
    attack = 125
    special_attack = 105
    defense = 52
    special_defense = 52
    speed = 71
    tier = 'B'
    number = 75
    exp_yield = 187
    types = [16,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Glameow(Pokemon):
    """Glameow."""
    name = "GLAMEOW"
    hp = 49
    attack = 55
    special_attack = 52
    defense = 42
    special_defense = 37
    speed = 85
    tier = 'F'
    number = 76
    exp_yield = 71
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            38: Purugly
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Purugly(Pokemon):
    """Purugly."""
    name = "PURUGLY"
    hp = 71
    attack = 82
    special_attack = 64
    defense = 64
    special_defense = 59
    speed = 112
    tier = 'C'
    number = 77
    exp_yield = 183
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Goldeen(Pokemon):
    """Goldeen."""
    name = "GOLDEEN"
    hp = 45
    attack = 67
    special_attack = 35
    defense = 60
    special_defense = 50
    speed = 63
    tier = 'F'
    number = 78
    exp_yield = 111
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            33: Seaking
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Seaking(Pokemon):
    """Seaking."""
    name = "SEAKING"
    hp = 80
    attack = 92
    special_attack = 65
    defense = 65
    special_defense = 80
    speed = 68
    tier = 'C'
    number = 79
    exp_yield = 170
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Barboach(Pokemon):
    """Barboach."""
    name = "BARBOACH"
    hp = 50
    attack = 48
    special_attack = 46
    defense = 43
    special_defense = 41
    speed = 60
    tier = 'F'
    number = 80
    exp_yield = 92
    types = [10,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Whiscash
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Whiscash(Pokemon):
    """Whiscash."""
    name = "WHISCASH"
    hp = 110
    attack = 78
    special_attack = 76
    defense = 73
    special_defense = 71
    speed = 60
    tier = 'C'
    number = 81
    exp_yield = 158
    types = [10,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Chingling(Pokemon):
    """Chingling."""
    name = "CHINGLING"
    hp = 45
    attack = 30
    special_attack = 65
    defense = 50
    special_defense = 50
    speed = 45
    tier = 'F'
    number = 82
    exp_yield = 74
    types = [13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: friendship at night
        evolutions = {
            31: Chimecho
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Chimecho(Pokemon):
    """Chimecho."""
    name = "CHIMECHO"
    hp = 75
    attack = 50
    special_attack = 95
    defense = 80
    special_defense = 90
    speed = 65
    tier = 'C'
    number = 83
    exp_yield = 147
    types = [13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Stunky(Pokemon):
    """Stunky."""
    name = "STUNKY"
    hp = 63
    attack = 63
    special_attack = 41
    defense = 47
    special_defense = 41
    speed = 74
    tier = 'F'
    number = 84
    exp_yield = 79
    types = [3,16]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            34: Skuntank
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Skuntank(Pokemon):
    """Skuntank."""
    name = "SKUNTANK"
    hp = 103
    attack = 93
    special_attack = 71
    defense = 67
    special_defense = 61
    speed = 84
    tier = 'C'
    number = 85
    exp_yield = 209
    types = [3,16]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Meditite(Pokemon):
    """Meditite."""
    name = "MEDITITE"
    hp = 30
    attack = 40
    special_attack = 40
    defense = 55
    special_defense = 55
    speed = 60
    tier = 'F'
    number = 86
    exp_yield = 91
    types = [1,13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            37: Medicham
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Medicham(Pokemon):
    """Medicham."""
    name = "MEDICHAM"
    hp = 60
    attack = 60
    special_attack = 60
    defense = 75
    special_defense = 75
    speed = 80
    tier = 'D'
    number = 87
    exp_yield = 153
    types = [1,13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Bronzor(Pokemon):
    """Bronzor."""
    name = "BRONZOR"
    hp = 57
    attack = 24
    special_attack = 24
    defense = 86
    special_defense = 86
    speed = 23
    tier = 'F'
    number = 88
    exp_yield = 72
    types = [8,13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            33: Bronzong
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Bronzong(Pokemon):
    """Bronzong."""
    name = "BRONZONG"
    hp = 67
    attack = 89
    special_attack = 79
    defense = 116
    special_defense = 116
    speed = 23
    tier = 'B'
    number = 89
    exp_yield = 188
    types = [8,13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Ponyta(Pokemon):
    """Ponyta."""
    name = "PONYTA"
    hp = 50
    attack = 85
    special_attack = 65
    defense = 55
    special_defense = 65
    speed = 90
    tier = 'D'
    number = 90
    exp_yield = 152
    types = [9]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            40: Rapidash
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Rapidash(Pokemon):
    """Rapidash."""
    name = "RAPIDASH"
    hp = 65
    attack = 100
    special_attack = 80
    defense = 70
    special_defense = 80
    speed = 105
    tier = 'B'
    number = 91
    exp_yield = 192
    types = [9]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Bonsly(Pokemon):
    """Bonsly."""
    name = "BONSLY"
    hp = 50
    attack = 80
    special_attack = 10
    defense = 95
    special_defense = 45
    speed = 10
    tier = 'F'
    number = 92
    exp_yield = 68
    types = [5]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: after mimic learned... look up that level
        evolutions = {
            24: Sudowoodo
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Sudowoodo(Pokemon):
    """Sudowoodo."""
    name = "SUDOWOODO"
    hp = 70
    attack = 100
    special_attack = 30
    defense = 115
    special_defense = 65
    speed = 30
    tier = 'D'
    number = 93
    exp_yield = 135
    types = [5]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

### TODO: um... where are 94 and 95? ###

class Happiny(Pokemon):
    """Happiny."""
    name = "HAPPINY"
    hp = 100
    attack = 5
    special_attack = 15
    defense = 5
    special_defense = 65
    speed = 30
    tier = 'F'
    number = 96
    exp_yield = 255
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: level w oval stone
        evolutions = {
            20: Chansey
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Chansey(Pokemon):
    """Chansey."""
    name = "CHANSEY"
    hp = 250
    attack = 5
    special_attack = 35
    defense = 5
    special_defense = 105
    speed = 50
    tier = 'C'
    number = 97
    exp_yield = 255
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: friendship
        evolutions = {
            38: Blissey
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Blissey(Pokemon):
    """Blissey."""
    name = "BLISSEY"
    hp = 255
    attack = 10
    special_attack = 75
    defense = 10
    special_defense = 135
    speed = 55
    tier = 'A'
    number = 98
    exp_yield = 255
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Cleffa(Pokemon):
    """Cleffa."""
    name = "CLEFFA"
    hp = 50
    attack = 25
    special_attack = 45
    defense = 28
    special_defense = 55
    speed = 15
    tier = 'F'
    number = 99
    exp_yield = 37
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: friendship
        evolutions = {
            18: Clefairy
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Clefairy(Pokemon):
    """Clefairy."""
    name = "CLEFAIRY"
    hp = 70
    attack = 45
    special_attack = 60
    defense = 48
    special_defense = 65
    speed = 35
    tier = 'F'
    number = 100
    exp_yield = 68
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: moon stone
        evolutions = {
            34: Clefable
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Clefable(Pokemon):
    """Clefable."""
    name = "CLEFABLE"
    hp = 95
    attack = 70
    special_attack = 95
    defense = 73
    special_defense = 90
    speed = 60
    tier = 'C'
    number = 101
    exp_yield = 129
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Chatot(Pokemon):
    """Chatot."""
    name = "CHATOT"
    hp = 76
    attack = 65
    special_attack = 92
    defense = 45
    special_defense = 42
    speed = 91
    tier = 'D'
    number = 102
    exp_yield = 107
    types = [2,0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Pichu(Pokemon):
    """Pichu."""
    name = "PICHU"
    hp = 20
    attack = 40
    special_attack = 35
    defense = 15
    special_defense = 35
    speed = 60
    tier = 'F'
    number = 103
    exp_yield = 42
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: friendship
        evolutions = {
            15: Pikachu
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Pikachu(Pokemon):
    """Pikachu."""
    name = "PIKACHU"
    hp = 35
    attack = 55
    special_attack = 50
    defense = 40
    special_defense = 50
    speed = 90
    tier = 'F'
    number = 104
    exp_yield = 82
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: thunder stone
        evolutions = {
            30: Raichu
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Raichu(Pokemon):
    """Raichu."""
    name = "RAICHU"
    hp = 60
    attack = 90
    special_attack = 90
    defense = 55
    special_defense = 80
    speed = 110
    tier = 'C'
    number = 105
    exp_yield = 122
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Hoothoot(Pokemon):
    """Hoothoot."""
    name = "HOOTHOOT"
    hp = 60
    attack = 30
    special_attack = 36
    defense = 30
    special_defense = 56
    speed = 50
    tier = 'F'
    number = 106
    exp_yield = 58
    types = [2,0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            20: Noctowl
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Noctowl(Pokemon):
    """Noctowl."""
    name = "NOCTOWL"
    hp = 100
    attack = 50
    special_attack = 86
    defense = 50
    special_defense = 96
    speed = 70
    tier = 'C'
    number = 107
    exp_yield = 162
    types = [2,0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Spiritomb(Pokemon):
    """Spiritomb."""
    name = "SPIRITOMB"
    hp = 50
    attack = 92
    special_attack = 92
    defense = 108
    special_defense = 108
    speed = 35
    tier = 'C'
    number = 108
    exp_yield = 168
    types = [7,16]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gible(Pokemon):
    """Gible."""
    name = "GIBLE"
    hp = 58
    attack = 70
    special_attack = 40
    defense = 45
    special_defense = 45
    speed = 42
    tier = 'F'
    number = 109
    exp_yield = 67
    types = [15,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            24: Gabite
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gabite(Pokemon):
    """Gabite."""
    name = "GABITE"
    hp = 68
    attack = 90
    special_attack = 50
    defense = 65
    special_defense = 55
    speed = 82
    tier = 'D'
    number = 110
    exp_yield = 144
    types = [15,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            48: Garchomp
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Garchomp(Pokemon):
    """Garchomp."""
    name = "GARCHOMP"
    hp = 108
    attack = 130
    special_attack = 80
    defense = 95
    special_defense = 85
    speed = 102
    tier = 'S'
    number = 111
    exp_yield = 218
    types = [15,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Munchlax(Pokemon):
    """Munchlax."""
    name = "MUNCHLAX"
    hp = 135
    attack = 85
    special_attack = 40
    defense = 40
    special_defense = 85
    speed = 5
    tier = 'E'
    number = 112
    exp_yield = 94
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: friendship
        evolutions = {
            26: Snorlax
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Snorlax(Pokemon):
    """Snorlax."""
    name = "SNORLAX"
    hp = 160
    attack = 110
    special_attack = 65
    defense = 65
    special_defense = 110
    speed = 30
    tier = 'A'
    number = 113
    exp_yield = 154
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

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
    75: Honchkrow,
    76: Glameow,
    77: Purugly,
    78: Goldeen,
    79: Seaking,
    80: Barboach,
    81: Whiscash,
    82: Chingling,
    83: Chimecho,
    84: Stunky,
    85: Skuntank,
    86: Meditite,
    87: Medicham,
    88: Bronzor,
    89: Bronzong,
    90: Ponyta,
    91: Rapidash,
    92: Bonsly,
    93: Sudowoodo,

    96: Happiny,
    97: Chansey,
    98: Blissey,
    99: Cleffa,
    100: Clefairy,
    101: Clefable,
    102: Chatot,
    103: Pichu,
    104: Pikachu,
    105: Raichu,
    106: Hoothoot,
    107: Noctowl,
    108: Spiritomb,
    109: Gible,
    110: Gabite,
    111: Garchomp,
    112: Munchlax,
    113: Snorlax
}



TEST_TRAINER = PokemonTrainer(pokemon=[Garchomp(level=99), Snorlax(level=50), Machamp(level=100), Gyarados(level=50), Crobat(level=50), Staraptor(level=50)],
                              items={Item(0, 0, None, name="Empty"): 1, KeyItem(None, name="Empty"): 1},
                              money=0)

