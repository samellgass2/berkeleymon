"""Pokemon and Trainers."""
from game_utils.Actions import *
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
        movetable = {
            1: Tackle,
            5: Withdraw,
            9: Absorb,
            13: RazorLeaf,
            17: Curse,
            21: Bite,
            25: MegaDrain,
            29: LeechSeed,
            37: Crunch,
            41: GigaDrain,
            45: LeafStorm
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
        movetable = {
            0: Tackle,
            5: Withdraw,
            9: Absorb,
            13: RazorLeaf,
            17: Curse,
            22: Bite,
            27: MegaDrain,
            32: LeechSeed,
            37: Synthesis,
            42: Crunch,
            47: GigaDrain,
            52: LeafStorm
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
        movetable = {
            0: Tackle,
            5: Withdraw,
            9: Absorb,
            13: RazorLeaf,
            17: Curse,
            22: Bite,
            27: MegaDrain,
            32: Earthquake,
            33: LeechSeed,
            39: Synthesis,
            45: Crunch,
            51: GigaDrain,
            57: LeafStorm
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
        movetable = {
            0: Scratch,
            1: Leer,
            7: Ember,
            9: Taunt,
            15: FurySwipes,
            17: FlameWheel,
            23: NastyPlot,
            25: Torment,
            31: Facade,
            33: FireSpin,
            39: SlackOff,
            41: FlameThrower
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
        movetable = {
            0: Scratch,
            1: Leer,
            7: Ember,
            9: Taunt,
            11: MachPunch,
            16: FurySwipes,
            19: FlameWheel,
            26: Feint,
            29: Torment,
            36: CloseCombat,
            39: FireSpin,
            46: SlackOff,
            49: FlareBlitz
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
        movetable = {
            0: Scratch,
            1: Leer,
            7: Ember,
            9: Taunt,
            14: MachPunch,
            17: FurySwipes,
            21: FlameWheel,
            29: Feint,
            33: Punishment,
            41: CloseCombat,
            45: FireSpin,
            53: CalmMind,
            57: FlareBlitz
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
        movetable = {
            1: Tackle,
            4: Growl,
            8: Bubble,
            11: WaterSport,
            15: Peck,
            16: MetalClaw,
            19: Bide,
            24: BubbleBeam,
            28: FuryAttack,
            33: Brine,
            37: Whirlpool,
            42: Mist,
            46: DrillPeck,
            51: HydroPump
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
        movetable = {
            1: Tackle,
            4: Growl,
            8: Bubble,
            11: SwordsDance,
            15: Peck,
            16: MetalClaw,
            19: Swagger,
            24: BubbleBeam,
            28: FuryAttack,
            33: Brine,
            36: AquaJet,
            39: Whirlpool,
            46: Mist,
            52: DrillPeck,
            59: HydroPump
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
        movetable = {
            0: Tackle,
            1: Growl,
            5: QuickAttack,
            9: WingAttack,
            13: DoubleTeam,
            17: Endeavor,
            21: Whirlwind,
            25: AerialAce,
            29: TakeDown,
            33: Agility,
            37: BraveBird
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
        movetable = {
            0: Tackle,
            1: Growl,
            5: QuickAttack,
            9: WingAttack,
            13: DoubleTeam,
            18: Endeavor,
            23: Whirlwind,
            28: AerialAce,
            33: TakeDown,
            38: Agility,
            43: BraveBird
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
        movetable = {
            0: Tackle,
            1: Growl,
            5: QuickAttack,
            9: WingAttack,
            13: DoubleTeam,
            18: Endeavor,
            23: Whirlwind,
            28: AerialAce,
            33: TakeDown,
            34: CloseCombat,
            41: Agility,
            49: BraveBird
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
        movetable = {
            1: Tackle,
            5: Growl,
            9: DefenseCurl,
            13: Rollout,
            17: Headbutt,
            21: HyperFang,
            25: Yawn,
            29: Amnesia,
            33: TakeDown,
            37: SuperFang,
            41: Superpower

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
        movetable = {
            1: Tackle,
            5: Growl,
            9: DefenseCurl,
            13: Rollout,
            15: WaterGun,
            18: Headbutt,
            23: HyperFang,
            28: Yawn,
            33: Amnesia,
            38: TakeDown,
            43: SuperFang,
            48: Superpower
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
        movetable = {
            0: Growl,
            1: Bide,
            16: BugBite
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
        movetable = {
            0: Growl,
            1: Bide,
            10: FuryCutter,
            14: LeechLife,
            18: Sing,
            22: FocusEnergy,
            26: XScissor,
            30: Screech,
            34: BugBuzz,
            38: PerishSong
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


class Unown(Pokemon):
    """Unown."""
    ### TODO: IMPLEMENT ALL BUT A ###
    name = "UNOWN"
    hp = 48
    attack = 72
    special_attack = 72
    defense = 48
    special_defense = 48
    speed = 48
    tier = 'E'
    number = 114
    exp_yield = 61
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

class Riolu(Pokemon):
    """Riolu."""
    name = "RIOLU"
    hp = 40
    attack = 70
    special_attack = 35
    defense = 40
    special_defense = 40
    speed = 60
    tier = 'F'
    number = 115
    exp_yield = 72
    types = [1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: high friendship in day
        evolutions = {
            26: Lucario
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Lucario(Pokemon):
    """Lucario."""
    name = "LUCARIO"
    hp = 70
    attack = 110
    special_attack = 115
    defense = 70
    special_defense = 70
    speed = 90
    tier = 'B'
    number = 116
    exp_yield = 204
    types = [1,8]
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

class Wooper(Pokemon):
    """Wooper."""
    name = "WOOPER"
    hp = 55
    attack = 45
    special_attack = 25
    defense = 45
    special_defense = 25
    speed = 15
    tier = 'B'
    number = 117
    exp_yield = 52
    types = [10,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            20: Quagsire
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Quagsire(Pokemon):
    """Quagsire."""
    name = "QUAGSIRE"
    hp = 95
    attack = 85
    special_attack = 65
    defense = 85
    special_defense = 65
    speed = 35
    tier = 'D'
    number = 118
    exp_yield = 137
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

class Wingull(Pokemon):
    """Wingull."""
    name = "WINGULL"
    hp = 40
    attack = 30
    special_attack = 55
    defense = 30
    special_defense = 30
    speed = 85
    tier = 'F'
    number = 119
    exp_yield = 64
    types = [2,10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            25: Pelipper
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Pelipper(Pokemon):
    """Pelipper."""
    name = "PELIPPER"
    hp = 60
    attack = 50
    special_attack = 95
    defense = 100
    special_defense = 70
    speed = 65
    tier = 'F'
    number = 120
    exp_yield = 164
    types = [2,10]
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

class Girafarig(Pokemon):
    """Girafarig."""
    name = "GIRAFARIG"
    hp = 70
    attack = 80
    special_attack = 90
    defense = 65
    special_defense = 65
    speed = 85
    tier = 'F'
    number = 121
    exp_yield = 149
    types = [13,0]
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

class Hippopotas(Pokemon):
    """Hippopotas."""
    name = "HIPPOPOTAS"
    hp = 68
    attack = 72
    special_attack = 38
    defense = 78
    special_defense = 42
    speed = 32
    tier = 'F'
    number = 122
    exp_yield = 95
    types = [4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            34: Hippowdon
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Hippowdon(Pokemon):
    """Hippowdon."""
    name = "HIPPOWDON"
    hp = 108
    attack = 112
    special_attack = 68
    defense = 118
    special_defense = 72
    speed = 47
    tier = 'B'
    number = 123
    exp_yield = 198
    types = [4]
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

class Azurill(Pokemon):
    """Azurill."""
    name = "AZURILL"
    hp = 50
    attack = 20
    special_attack = 20
    defense = 40
    special_defense = 40
    speed = 20
    tier = 'F'
    number = 124
    exp_yield = 33
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
            10: Marill
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Marill(Pokemon):
    """Marill."""
    name = "MARILL"
    hp = 70
    attack = 20
    special_attack = 20
    defense = 50
    special_defense = 50
    speed = 40
    tier = 'F'
    number = 125
    exp_yield = 58
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            18: Azumarill
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Azumarill(Pokemon):
    """Azumarill."""
    name = "AZUMARILL"
    hp = 100
    attack = 50
    special_attack = 60
    defense = 80
    special_defense = 80
    speed = 50
    tier = 'D'
    number = 126
    exp_yield = 153
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

class Skorupi(Pokemon):
    """Skorupi."""
    name = "SKORUPI"
    hp = 40
    attack = 50
    special_attack = 30
    defense = 90
    special_defense = 55
    speed = 65
    tier = 'F'
    number = 127
    exp_yield = 114
    types = [3,6]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            40: Drapion
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Drapion(Pokemon):
    """Drapion."""
    name = "DRAPION"
    hp = 70
    attack = 90
    special_attack = 60
    defense = 110
    special_defense = 75
    speed = 95
    tier = 'B'
    number = 128
    exp_yield = 204
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

class Croagunk(Pokemon):
    """Croagunk."""
    name = "CROAGUNK"
    hp = 48
    attack = 61
    special_attack = 61
    defense = 40
    special_defense = 40
    speed = 50
    tier = 'F'
    number = 129
    exp_yield = 83
    types = [3,1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            37: Toxicroak
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Toxicroak(Pokemon):
    """Toxicroak."""
    name = "TOXICROAK"
    hp = 83
    attack = 106
    special_attack = 86
    defense = 65
    special_defense = 65
    speed = 85
    tier = 'C'
    number = 130
    exp_yield = 181
    types = [3,1]
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

class Carnivine(Pokemon):
    """Carnivine."""
    name = "CARNIVINE"
    hp = 74
    attack = 100
    special_attack = 90
    defense = 72
    special_defense = 72
    speed = 46
    tier = 'C'
    number = 131
    exp_yield = 181
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

class Remoraid(Pokemon):
    """Remoraid."""
    name = "REMORAID"
    hp = 35
    attack = 65
    special_attack = 65
    defense = 35
    special_defense = 35
    speed = 65
    tier = 'F'
    number = 132
    exp_yield = 78
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            25: Octillery
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Octillery(Pokemon):
    """Octillery."""
    name = "OCTILLERY"
    hp = 75
    attack = 105
    special_attack = 105
    defense = 75
    special_defense = 75
    speed = 45
    tier = 'F'
    number = 133
    exp_yield = 164
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

class Finneon(Pokemon):
    """Finneon."""
    name = "FINNEON"
    hp = 49
    attack = 49
    special_attack = 49
    defense = 56
    special_defense = 61
    speed = 66
    tier = 'F'
    number = 134
    exp_yield = 90
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            31: Lumineon
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Lumineon(Pokemon):
    """Lumineon."""
    name = "LUMINEON"
    hp = 69
    attack = 69
    special_attack = 69
    defense = 76
    special_defense = 86
    speed = 91
    tier = 'C'
    number = 135
    exp_yield = 156
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

class Tentacool(Pokemon):
    """Tentacool."""
    name = "TENTACOOL"
    hp = 40
    attack = 40
    special_attack = 50
    defense = 35
    special_defense = 100
    speed = 70
    tier = 'F'
    number = 136
    exp_yield = 105
    types = [10,3]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Tentacruel
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Tentacruel(Pokemon):
    """Tentacruel."""
    name = "TENTACRUEL"
    hp = 80
    attack = 70
    special_attack = 80
    defense = 65
    special_defense = 120
    speed = 100
    tier = 'B'
    number = 137
    exp_yield = 205
    types = [10,3]
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

class Feebas(Pokemon):
    """Feebas."""
    name = "FEEBAS"
    hp = 20
    attack = 15
    special_attack = 10
    defense = 20
    special_defense = 55
    speed = 80
    tier = 'F'
    number = 138
    exp_yield = 61
    types = [10]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: Max beauty ?
        evolutions = {
            26: Milotic
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Milotic(Pokemon):
    """Milotic."""
    name = "MILOTIC"
    hp = 95
    attack = 60
    special_attack = 100
    defense = 79
    special_defense = 125
    speed = 81
    tier = 'A'
    number = 139
    exp_yield = 213
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

class Mantyke(Pokemon):
    """Mantyke."""
    name = "MANTYKE"
    hp = 45
    attack = 20
    special_attack = 60
    defense = 50
    special_defense = 120
    speed = 50
    tier = 'E'
    number = 140
    exp_yield = 108
    types = [10,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: ... w remoraid in party
        evolutions = {
            30: Mantine
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Mantine(Pokemon):
    """Mantine."""
    name = "MANTINE"
    hp = 85
    attack = 40
    special_attack = 80
    defense = 70
    special_defense = 140
    speed = 70
    tier = 'C'
    number = 141
    exp_yield = 168
    types = [10,2]
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

class Snover(Pokemon):
    """Snover."""
    name = "SNOVER"
    hp = 60
    attack = 62
    special_attack = 62
    defense = 50
    special_defense = 60
    speed = 40
    tier = 'F'
    number = 142
    exp_yield = 131
    types = [14,11]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            40: Abomasnow
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Abomasnow(Pokemon):
    """Abomasnow."""
    name = "ABOMASNOW"
    hp = 90
    attack = 92
    special_attack = 92
    defense = 75
    special_defense = 85
    speed = 60
    tier = 'C'
    number = 143
    exp_yield = 214
    types = [14,11]
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

class Sneasel(Pokemon):
    """Sneasel."""
    name = "SNEASEL"
    hp = 55
    attack = 95
    special_attack = 35
    defense = 55
    special_defense = 75
    speed = 115
    tier = 'D'
    number = 144
    exp_yield = 132
    types = [16,14]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: razor claw at night
        evolutions = {
            34: Weavile
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Weavile(Pokemon):
    """Weavile."""
    name = "WEAVILE"
    hp = 70
    attack = 120
    special_attack = 45
    defense = 65
    special_defense = 85
    speed = 125
    tier = 'B'
    number = 145
    exp_yield = 199
    types = [16,14]
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

class Uxie(Pokemon):
    """Uxie."""
    name = "UXIE"
    hp = 75
    attack = 75
    special_attack = 75
    defense = 130
    special_defense = 130
    speed = 95
    tier = 'S'
    number = 146
    exp_yield = 210
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

class Mesprit(Pokemon):
    """Mesprit."""
    name = "MESPRIT"
    hp = 80
    attack = 105
    special_attack = 105
    defense = 105
    special_defense = 105
    speed = 80
    tier = 'S'
    number = 147
    exp_yield = 210
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

class Azelf(Pokemon):
    """Azelf."""
    name = "AZELF"
    hp = 75
    attack = 125
    special_attack = 125
    defense = 70
    special_defense = 70
    speed = 115
    tier = 'S'
    number = 148
    exp_yield = 210
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

class Dialga(Pokemon):
    """Dialga."""
    name = "DIALGA"
    hp = 100
    attack = 120
    special_attack = 150
    defense = 120
    special_defense = 100
    speed = 90
    tier = 'S'
    number = 149
    exp_yield = 220
    types = [15,8]
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

class Palkia(Pokemon):
    """Palkia."""
    name = "PALKIA"
    hp = 90
    attack = 120
    special_attack = 150
    defense = 100
    special_defense = 120
    speed = 100
    tier = 'S'
    number = 150
    exp_yield = 220
    types = [15,10]
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

class Manaphy(Pokemon):
    """Manaphy."""
    name = "MANAPHY"
    hp = 100
    attack = 100
    special_attack = 100
    defense = 100
    special_defense = 100
    speed = 100
    tier = 'S'
    number = 151
    exp_yield = 215
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

class Gligar(Pokemon):
    """Gligar."""
    name = "GLIGAR"
    hp = 65
    attack = 75
    special_attack = 35
    defense = 105
    special_defense = 65
    speed = 85
    tier = 'D'
    number = 153
    exp_yield = 108
    types = [2,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: razor fang at night
        evolutions = {
            35: Gliscor
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gliscor(Pokemon):
    """Gliscor."""
    name = "GLISCOR"
    hp = 75
    attack = 95
    special_attack = 45
    defense = 125
    special_defense = 75
    speed = 95
    tier = 'D'
    number = 154
    exp_yield = 192
    types = [2,4]
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

class Ralts(Pokemon):
    """Ralts."""
    name = "RALTS"
    hp = 28
    attack = 25
    special_attack = 45
    defense = 25
    special_defense = 35
    speed = 40
    tier = 'F'
    number = 157
    exp_yield = 70
    types = [13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            20: Kirlia
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Kirlia(Pokemon):
    """Kirlia."""
    name = "KIRLIA"
    hp = 38
    attack = 35
    special_attack = 65
    defense = 35
    special_defense = 55
    speed = 50
    tier = 'F'
    number = 158
    exp_yield = 140
    types = [13]
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
                30: Gallade
            }
        else:
            evolutions = {
                30: Gardevoir
            }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Gardevoir(Pokemon):
    """Gardevoir."""
    name = "GARDEVOIR"
    hp = 68
    attack = 65
    special_attack = 125
    defense = 65
    special_defense = 115
    speed = 80
    tier = 'B'
    number = 159
    exp_yield = 208
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

class Gallade(Pokemon):
    """Gallade."""
    name = "GALLADE"
    hp = 68
    attack = 125
    special_attack = 65
    defense = 65
    special_defense = 115
    speed = 80
    tier = 'B'
    number = 160
    exp_yield = 208
    types = [13,1]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: lookup level of learning rollout
        evolutions = {
            26: Lickitung
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Lickitung(Pokemon):
    """Lickitung."""
    name = "LICKITUNG"
    hp = 90
    attack = 55
    special_attack = 60
    defense = 75
    special_defense = 75
    speed = 30
    tier = 'E'
    number = 161
    exp_yield = 127
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: lookup when learns rollout
        evolutions = {
            27: Lickilicky
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Lickilicky(Pokemon):
    """Lickilicky."""
    name = "LICKILICKY"
    hp = 110
    attack = 85
    special_attack = 80
    defense = 95
    special_defense = 95
    speed = 50
    tier = 'B'
    number = 162
    exp_yield = 193
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

class Eevee(Pokemon):
    """Eevee."""
    name = "EEVEE"
    hp = 55
    attack = 55
    special_attack = 45
    defense = 50
    special_defense = 65
    speed = 55
    tier = 'F'
    number = 163
    exp_yield = 92
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolution = np.random.choice([Vaporeon, Jolteon, Flareon, Espeon, Umbreon, Leafeon, Glaceon])
        evolutions = {
            25: evolution
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Vaporeon(Pokemon):
    """Vaporeon."""
    name = "VAPOREON"
    hp = 130
    attack = 65
    special_attack = 110
    defense = 60
    special_defense = 95
    speed = 65
    tier = 'B'
    number = 164
    exp_yield = 196
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

class Jolteon(Pokemon):
    """Jolteon."""
    name = "JOLTEON"
    hp = 65
    attack = 65
    special_attack = 110
    defense = 60
    special_defense = 95
    speed = 130
    tier = 'B'
    number = 165
    exp_yield = 197
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

class Flareon(Pokemon):
    """Flareon."""
    name = "FLAREON"
    hp = 65
    attack = 130
    special_attack = 95
    defense = 60
    special_defense = 110
    speed = 65
    tier = 'B'
    number = 166
    exp_yield = 198
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

class Espeon(Pokemon):
    """Espeon."""
    name = "ESPEON"
    hp = 65
    attack = 65
    special_attack = 130
    defense = 60
    special_defense = 95
    speed = 110
    tier = 'B'
    number = 167
    exp_yield = 197
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

class Umbreon(Pokemon):
    """Umbreon."""
    name = "UMBREON"
    hp = 95
    attack = 65
    special_attack = 60
    defense = 110
    special_defense = 130
    speed = 65
    tier = 'B'
    number = 168
    exp_yield = 197
    types = [16]
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

class Leafeon(Pokemon):
    """Leafeon."""
    name = "LEAFEON"
    hp = 65
    attack = 110
    special_attack = 60
    defense = 130
    special_defense = 65
    speed = 95
    tier = 'B'
    number = 169
    exp_yield = 197
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

class Glaceon(Pokemon):
    """Glaceon."""
    name = "GLACEON"
    hp = 65
    attack = 60
    special_attack = 130
    defense = 110
    special_defense = 95
    speed = 65
    tier = 'B'
    number = 170
    exp_yield = 197
    types = [14]
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

class Swablu(Pokemon):
    """Swablu."""
    name = "SWABLU"
    hp = 45
    attack = 40
    special_attack = 40
    defense = 60
    special_defense = 75
    speed = 50
    tier = 'F'
    number = 171
    exp_yield = 74
    types = [15,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            35: Altaria
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Altaria(Pokemon):
    """Altaria."""
    name = "ALTARIA"
    hp = 75
    attack = 70
    special_attack = 70
    defense = 90
    special_defense = 105
    speed = 80
    tier = 'C'
    number = 172
    exp_yield = 188
    types = [15,2]
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

class Togepi(Pokemon):
    """Togepi."""
    name = "TOGEPI"
    hp = 35
    attack = 20
    special_attack = 40
    defense = 65
    special_defense = 65
    speed = 20
    tier = 'F'
    number = 173
    exp_yield = 74
    types = [0]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: high friendship
        evolutions = {
            14: Togetic
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Togetic(Pokemon):
    """Togetic."""
    name = "TOGETIC"
    hp = 55
    attack = 40
    special_attack = 80
    defense = 85
    special_defense = 105
    speed = 40
    tier = 'D'
    number = 174
    exp_yield = 114
    types = [0,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: shiny stone
        evolutions = {
            28: Togekiss
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Togekiss(Pokemon):
    """Togekiss."""
    name = "TOGEKISS"
    hp = 85
    attack = 50
    special_attack = 120
    defense = 95
    special_defense = 115
    speed = 80
    tier = 'A'
    number = 175
    exp_yield = 220
    types = [0,2]
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

class Houndour(Pokemon):
    """Houndour."""
    name = "HOUNDOUR"
    hp = 45
    attack = 60
    special_attack = 80
    defense = 30
    special_defense = 50
    speed = 65
    tier = 'F'
    number = 176
    exp_yield = 114
    types = [16,9]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            24: Houndoom
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Houndoom(Pokemon):
    """Houndoom."""
    name = "HOUNDOOM"
    hp = 75
    attack = 90
    special_attack = 110
    defense = 50
    special_defense = 80
    speed = 95
    tier = 'B'
    number = 177
    exp_yield = 204
    types = [16,9]
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

class Magnemite(Pokemon):
    """Magnemite."""
    name = "MAGNEMITE"
    hp = 25
    attack = 35
    special_attack = 95
    defense = 70
    special_defense = 55
    speed = 45
    tier = 'F'
    number = 178
    exp_yield = 89
    types = [8,12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Magneton
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Magneton(Pokemon):
    """Magneton."""
    name = "MAGNETON"
    hp = 50
    attack = 60
    special_attack = 120
    defense = 95
    special_defense = 70
    speed = 70
    tier = 'C'
    number = 179
    exp_yield = 161
    types = [8,12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            40: Magnezone
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Magnezone(Pokemon):
    """Magnezone."""
    name = "MAGNEZONE"
    hp = 70
    attack = 70
    special_attack = 130
    defense = 115
    special_defense = 90
    speed = 60
    tier = 'A'
    number = 180
    exp_yield = 211
    types = [8,12]
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

class Rhyhorn(Pokemon):
    """Rhyhorn."""
    name = "RHYHORN"
    hp = 80
    attack = 85
    special_attack = 30
    defense = 95
    special_defense = 30
    speed = 25
    tier = 'E'
    number = 186
    exp_yield = 135
    types = [5,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            42: Rhydon
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Rhydon(Pokemon):
    """Rhydon."""
    name = "RHYDON"
    hp = 105
    attack = 130
    special_attack = 45
    defense = 120
    special_defense = 45
    speed = 40
    tier = 'C'
    number = 187
    exp_yield = 204
    types = [5,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            48: Rhyperior
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Rhyperior(Pokemon):
    """Rhyperior."""
    name = "RHYPERIOR"
    hp = 115
    attack = 140
    special_attack = 55
    defense = 130
    special_defense = 55
    speed = 40
    tier = 'A'
    number = 188
    exp_yield = 217
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

class Duskull(Pokemon):
    """Duskull."""
    name = "DUSKULL"
    hp = 20
    attack = 40
    special_attack = 30
    defense = 90
    special_defense = 90
    speed = 25
    tier = 'F'
    number = 189
    exp_yield = 97
    types = [7]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            37: Dusclops
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Dusclops(Pokemon):
    """Dusclops."""
    name = "DUSCLOPS"
    hp = 40
    attack = 70
    special_attack = 60
    defense = 130
    special_defense = 130
    speed = 25
    tier = 'C'
    number = 190
    exp_yield = 179
    types = [7]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            46: Dusknoir
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Dusknoir(Pokemon):
    """Dusknoir."""
    name = "DUSKNOIR"
    hp = 45
    attack = 100
    special_attack = 65
    defense = 135
    special_defense = 135
    speed = 45
    tier = 'B'
    number = 191
    exp_yield = 210
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

class Scyther(Pokemon):
    """Scyther."""
    name = "DUSKNOIR"
    hp = 70
    attack = 110
    special_attack = 55
    defense = 80
    special_defense = 80
    speed = 105
    tier = 'B'
    number = 195
    exp_yield = 187
    types = [6,2]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            32: Scizor
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Scizor(Pokemon):
    """Scizor."""
    name = "SCIZOR"
    hp = 70
    attack = 130
    special_attack = 55
    defense = 100
    special_defense = 80
    speed = 65
    tier = 'B'
    number = 196
    exp_yield = 200
    types = [8,6]
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

class Elekid(Pokemon):
    """Elekid."""
    name = "ELEKID"
    hp = 45
    attack = 63
    special_attack = 65
    defense = 37
    special_defense = 55
    speed = 95
    tier = 'E'
    number = 197
    exp_yield = 106
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Electabuzz
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Electabuzz(Pokemon):
    """Electabuzz."""
    name = "ELECTABUZZ"
    hp = 65
    attack = 83
    special_attack = 95
    defense = 57
    special_defense = 85
    speed = 105
    tier = 'C'
    number = 198
    exp_yield = 156
    types = [12]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: hold electirizer
        evolutions = {
            40: Electivire
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Electivire(Pokemon):
    """Electivire."""
    name = "ELECTIVIRE"
    hp = 75
    attack = 123
    special_attack = 95
    defense = 67
    special_defense = 85
    speed = 95
    tier = 'A'
    number = 199
    exp_yield = 199
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

class Magby(Pokemon):
    """Magby."""
    name = "MAGBY"
    hp = 45
    attack = 75
    special_attack = 70
    defense = 37
    special_defense = 55
    speed = 83
    tier = 'E'
    number = 200
    exp_yield = 117
    types = [9]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Magmar
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Magmar(Pokemon):
    """Magmar."""
    name = "MAGMAR"
    hp = 65
    attack = 95
    special_attack = 100
    defense = 57
    special_defense = 85
    speed = 93
    tier = 'C'
    number = 201
    exp_yield = 167
    types = [9]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: magmarizer
        evolutions = {
            40: Magmortar
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Magmortar(Pokemon):
    """Magmortar."""
    name = "MAGMORTAR"
    hp = 75
    attack = 95
    special_attack = 125
    defense = 67
    special_defense = 89
    speed = 83
    tier = 'A'
    number = 202
    exp_yield = 199
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

class Swinub(Pokemon):
    """Swinub."""
    name = "SWINUB"
    hp = 50
    attack = 50
    special_attack = 30
    defense = 40
    special_defense = 30
    speed = 50
    tier = 'F'
    number = 203
    exp_yield = 78
    types = [14,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            33: Piloswine
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Piloswine(Pokemon):
    """Piloswine."""
    name = "PILOSWINE"
    hp = 100
    attack = 100
    special_attack = 60
    defense = 80
    special_defense = 60
    speed = 50
    tier = 'C'
    number = 204
    exp_yield = 160
    types = [14,4]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        # TODO: lookup level learns ANCIENT POWER
        evolutions = {
            34: Mamoswine
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Mamoswine(Pokemon):
    """Mamoswine."""
    name = "MAMOSWINE"
    hp = 110
    attack = 130
    special_attack = 70
    defense = 80
    special_defense = 60
    speed = 80
    tier = 'A'
    number = 205
    exp_yield = 207
    types = [14,4]
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

class Snorunt(Pokemon):
    """Snorunt."""
    name = "SNORUNT"
    hp = 50
    attack = 50
    special_attack = 50
    defense = 50
    special_defense = 50
    speed = 50
    tier = 'F'
    number = 206
    exp_yield = 74
    types = [14]
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
                42: Glalie
            }
        else:
            evolutions = {
                42: Froslass
            }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Glalie(Pokemon):
    """Glalie."""
    name = "GLALIE"
    hp = 80
    attack = 80
    special_attack = 80
    defense = 80
    special_defense = 80
    speed = 80
    tier = 'C'
    number = 207
    exp_yield = 187
    types = [14]
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

class Froslass(Pokemon):
    """Froslass."""
    name = "FROSLASS"
    hp = 70
    attack = 80
    special_attack = 80
    defense = 70
    special_defense = 70
    speed = 110
    tier = 'C'
    number = 208
    exp_yield = 187
    types = [14,7]
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

class Absol(Pokemon):
    """Absol."""
    name = "ABSOL"
    hp = 65
    attack = 130
    special_attack = 75
    defense = 60
    special_defense = 60
    speed = 75
    tier = 'C'
    number = 209
    exp_yield = 174
    types = [16]
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

class Pinsir(Pokemon):
    """Pinsir."""
    name = "PINSIR"
    hp = 65
    attack = 125
    special_attack = 55
    defense = 100
    special_defense = 70
    speed = 85
    tier = 'B'
    number = 210
    exp_yield = 200
    types = [6]
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

class Smoochum(Pokemon):
    """Smoochum."""
    name = "SMOOCHUM"
    hp = 45
    attack = 30
    special_attack = 85
    defense = 15
    special_defense = 65
    speed = 65
    tier = 'F'
    number = 211
    exp_yield = 87
    types = [6,13]
    front_sprite = pg.image.load("sprites/pokemon front/"+name.lower()+"_front.png")
    back_sprite = pg.image.load("sprites/pokemon back/" + name.lower() + "_back.png")

    def __init__(self, gender=None, moveset=None, nickname=None, level=None, xp=None):
        # TODO: MOVE TABLE
        movetable = {
            1: Pound
        }
        evolutions = {
            30: Jynx
        }

        super().__init__(self.name, nickname=nickname,
                         hp=self.hp, attack=self.attack,special_attack=self.special_attack, defense=self.defense,
                         special_defense=self.special_defense, speed=self.speed,
                         types=self.types, gender=gender, level=level, xp=xp, moveset=moveset, movetable=movetable,
                         front_sprite=pg.sprite.Sprite(self.front_sprite),
                         back_sprite=pg.sprite.Sprite(self.back_sprite),
                         exp_yield=self.exp_yield, evolutions=evolutions)

class Jynx(Pokemon):
    """Jynx."""
    name = "JYNX"
    hp = 65
    attack = 50
    special_attack = 115
    defense = 35
    special_defense = 95
    speed = 95
    tier = 'C'
    number = 212
    exp_yield = 137
    types = [6,13]
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
    113: Snorlax,
    114: Unown,
    115: Riolu,
    116: Lucario,
    117: Wooper,
    118: Quagsire,
    119: Wingull,
    120: Pelipper,
    121: Girafarig,
    122: Hippopotas,
    123: Hippowdon,
    124: Azurill,
    125: Marill,
    126: Azumarill,
    127: Skorupi,
    128: Drapion,
    129: Croagunk,
    130: Toxicroak,
    131: Carnivine,
    132: Remoraid,
    133: Octillery,
    134: Finneon,
    135: Lumineon,
    136: Tentacool,
    137: Tentacruel,
    138: Feebas,
    139: Milotic,
    140: Mantyke,
    141: Mantine,
    142: Snover,
    143: Abomasnow,
    144: Sneasel,
    145: Weavile,
    146: Uxie,
    147: Mesprit,
    148: Azelf,
    149: Dialga,
    150: Palkia,
    151: Manaphy,
    153: Gligar,
    154: Gliscor,
    157: Ralts,
    158: Kirlia,
    159: Gardevoir,
    160: Gallade,
    161: Lickitung,
    162: Lickilicky,
    163: Eevee,
    164: Vaporeon,
    165: Jolteon,
    166: Flareon,
    167: Espeon,
    168: Umbreon,
    169: Leafeon,
    170: Glaceon,
    171: Swablu,
    172: Altaria,
    173: Togepi,
    174: Togetic,
    175: Togekiss,
    176: Houndour,
    177: Houndoom,
    178: Magnemite,
    179: Magneton,
    180: Magnezone,
    186: Rhyhorn,
    187: Rhydon,
    188: Rhyperior,
    189: Duskull,
    190: Dusclops,
    191: Dusknoir,
    195: Scyther,
    196: Scizor,
    197: Elekid,
    198: Electabuzz,
    199: Electivire,
    200: Magby,
    201: Magmar,
    202: Magmortar,
    203: Swinub,
    204: Piloswine,
    205: Mamoswine,
    206: Snorunt,
    207: Glalie,
    208: Froslass,
    209: Absol,
    210: Pinsir,
    211: Smoochum,
    212: Jynx
}


pokeball_sprite = pg.sprite.Sprite(pg.image.load("sprites/items/pokeball.png"))
TEST_TRAINER = PokemonTrainer(pokemon=[Empoleon(level=45, nickname="soup dumpling"), Torterra(level=50), Infernape(level=55)],
                              items=[
                                  PokeballItem(value=0, name="Pokeball",sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Great Ball", count=10,sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Ultra Ball", count=100,sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Pokeball", count=9,sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Great Ball", count=20,sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Ultra Ball", count=200,sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Pokeball", count=80,sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Great Ball", count=7,sprite=pokeball_sprite),
                                  PokeballItem(value=0, name="Ultra Ball", count=60,sprite=pokeball_sprite),
                                  Item(value=1, kind=1, name="Test battle item",sprite=pokeball_sprite),
                                  BattleItem(value=100, name="Hyper Potion", count=20,sprite=None),
                                  BattleItem(value=100, name="Potion", count=10,sprite=None),
                                  BattleItem(value=100, name="Potion", count=10,sprite=None),
                                  KeyItem(None, name="Test key item 1", sprite=None),
                              ],
                              money=0)

