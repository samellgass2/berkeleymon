from game_utils.Encounter import *
from data.Constants import *

##### ALL MOVES #####
class Splash(PokemonMove):
    def __init__(self):
        super().__init__(type=10, name="Splash", power=0, physical=True, accuracy=100,pp=35, is_status=True)

class Pound(PokemonMove):
    """Pound."""
    def __init__(self):
        super().__init__(type=0, name="Pound", power=40, physical=True, accuracy=100, pp=35)

class Tackle(PokemonMove):
    """Tackle."""
    def __init__(self):
        super().__init__(type=0, name="Tackle", power=35, physical=True, accuracy=95, pp=35)

class Withdraw(PokemonMove):
    """Withdraw."""
    def __init__(self):
        super().__init__(type=10, name="Withdraw", power=0, physical=False, accuracy=100, pp=40, is_status=True)

    def use(self, opponent):
        self.raise_stat("defense", opponent)
        self.pp -= 1

class Growl(PokemonMove):
    """Growl."""
    def __init__(self):
        super().__init__(type=0, name="Growl", power=0, physical=False, accuracy=100, pp=40, is_status=True)

    def use(self, opponent):
        opponent.raise_stat("attack", opponent, lower=True)
        self.pp -= 1

class Absorb(PokemonMove):
    """Absorb."""
    def __init__(self):
        super().__init__(type=11, name="Absorb", power=20, physical=False, accuracy=100, pp=25, is_status=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit:
            self.user.take_damage(-total_damage // 2)
            self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!",overworld=False, unskippable=False), skip_queue=True)
        return is_crit, is_super_eff, is_hit, total_damage

class RazorLeaf(PokemonMove):
    """Razor Leaf."""
    def __init__(self):
        super().__init__(type=11, name="Razor Leaf", power=55, accuracy=95, physical=True,pp=25)

class Curse(PokemonMove):
    """Curse."""
    def __init__(self):
        super().__init__(type=7, name="Curse", power=0, accuracy=100, physical=False, pp=10)

    def use(self, opponent):
        self.raise_stat(opponent, key="speed", lower=True, lower_self=True)
        self.raise_stat(opponent, key="attack")
        self.raise_stat(opponent, key="defense")
        self.pp -= 1

class Bite(PokemonMove):
    def __init__(self):
        super().__init__(type=16, name="Bite", power=60, accuracy=100, pp=25, physical=True)

    # TODO: may cause flinch

class MegaDrain(PokemonMove):
    def __init__(self):
        super().__init__(type=11, name="Mega drain", power=40, accuracy=100, pp=15, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit:
            self.user.take_damage(-total_damage // 2)
            self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!",overworld=False, unskippable=False), skip_queue=True)
        return is_crit, is_super_eff, is_hit, total_damage

class LeechSeed(PokemonMove):
    """Leech Seed."""
    def __init__(self):
        super().__init__(type=11, name="Leech Seed", power=0, physical=False, accuracy=90, pp=10, is_status=True)

    # TODO: IMPLEMENT LEECHING AS A STATUS

class Synthesis(PokemonMove):
    """Synthesis."""
    def __init__(self):
        super().__init__(type=11, name="Synthesis", power=0, physical=False, accuracy=100, pp=10, is_status=True)

    def use(self, opponent):
        healing = np.random.choice(range(self.user.stats["max_hp"] // 3, self.user.stats["max_hp"] // 2))
        self.user.take_damage(-healing)
        self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!", overworld=False, unskippable=False))
        return False, False, True, 0

class Crunch(PokemonMove):
    """Crunch."""
    def __init__(self):
        super().__init__(type=16, name="Crunch", power=80, physical=True, accuracy=100, pp=15)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # may lower defense
        if np.random.random() <= 0.2:
            self.raise_stat(opponent, "defense", lower=True)
        return is_crit, is_super_eff, is_hit, total_damage

class GigaDrain(PokemonMove):
    """Giga Drain."""
    def __init__(self):
        super().__init__(type=11, name="Mega drain", power=60, accuracy=100, pp=10, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        # TODO: FIND A MORE KOSHER WAY TO IMPLEMENT THIS
        if is_hit:
            self.user.take_damage(-total_damage // 2)
            self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!",overworld=False, unskippable=False), skip_queue=True)
        return is_crit, is_super_eff, is_hit, total_damage

class LeafStorm(PokemonMove):
    """Leaf Storm."""
    def __init__(self):
        super().__init__(type=11, name="Leaf Storm", power=140, accuracy=90, pp=5, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        self.raise_stat(opponent, "special attack", lower=True, lower_self=True, sharply=True)
        return is_crit, is_super_eff, is_hit, total_damage

class Earthquake(PokemonMove):
    """Earthquake."""
    def __init__(self):
        super().__init__(type=4, name="Earthquake", power=100, accuracy=100, pp=10, physical=True)

class Scratch(PokemonMove):
    """Scratch."""
    def __init__(self):
        super().__init__(type=0, name="Scratch", power=40, accuracy=100, pp=35, physical=True)

class Leer(PokemonMove):
    """Leer."""
    def __init__(self):
        super().__init__(type=0, name="Leer", power=0, accuracy=100, pp=35, physical=False)

    def use(self, opponent):
        self.raise_stat(opponent, "defense", lower=True)
        return False, False, True, 0

class Ember(PokemonMove):
    """Ember."""
    def __init__(self):
        super().__init__(type=9, name="Ember", power=40, accuracy=100, pp=25, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_status("burn")
        return is_crit, is_super_eff, is_hit, total_damage

class Taunt(PokemonMove):
    """Taunt."""
    def __init__(self):
        super().__init__(type=16, name="Taunt", power=0, accuracy=100, pp=20, physical=False)

    # TODO: MAKE TAUNT WORK
    def use(self, opponent):
        return False, False, True, 0

class FurySwipes(PokemonMove):
    """Fury Swipes."""
    def __init__(self):
        super().__init__(type=0, name="Fury Swipes", power=18, accuracy=80, pp=15, physical=True)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        times_hit = np.random.choice(range(2,6))
        return is_crit, is_super_eff, is_hit, times_hit * total_damage

class FlameWheel(PokemonMove):
    """Flame Wheel."""
    def __init__(self):
        super().__init__(type=9, name="Flame Wheel", power=60, physical=True, accuracy=100, pp=25)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_status("burn")
        return is_crit, is_super_eff, is_hit, total_damage

class NastyPlot(PokemonMove):
    """Nasty Plot."""
    def __init__(self):
        super().__init__(type=16, name="Nasty Plot", power=0, physical=True, accuracy=100, pp=20)


    def use(self, opponent):
        self.raise_stat(opponent, "special attack", sharply=True)
        return False, False, True, 0

class Torment(PokemonMove):
    """Torment."""
    def __init__(self):
        super().__init__(type=16, name="Torment", power=0, physical=False, accuracy=100, pp=15)

    # TODO: figure ouot how to do torment
    def use(self, opponent):
        return False, False, True, 0

class Facade(PokemonMove):
    """Facade."""
    def __init__(self):
        super().__init__(type=0, name="Facade", power=70, physical=True, accuracy=100, pp=20)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if self.user.status is not None and self.user.status in ["paralysis", "burn", "poison"]:
            total_damage *= 2
        return is_crit, is_super_eff, is_hit, total_damage

class FireSpin(PokemonMove):
    """Fire Spin."""
    def __init__(self):
        super().__init__(type=9, name="Fire Spin", power=15, physical=True, accuracy=70, pp=15)

    # TODO: make lasting status somehow

class SlackOff(PokemonMove):
    """Slack Off."""
    def __init__(self):
        super().__init__(type=0, name="Slack Off.", power=0, physical=False, accuracy=100, pp=10, is_status=True)

    def use(self, opponent):
        healing = np.random.choice(range(self.user.stats["max_hp"] // 3, self.user.stats["max_hp"] // 2))
        self.user.take_damage(-healing)
        self.user.trainer.board.display_text(TextBox(self.user.name+" was healed!", overworld=False, unskippable=False))
        return False, False, True, 0

class FlameThrower(PokemonMove):
    """Flame Thrower."""
    def __init__(self):
        super().__init__(type=9, name="Flame Thrower", power=95, accuracy=100, pp=15, physical=False)

    def use(self, opponent):
        is_crit, is_super_eff, is_hit, total_damage = super().use(opponent)
        if np.random.random() <= 0.1:
            opponent.inflict_status("burn")
        return is_crit, is_super_eff, is_hit, total_damage

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